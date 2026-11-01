"""Extra Step-2 analyses (read-only on all existing files; writes new CSVs only).

Usage (paths to the two unzipped folders):
    python step2_extra_analyses.py  path/to/hinglish_asr_sum  path/to/step2_results

Writes into step2_results/extra/:
  conditional_retention.csv   - of facts the ORACLE summary supported, share still
                                supported under each condition (retention), and of
                                facts the oracle missed, share newly supported (gain);
                                window-cluster bootstrap CI for real-ASR rows
  en_fact_table.csv           - the 21 English-tagged facts (W00-W15): what Trelis did to
                                the English tokens of each evidence span + judge decisions
  noise_en_token_fate.csv     - fate of English reference tokens in each noise condition
  whisper_small_repetition_sensitivity.csv
"""
import os
import re
import sys
import difflib

import numpy as np
import pandas as pd
from scipy.stats import fisher_exact, wilcoxon

ROOT, RES = sys.argv[1], sys.argv[2]
B = os.path.join(ROOT, "outputs")
OUT = os.path.join(RES, "extra")
os.makedirs(OUT, exist_ok=True)
W16 = [f"W{i:02d}" for i in range(16)]

facts = pd.read_csv(f"{B}/step2/silver_facts.csv")
sw = pd.read_csv(f"{B}/selected_windows.csv").set_index("window_id")
pw = pd.read_csv(f"{B}/asr_metrics_per_window_vad15.csv")
cond_txt = pd.read_csv(f"{B}/step2/conditions.csv")
j = pd.read_csv(f"{RES}/judgements.csv")
j = j[j.kind == "summary"].merge(facts[["fact_id", "tag"]], on="fact_id")

LAT = re.compile(r"^[a-z0-9']+$")
DEV = re.compile(r"[ऀ-ॿ]")


def token_fate(ref, hyp):
    """Per reference token: ok / dev (replaced by Devanagari) / lat (other Latin) / del."""
    out = ["?"] * len(ref)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ref, hyp, autojunk=False).get_opcodes():
        dv = any(DEV.search(x) for x in hyp[j1:j2])
        for k in range(i1, i2):
            out[k] = "ok" if op == "equal" else "del" if op == "delete" else ("dev" if dv else "lat")
    return out


# ---------- 1. conditional retention ----------
wide = j.pivot_table(index=["window_id", "fact_id", "tag"], columns="condition",
                     values="supported").astype(int).reset_index()
rng = np.random.default_rng(13)
wins = wide.window_id.unique()
groups = {w: wide[wide.window_id == w] for w in wins}


def retention(d, c):
    k = d[d.oracle == 1]
    return k[c].mean() if len(k) else np.nan


def boot_ci(c, tag, n=2000):
    vals = []
    for _ in range(n):
        d = pd.concat([groups[w] for w in rng.choice(wins, len(wins))])
        if tag != "all":
            d = d[d.tag == tag]
        v = retention(d, c)
        if v == v:
            vals.append(v)
    return np.percentile(vals, [2.5, 97.5])


rows = []
for c in [x for x in wide.columns if str(x).startswith(("asr", "noise"))]:
    for tag in ["all", "hi", "mixed", "en"]:
        d = wide if tag == "all" else wide[wide.tag == tag]
        k, g = d[d.oracle == 1], d[d.oracle == 0]
        row = dict(condition=c, tag=tag, n_oracle_supported=len(k), retained=int(k[c].sum()),
                   retention=k[c].mean(), n_oracle_missed=len(g), gained=int(g[c].sum()),
                   gain_rate=g[c].mean(), ci_lo=np.nan, ci_hi=np.nan)
        if c.startswith("asr"):
            row["ci_lo"], row["ci_hi"] = boot_ci(c, tag)
        rows.append(row)
ret = pd.DataFrame(rows)
ret.to_csv(f"{OUT}/conditional_retention.csv", index=False)

t = ret[(ret.condition == "asr:trelis-hinglish-preview")].set_index("tag")
en, hm = t.loc["en"], t.loc[["hi", "mixed"]].sum()
p = fisher_exact([[en.retained, en.n_oracle_supported - en.retained],
                  [hm.retained, hm.n_oracle_supported - hm.retained]]).pvalue
print(f"Trelis retention: en {en.retained}/{en.n_oracle_supported} vs hi+mixed "
      f"{int(hm.retained)}/{int(hm.n_oracle_supported)}; Fisher p={p:.3f} "
      "(treats facts as independent - they cluster in windows, so optimistic)")

# ---------- 2. English-fact table ----------
fates = {}
en_facts = facts[facts.located & (facts.tag == "en") & facts.window_id.isin(W16)]
for m in ["trelis-hinglish-preview", "whisper-small"]:
    for w in en_facts.window_id.unique():
        ref = sw.loc[w, "ref_norm"].split()
        hyp = str(pw[(pw.window_id == w) & (pw.model == m)].hyp_norm.iloc[0]).split()
        fates[(m, w)] = token_fate(ref, hyp)
rows = []
for _, r in en_facts.iterrows():
    ref = sw.loc[r.window_id, "ref_norm"].split()
    a, b = int(r.span_start), int(r.span_end)  # token indices into ref_norm
    sup = j[j.fact_id == r.fact_id].set_index("condition").supported
    row = dict(fact_id=r.fact_id, fact=r.fact)
    for m, short in [("trelis-hinglish-preview", "trelis"), ("whisper-small", "wsmall")]:
        lat = [x for t_, x in zip(ref[a:b], fates[(m, r.window_id)][a:b]) if LAT.match(t_)]
        n = max(1, len(lat))
        row.update({f"{short}_en_ok": lat.count("ok") / n, f"{short}_en_dev": lat.count("dev") / n,
                    f"{short}_en_other": (lat.count("lat") + lat.count("del")) / n})
    row["n_en_tokens_in_evidence"] = len(lat)
    for c in ["oracle", "asr:trelis-hinglish-preview", "asr:whisper-small"]:
        row[f"supported_{c}"] = int(sup[c])
    rows.append(row)
pd.DataFrame(rows).to_csv(f"{OUT}/en_fact_table.csv", index=False)

# ---------- 3. English-token fate in noise conditions ----------
rows = []
for c in sorted(cond_txt.condition.unique()):
    if not c.startswith("noise"):
        continue
    cnt = {"ok": 0, "dev": 0, "lat": 0, "del": 0}
    for w in W16:
        ref = sw.loc[w, "ref_norm"].split()
        hyp = cond_txt[(cond_txt.window_id == w) & (cond_txt.condition == c)].text.iloc[0].split()
        for t_, x in zip(ref, token_fate(ref, hyp)):
            if LAT.match(t_):
                cnt[x] += 1
    n = sum(cnt.values())
    rows.append({"condition": c, **{f"share_{k}": v / n for k, v in cnt.items()}, "n_en_tokens": n})
pd.DataFrame(rows).to_csv(f"{OUT}/noise_en_token_fate.csv", index=False)

# ---------- 4. whisper-small repetition sensitivity ----------
m = pd.read_csv(f"{RES}/summary_metrics_per_item.csv")
m = m[m.out_lang == "en"]
rep = set(pw[(pw.model == "whisper-small") & pw.flag_repetition].window_id)
o = m[m.condition == "oracle"].set_index("window_id")
ws = m[m.condition == "asr:whisper-small"].set_index("window_id")
rows = []
for name, keep in [("all_16", list(o.index)), ("no_repetition_flag", [x for x in o.index if x not in rep])]:
    d = ws.loc[keep, "recall_all"] - o.loc[keep, "recall_all"]
    rows.append(dict(subset=name, n_windows=len(keep), recall_diff=d.mean(),
                     wilcoxon_p=wilcoxon(d).pvalue,
                     rougeL_diff=(ws.loc[keep, "rougeL"] - o.loc[keep, "rougeL"]).mean()))
pd.DataFrame(rows).to_csv(f"{OUT}/whisper_small_repetition_sensitivity.csv", index=False)
print(pd.DataFrame(rows).round(3).to_string())
print("wrote", OUT)
