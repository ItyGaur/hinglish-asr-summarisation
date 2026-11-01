"""Score the script-shift judging. Usage:
  python analyse_script_shift.py RESPONSES.txt MAPPING.json silver_facts.csv judgements_25w.csv OUTDIR
Writes judgements_script_shift.csv and result CSVs (new files only)."""
import sys, re, json, os
import numpy as np, pandas as pd
from scipy.stats import wilcoxon
resp, mapf, factf, j25f, OUT = sys.argv[1:6]; os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(13); NB = 2000
got = dict(re.findall(r"(S-W\d\d-\d)\s*:\s*([01]+)", open(resp).read()))
M = json.load(open(mapf))["mapping"]
facts = pd.read_csv(factf); facts = facts[facts.located].sort_values("fact_id")
assert set(got) == set(M), (set(M) - set(got), set(got) - set(M))
rows = []
for bid, m in M.items():
    fids = list(facts[facts.window_id == m["window_id"]].fact_id)
    assert len(got[bid]) == len(fids), (bid, len(got[bid]), len(fids))
    rows += [dict(bid=bid, **m, fact_id=f, supported=b == "1") for f, b in zip(fids, got[bid])]
j = pd.DataFrame(rows).merge(facts[["fact_id", "tag"]], on="fact_id")
j.to_csv(f"{OUT}/judgements_script_shift.csv", index=False)

# 1. test-retest
j25 = pd.read_csv(j25f); j25 = j25[j25.kind == "summary"][["condition", "fact_id", "supported"]]
a = j[j.kind == "anchor_original"].merge(j25, on=["condition", "fact_id"], suffixes=("_now", "_orig"))
rt = []
for name, d in [("both", a)] + list(a.groupby("condition")):
    x, y = d.supported_now.astype(bool), d.supported_orig.astype(bool)
    po = (x == y).mean(); pe = x.mean()*y.mean() + (1-x.mean())*(1-y.mean())
    rt.append(dict(anchor=name, n=len(d), agreement=po, kappa=(po-pe)/(1-pe), recall_now=x.mean(), recall_orig=y.mean()))
pd.DataFrame(rt).to_csv(f"{OUT}/judge_test_retest.csv", index=False)

# 2. recall by tag (this session)
wide = j.pivot_table(index=["window_id", "fact_id", "tag"], columns="condition", values="supported").astype(float).reset_index()
wins = wide.window_id.unique(); G = {w: wide[wide.window_id == w] for w in wins}
boots = [pd.concat([G[w] for w in rng.choice(wins, len(wins))]) for _ in range(NB)]
PAIRS = [("script_shift_v2", "oracle"), ("asr:trelis+backtranslit", "asr:trelis-hinglish-preview"),
         ("asr:trelis-hinglish-preview", "oracle"), ("asr:trelis+backtranslit", "oracle")]
rows = []
for c, base in PAIRS:
    for t in ["all", "hi", "mixed", "en"]:
        d = wide if t == "all" else wide[wide.tag == t]
        bs = [(bb[c].mean() - bb[base].mean()) for b in boots for bb in [b if t == "all" else b[b.tag == t]] if len(bb)]
        # window-level paired test
        pw = d.groupby("window_id")[[c, base]].mean().dropna(); diff = pw[c] - pw[base]
        p = wilcoxon(diff).pvalue if (diff != 0).any() else 1.0
        k = d[d[base] == 1]
        rows.append(dict(comparison=f"{c} vs {base}", tag=t, n_facts=len(d), base_recall=d[base].mean(),
                         cond_recall=d[c].mean(), diff=d[c].mean() - d[base].mean(),
                         ci_lo=np.percentile(bs, 2.5), ci_hi=np.percentile(bs, 97.5),
                         n_windows=len(pw), window_wilcoxon_p=p,
                         retained_of_base=f"{int(k[c].sum())}/{len(k)}"))
res = pd.DataFrame(rows)
for t in res.tag.unique():  # Holm across the 4 comparisons within each tag
    idx = res[res.tag == t].index; ps = res.loc[idx, "window_wilcoxon_p"].values
    order = np.argsort(ps); adj = np.empty_like(ps); run = 0
    for r, i in enumerate(order):
        run = max(run, (len(ps)-r)*ps[i]); adj[i] = min(1, run)
    res.loc[idx, "p_holm"] = adj
res.to_csv(f"{OUT}/script_shift_results.csv", index=False)
pd.set_option("display.width", 250)
print(pd.DataFrame(rt).round(3).to_string()); print(res.round(3).to_string())
