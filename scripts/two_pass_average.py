"""Results using the AVERAGE of the two blind judging passes for oracle and Trelis (25 windows).

Pass 1 = judgements_25w.csv; pass 2 = judgements_script_shift.csv (anchor_original rows).
Each fact gets support = mean of the passes (0, 0.5 or 1) for oracle and Trelis; every other
condition has one pass. Averaging only reduces judge noise; it does not change what is measured.

Usage: python two_pass_average.py judgements_25w.csv judgements_script_shift.csv silver_facts.csv OUTDIR
"""
import os
import sys

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

J1, J2, FACTS, OUT = sys.argv[1:5]
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(13)
NB = 2000
tags = pd.read_csv(FACTS)[["fact_id", "tag"]]
p1 = pd.read_csv(J1)
p1 = p1[p1.kind == "summary"][["window_id", "condition", "fact_id", "supported"]]
p2 = pd.read_csv(J2)
p2 = p2[p2.kind == "anchor_original"][["window_id", "condition", "fact_id", "supported"]]

avg = (pd.concat([p1[p1.condition.isin(["oracle", "asr:trelis-hinglish-preview"])], p2])
       .groupby(["window_id", "condition", "fact_id"]).supported.mean().reset_index())
single = p1[~p1.condition.isin(["oracle", "asr:trelis-hinglish-preview"])].copy()
single["supported"] = single.supported.astype(float)
allj = pd.concat([avg, single]).merge(tags, on="fact_id")
allj.to_csv(f"{OUT}/judgements_two_pass_avg.csv", index=False)

wide = allj.pivot_table(index=["window_id", "fact_id", "tag"], columns="condition",
                        values="supported").reset_index()
wins = wide.window_id.unique()
G = {w: wide[wide.window_id == w] for w in wins}
boots = [pd.concat([G[w] for w in rng.choice(wins, len(wins))]) for _ in range(NB)]
CONDS = ["asr:trelis-hinglish-preview", "asr:whisper-small", "noise:hi:0.2", "noise:hi:0.4",
         "noise:hi:0.5", "noise:en:0.2", "noise:en:0.4", "noise:en:0.5"]
rows = []
for t in ["all", "hi", "mixed", "en"]:
    block = []
    d = wide if t == "all" else wide[wide.tag == t]
    for c in CONDS:
        bs = []
        for b in boots:
            bb = b if t == "all" else b[b.tag == t]
            if len(bb):
                bs.append(bb[c].mean() - bb["oracle"].mean())
        pw = d.groupby("window_id")[["oracle", c]].mean()
        diff = pw[c] - pw["oracle"]
        block.append(dict(tag=t, condition=c, n_facts=len(d), n_windows=len(pw),
                          oracle_recall=d["oracle"].mean(), cond_recall=d[c].mean(),
                          diff=d[c].mean() - d["oracle"].mean(),
                          ci_lo=np.percentile(bs, 2.5), ci_hi=np.percentile(bs, 97.5),
                          window_wilcoxon_p=wilcoxon(diff).pvalue if (diff != 0).any() else 1.0))
    ps = np.array([b["window_wilcoxon_p"] for b in block])
    order, run, adj = np.argsort(ps), 0.0, np.empty(len(ps))
    for r, i in enumerate(order):
        run = max(run, (len(ps) - r) * ps[i])
        adj[i] = min(1.0, run)
    for b, a in zip(block, adj):
        b["p_holm"] = a
    rows += block
res = pd.DataFrame(rows)
res.to_csv(f"{OUT}/results_two_pass_avg.csv", index=False)
pd.set_option("display.width", 250)
print(res.round(3).to_string())
