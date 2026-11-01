"""Final analysis: every condition, every metric, all judging passes (25 windows).

Usage:
  python final_analysis.py --root hinglish_asr_sum --pass1 judgements_25w.csv \
      --pass2 judgements_script_shift.csv --pass3 judgements_pass3_hinglish_noise.csv \
      --v2 summaries_v2.csv --bertscore bertscore_all.csv --out final_results \
      --pass4 judgements_pass4_hinglish_v2.csv --hinglish-v2 summaries_hinglish_v2.csv

Fact support for a (condition, output language, fact) = mean over the blind judging passes
that covered it: English oracle 4 passes, English Trelis 2, everything else 1.
out_lang "hinglish" = re-generated Hinglish outputs (max_new_tokens 1024, pass 4);
"hinglish_320" = the original Hinglish outputs, cut off at 320 tokens (pass 3).
BERTScore exists only for the English and hinglish_320 summaries.
Writes (new files only):
  item_metrics.csv          one row per summary: fact recall (all/hi/mixed/en), ROUGE-1/2/L,
                            BERTScore P/R/F1 (raw) and F1 (baseline-rescaled), words, truncated flag
  condition_table.csv       mean of every metric per condition
  paired_vs_oracle.csv      window-level paired Wilcoxon vs English oracle + bootstrap CI;
                            Holm across the 12 ASR/noise conditions within each metric
  noise_slopes.csv          per-window OLS slope over noise levels 0,.1,.2,.3,.4,.5 (mean, bootstrap CI)
  metric_validity.csv       how automatic metrics track judge recall (Spearman, item and within-window)
                            and how strongly each metric detects the whisper-small drop
  judge_reliability.csv     pairwise agreement / Cohen's kappa between judging passes
  hinglish_truncation.csv   Hinglish outputs: ends cleanly? words? (max_new_tokens=320 cut-off)
"""
import argparse
import itertools
import os

import numpy as np
import pandas as pd
from rouge_score import rouge_scorer
from scipy.stats import spearmanr, wilcoxon

ap = argparse.ArgumentParser()
for a in ["root", "pass1", "pass2", "pass3", "v2", "bertscore", "out"]:
    ap.add_argument(f"--{a}", required=True)
ap.add_argument("--pass4", help="judgements of the re-generated Hinglish summaries (max_new_tokens 1024)")
ap.add_argument("--hinglish-v2", dest="hinglish_v2", help="summaries_hinglish_v2.csv")
A = ap.parse_args()
os.makedirs(A.out, exist_ok=True)
S2 = f"{A.root}/outputs/step2"
rng = np.random.default_rng(13)
NB = 2000
WINS = [f"W{i:02d}" for i in range(25)]
NOISE = [f"noise:{l}:{x}" for l in ["hi", "en"] for x in ["0.1", "0.2", "0.3", "0.4", "0.5"]]
FAMILY = ["asr:trelis-hinglish-preview", "asr:whisper-small"] + NOISE

tags = pd.read_csv(f"{S2}/silver_facts.csv")[["fact_id", "tag"]]
cols = ["window_id", "condition", "out_lang", "fact_id", "supported", "pass"]
p1 = pd.read_csv(A.pass1)
p1 = p1[p1.kind == "summary"].assign(**{"pass": 1})
p2 = pd.read_csv(A.pass2).assign(out_lang="en", **{"pass": 2})
p3 = pd.read_csv(A.pass3).assign(**{"pass": 3})
# The original Hinglish outputs were cut off at 320 tokens: keep them, but under their own label.
H320 = "hinglish_320"
p3.loc[p3.out_lang == "hinglish", "out_lang"] = H320
parts = [p1[cols], p2[cols], p3[cols]]
if A.pass4:
    p4 = pd.read_csv(A.pass4).assign(**{"pass": 4})
    parts.append(p4[cols])
J = pd.concat(parts, ignore_index=True)
J["supported"] = J.supported.astype(float)
J.to_csv(f"{A.out}/judgements_all_passes.csv", index=False)
F = J.groupby(["window_id", "condition", "out_lang", "fact_id"]).supported.mean().reset_index().merge(tags, on="fact_id")

# ---------- item metrics ----------
s = pd.read_csv(f"{S2}/summaries.csv", keep_default_na=False)[["window_id", "condition", "out_lang", "summary"]]
v2 = pd.read_csv(A.v2, keep_default_na=False)[["window_id", "condition", "summary"]].assign(out_lang="en")
s.loc[s.out_lang == "hinglish", "out_lang"] = H320
S = [s, v2]
if A.hinglish_v2:
    S.append(pd.read_csv(A.hinglish_v2, keep_default_na=False)[["window_id", "condition", "summary"]].assign(out_lang="hinglish"))
S = pd.concat(S, ignore_index=True)
ref = pd.read_csv(f"{S2}/silver_references.csv", keep_default_na=False).set_index("window_id").ref_summary
sc = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
rows = []
for r in S.itertuples():
    z = sc.score(ref[r.window_id], r.summary)
    rows.append(dict(window_id=r.window_id, condition=r.condition, out_lang=r.out_lang,
                     words=len(r.summary.split()),
                     truncated=r.summary.strip()[-1:] not in list('.।!?"\')'),
                     rouge1=z["rouge1"].fmeasure, rouge2=z["rouge2"].fmeasure, rougeL=z["rougeL"].fmeasure))
I = pd.DataFrame(rows)
bs = pd.read_csv(A.bertscore)
bs.loc[bs.out_lang == "hinglish", "out_lang"] = H320  # BERTScore was computed on the 320-token outputs
I = I.merge(bs, on=["window_id", "condition", "out_lang"], how="left")
rec = F.groupby(["window_id", "condition", "out_lang"]).supported.mean().rename("recall_all").reset_index()
for t in ["hi", "mixed", "en"]:
    rt = F[F.tag == t].groupby(["window_id", "condition", "out_lang"]).supported.mean().rename(f"recall_{t}").reset_index()
    rec = rec.merge(rt, on=["window_id", "condition", "out_lang"], how="left")
I = I.merge(rec, on=["window_id", "condition", "out_lang"], how="left")
npass = J.groupby(["window_id", "condition", "out_lang"])["pass"].nunique().rename("n_judge_passes").reset_index()
I = I.merge(npass, on=["window_id", "condition", "out_lang"], how="left")
I.to_csv(f"{A.out}/item_metrics.csv", index=False)
METRICS = ["recall_all", "recall_hi", "recall_mixed", "recall_en", "rouge1", "rouge2", "rougeL",
           "bertscore_f1", "bertscore_f1_rescaled"]
I.groupby(["out_lang", "condition"])[METRICS + ["words", "truncated", "n_judge_passes"]].mean() \
    .reset_index().to_csv(f"{A.out}/condition_table.csv", index=False)


def holm(ps):
    ps = np.asarray(ps, float)
    adj, run = np.empty_like(ps), 0.0
    for k, i in enumerate(np.argsort(ps)):
        run = max(run, (len(ps) - k) * ps[i])
        adj[i] = min(1.0, run)
    return adj


def paired(c, base, lang_c="en", lang_b="en", metric="recall_all"):
    a = I[(I.condition == c) & (I.out_lang == lang_c)].set_index("window_id")[metric]
    b = I[(I.condition == base) & (I.out_lang == lang_b)].set_index("window_id")[metric]
    d = pd.concat([a, b], axis=1, keys=["c", "b"]).dropna()
    diff = (d.c - d.b).values
    if len(diff) == 0:
        return None
    boot = [rng.choice(diff, len(diff)).mean() for _ in range(NB)]
    return dict(n_windows=len(diff), base_mean=d.b.mean(), cond_mean=d.c.mean(), diff=diff.mean(),
                ci_lo=np.percentile(boot, 2.5), ci_hi=np.percentile(boot, 97.5),
                wilcoxon_p=wilcoxon(diff).pvalue if np.any(diff != 0) else 1.0)


rows = []
for m in METRICS:
    block = [dict(family="asr_noise_vs_oracle", comparison=f"{c} vs oracle", metric=m, **paired(c, "oracle", metric=m))
             for c in FAMILY]  # English conditions always have every metric
    for b, p in zip(block, holm([b["wilcoxon_p"] for b in block])):
        b["p_holm"] = p
    rows += block
    extra = [("script_shift_v2", "oracle", "en", "en"),
             ("asr:trelis+backtranslit", "asr:trelis-hinglish-preview", "en", "en"),
             ("oracle", "oracle", "hinglish", "en"),
             ("asr:trelis-hinglish-preview", "oracle", "hinglish", "hinglish"),
             ("asr:whisper-small", "oracle", "hinglish", "hinglish"),
             ("oracle", "oracle", H320, "en")]
    for c, b, lc, lb in extra:
        if not ((I.condition == c) & (I.out_lang == lc)).any():
            continue
        res = paired(c, b, lc, lb, m)
        if res is not None:  # e.g. no BERTScore for the re-generated Hinglish outputs
            rows.append(dict(family="other", comparison=f"{c}[{lc}] vs {b}[{lb}]", metric=m, **res, p_holm=np.nan))
pd.DataFrame(rows).to_csv(f"{A.out}/paired_vs_oracle.csv", index=False)

# ---------- noise slopes ----------
rows = []
for lang in ["hi", "en"]:
    lv = {"oracle": 0.0, **{f"noise:{lang}:{x}": float(x) for x in ["0.1", "0.2", "0.3", "0.4", "0.5"]}}
    sub = I[(I.out_lang == "en") & I.condition.isin(lv)]
    for m in ["recall_all", "recall_hi", "recall_mixed", "recall_en", "rougeL", "bertscore_f1_rescaled"]:
        sl = []
        for w, g in sub.groupby("window_id"):
            g = g.dropna(subset=[m])
            if g.condition.nunique() == 6:
                sl.append(np.polyfit(g.condition.map(lv), g[m], 1)[0])
        sl = np.array(sl)
        boot = [rng.choice(sl, len(sl)).mean() for _ in range(NB)]
        rows.append(dict(sweep=lang, metric=m, n_windows=len(sl), slope_per_unit=sl.mean(),
                         ci_lo=np.percentile(boot, 2.5), ci_hi=np.percentile(boot, 97.5),
                         level_means=" ".join(f"{sub[sub.condition == c][m].mean():.3f}" for c in lv)))
pd.DataFrame(rows).to_csv(f"{A.out}/noise_slopes.csv", index=False)

# ---------- metric validity (English summaries) ----------
E = I[I.out_lang == "en"].dropna(subset=["recall_all"]).copy()
for m in ["rouge1", "rouge2", "rougeL", "bertscore_f1", "bertscore_f1_rescaled"]:
    E[m + "_dm"] = E[m] - E.groupby("window_id")[m].transform("mean")
E["recall_dm"] = E.recall_all - E.groupby("window_id").recall_all.transform("mean")
rows = []
for m in ["rouge1", "rouge2", "rougeL", "bertscore_f1", "bertscore_f1_rescaled"]:
    r_item, p_item = spearmanr(E[m], E.recall_all)
    r_w, p_w = spearmanr(E[m + "_dm"], E.recall_dm)
    d = paired("asr:whisper-small", "oracle", metric=m)
    dt = (I[(I.condition == "asr:whisper-small") & (I.out_lang == "en")].set_index("window_id")[m]
          - I[(I.condition == "oracle") & (I.out_lang == "en")].set_index("window_id")[m])
    rows.append(dict(metric=m, n_summaries=len(E), spearman_vs_recall=r_item, p=p_item,
                     spearman_within_window=r_w, p_within=p_w,
                     whisper_drop=d["diff"], whisper_drop_effect_size=dt.mean() / dt.std(ddof=1),
                     whisper_windows_lower=int((dt < 0).sum())))
dt = (I[(I.condition == "asr:whisper-small") & (I.out_lang == "en")].set_index("window_id").recall_all
      - I[(I.condition == "oracle") & (I.out_lang == "en")].set_index("window_id").recall_all)
rows.append(dict(metric="recall_all (judge)", n_summaries=len(E), whisper_drop=dt.mean(),
                 whisper_drop_effect_size=dt.mean() / dt.std(ddof=1), whisper_windows_lower=int((dt < 0).sum())))
pd.DataFrame(rows).to_csv(f"{A.out}/metric_validity.csv", index=False)

# ---------- judge reliability ----------
rows = []
for (c, l), g in J.groupby(["condition", "out_lang"]):
    ps = sorted(g["pass"].unique())
    for a_, b_ in itertools.combinations(ps, 2):
        m = g[g["pass"] == a_].merge(g[g["pass"] == b_], on="fact_id", suffixes=("_a", "_b"))
        x, y = m.supported_a.astype(bool), m.supported_b.astype(bool)
        po = (x == y).mean()
        pe = x.mean() * y.mean() + (1 - x.mean()) * (1 - y.mean())
        rows.append(dict(condition=c, out_lang=l, passes=f"{a_} vs {b_}", n=len(m), agreement=po,
                         kappa=(po - pe) / (1 - pe), recall_a=x.mean(), recall_b=y.mean()))
pd.DataFrame(rows).to_csv(f"{A.out}/judge_reliability.csv", index=False)

# ---------- Hinglish truncation ----------
I[I.out_lang.isin(["hinglish", H320])][["window_id", "condition", "out_lang", "words", "truncated", "recall_all"]] \
    .to_csv(f"{A.out}/hinglish_truncation.csv", index=False)
print("wrote", A.out)
