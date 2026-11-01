"""Re-run the Step-2 analyses on all 25 windows (W00-W24). Read-only on inputs; new files only.

Usage:
    python analysis_25w.py  path/to/hinglish_asr_sum  path/to/judgements_25w.csv  OUTDIR

Outputs (OUTDIR):
  summary_metrics_per_item_25w.csv   ROUGE (rouge-score 0.1.2, stemmer; reproduces the original
                                     values exactly) + fact recall by language, per summary
  paired_vs_oracle_25w.csv           window-level paired Wilcoxon vs oracle, Holm across the 8
                                     judged conditions within each metric x subset; bootstrap CI
  factlevel_recall_by_language_25w.csv   fact-level recall, window-cluster bootstrap CI of the diff
  conditional_retention_25w.csv      retention of oracle-supported facts / gain of missed facts
  sweep_slopes_25w.csv               per-window OLS slope of the metric on injected noise rate
                                     (levels 0=oracle, .2, .4, .5), mean over windows, bootstrap CI
  whisper_small_repetition_sensitivity_25w.csv
  judge_ceiling_25w.csv
Subsets: all_windows (25), excl_W07_W24 (SENSITIVITY_EXCLUDE from run_config_step2.json).
"""
import sys

import numpy as np
import pandas as pd
from rouge_score import rouge_scorer
from scipy.stats import wilcoxon

ROOT, JUDG, OUT = sys.argv[1:4]
import os
os.makedirs(OUT, exist_ok=True)
S2 = f"{ROOT}/outputs/step2"
N_BOOT, SEED = 2000, 13
rng = np.random.default_rng(SEED)
CONDS = ["asr:trelis-hinglish-preview", "asr:whisper-small", "noise:hi:0.2", "noise:hi:0.4",
         "noise:hi:0.5", "noise:en:0.2", "noise:en:0.4", "noise:en:0.5"]
EXCL = ["W07", "W24"]

facts = pd.read_csv(f"{S2}/silver_facts.csv")[["fact_id", "tag"]]
j = pd.read_csv(JUDG).merge(facts, on="fact_id")
js = j[j.kind == "summary"]
summ = pd.read_csv(f"{S2}/summaries.csv")
summ = summ[(summ.out_lang == "en") & summ.condition.isin(["oracle"] + CONDS)]
ref = pd.read_csv(f"{S2}/silver_references.csv").set_index("window_id").ref_summary

# ---------- per-item metrics ----------
sc = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
rows = []
for r in summ.itertuples():
    s = sc.score(ref[r.window_id], r.summary)
    d = js[(js.window_id == r.window_id) & (js.condition == r.condition)]
    row = dict(window_id=r.window_id, condition=r.condition, summary_words=len(r.summary.split()),
               rouge1=s["rouge1"].fmeasure, rouge2=s["rouge2"].fmeasure, rougeL=s["rougeL"].fmeasure,
               recall_all=d.supported.mean())
    for t in ["hi", "mixed", "en"]:
        dt = d[d.tag == t]
        row[f"recall_{t}"] = dt.supported.mean() if len(dt) else np.nan
        row[f"n_facts_{t}"] = len(dt)
    row["csl_gap"] = row["recall_en"] - row["recall_hi"]
    rows.append(row)
item = pd.DataFrame(rows)
item.to_csv(f"{OUT}/summary_metrics_per_item_25w.csv", index=False)


def holm(ps):
    ps = np.asarray(ps, float)
    order = np.argsort(ps)
    adj = np.empty_like(ps)
    run = 0.0
    for rank, i in enumerate(order):
        run = max(run, (len(ps) - rank) * ps[i])
        adj[i] = min(1.0, run)
    return adj


# ---------- paired vs oracle ----------
METRICS = ["recall_all", "recall_hi", "recall_mixed", "recall_en", "csl_gap", "rouge1", "rouge2", "rougeL"]
res = []
for subset, wins in [("all_windows", None), ("excl_W07_W24", EXCL)]:
    it = item if wins is None else item[~item.window_id.isin(wins)]
    for metric in METRICS:
        block = []
        for c in CONDS:
            pv = it.pivot_table(index="window_id", columns="condition", values=metric)[["oracle", c]].dropna()
            d = (pv[c] - pv["oracle"]).values
            p = wilcoxon(d).pvalue if np.any(d != 0) else 1.0
            bs = [rng.choice(d, len(d)).mean() for _ in range(N_BOOT)]
            block.append(dict(subset=subset, condition=c, metric=metric, n_windows=len(d),
                              oracle_mean=pv["oracle"].mean(), cond_mean=pv[c].mean(), diff=d.mean(),
                              ci95_lo=np.percentile(bs, 2.5), ci95_hi=np.percentile(bs, 97.5),
                              wilcoxon_p=p, windows_cond_worse=int((d < 0).sum())))
        for b, ph in zip(block, holm([b["wilcoxon_p"] for b in block])):
            b["p_holm"] = ph
        res += block
paired = pd.DataFrame(res)
paired.to_csv(f"{OUT}/paired_vs_oracle_25w.csv", index=False)

# ---------- fact-level by language, window-cluster bootstrap ----------
wide = js.pivot_table(index=["window_id", "fact_id", "tag"], columns="condition",
                      values="supported").astype(float).reset_index()
wins_all = wide.window_id.unique()
groups = {w: wide[wide.window_id == w] for w in wins_all}
boot_sets = [pd.concat([groups[w] for w in rng.choice(wins_all, len(wins_all))]) for _ in range(N_BOOT)]
rows = []
for c in ["oracle"] + CONDS:
    for t in ["all", "hi", "mixed", "en"]:
        d = wide if t == "all" else wide[wide.tag == t]
        row = dict(condition=c, tag=t, n_decisions=len(d), recall=d[c].mean())
        if c != "oracle":
            row["diff_vs_oracle"] = d[c].mean() - d["oracle"].mean()
            bs = []
            for b in boot_sets:
                bb = b if t == "all" else b[b.tag == t]
                if len(bb):
                    bs.append(bb[c].mean() - bb["oracle"].mean())
            row["ci_lo"], row["ci_hi"] = np.percentile(bs, [2.5, 97.5])
        rows.append(row)
pd.DataFrame(rows).to_csv(f"{OUT}/factlevel_recall_by_language_25w.csv", index=False)

# ---------- conditional retention ----------
rows = []
for c in CONDS:
    for t in ["all", "hi", "mixed", "en"]:
        d = wide if t == "all" else wide[wide.tag == t]
        k, g = d[d.oracle == 1], d[d.oracle == 0]
        row = dict(condition=c, tag=t, n_oracle_supported=len(k), retained=int(k[c].sum()),
                   retention=k[c].mean(), n_oracle_missed=len(g), gained=int(g[c].sum()),
                   gain_rate=g[c].mean())
        bs = []
        for b in boot_sets:
            bb = b if t == "all" else b[b.tag == t]
            kk = bb[bb.oracle == 1]
            if len(kk):
                bs.append(kk[c].mean())
        row["ret_ci_lo"], row["ret_ci_hi"] = np.percentile(bs, [2.5, 97.5])
        rows.append(row)
pd.DataFrame(rows).to_csv(f"{OUT}/conditional_retention_25w.csv", index=False)

# ---------- noise sweep slopes ----------
rows = []
for subset, wins in [("all_windows", None), ("excl_W07_W24", EXCL)]:
    it = item if wins is None else item[~item.window_id.isin(wins)]
    for lang in ["hi", "en"]:
        conds = {"oracle": 0.0, f"noise:{lang}:0.2": 0.2, f"noise:{lang}:0.4": 0.4, f"noise:{lang}:0.5": 0.5}
        for metric in ["recall_all", "recall_hi", "recall_en", "rougeL"]:
            slopes = []
            for w, g in it[it.condition.isin(conds)].groupby("window_id"):
                g = g.dropna(subset=[metric])
                if g.condition.nunique() == 4:
                    slopes.append(np.polyfit(g.condition.map(conds), g[metric], 1)[0])
            slopes = np.array(slopes)
            bs = [rng.choice(slopes, len(slopes)).mean() for _ in range(N_BOOT)]
            rows.append(dict(subset=subset, sweep=lang, metric=metric, x="injected_rate",
                             slope_per_unit=slopes.mean(), ci95_lo=np.percentile(bs, 2.5),
                             ci95_hi=np.percentile(bs, 97.5), n_windows=len(slopes)))
pd.DataFrame(rows).to_csv(f"{OUT}/sweep_slopes_25w.csv", index=False)

# ---------- whisper-small repetition sensitivity ----------
pw = pd.read_csv(f"{ROOT}/outputs/asr_metrics_per_window_vad15.csv")
rep = set(pw[(pw.model == "whisper-small") & pw.flag_repetition].window_id)
o = item[item.condition == "oracle"].set_index("window_id")
ws = item[item.condition == "asr:whisper-small"].set_index("window_id")
rows = []
for name, keep in [("all_25", list(o.index)), ("no_repetition_flag", [x for x in o.index if x not in rep])]:
    d = ws.loc[keep, "recall_all"] - o.loc[keep, "recall_all"]
    rows.append(dict(subset=name, n_windows=len(keep), recall_diff=d.mean(), wilcoxon_p=wilcoxon(d).pvalue,
                     rougeL_diff=(ws.loc[keep, "rougeL"] - o.loc[keep, "rougeL"]).mean()))
pd.DataFrame(rows).to_csv(f"{OUT}/whisper_small_repetition_sensitivity_25w.csv", index=False)

# ---------- judge ceiling ----------
jr = j[j.kind == "reference_sanity"]
pd.DataFrame([dict(scope=s, n_decisions=len(d), ceiling=d.supported.mean())
              for s, d in [("W00-W15", jr[jr.window_id < "W16"]), ("W16-W24", jr[jr.window_id >= "W16"]),
                           ("all_25", jr)]]).to_csv(f"{OUT}/judge_ceiling_25w.csv", index=False)
print("wrote", OUT)
