"""After you fill spotcheck_judge.csv (column human_supported_y_n = y/n for each row), run:
    python compute_spotcheck_agreement.py
It merges the hidden judge decisions and prints agreement + Cohen's kappa. It also writes
spotcheck_judge_filled.csv in the format the notebook's Stage 9 expects."""
import pandas as pd, numpy as np
h = pd.read_csv("spotcheck_judge.csv", keep_default_na=False)
k = pd.read_csv("spotcheck_judge_KEY_do_not_open_before_filling.csv")
d = h.merge(k, on=["item", "window_id"])
yn = lambda s: True if str(s).strip().lower() in ("y", "yes", "1", "true") else (False if str(s).strip().lower() in ("n", "no", "0", "false") else np.nan)
d["human"] = d.human_supported_y_n.map(yn)
ok = d.human.notna(); hh = d.human[ok].astype(bool); jj = d.judge_supported[ok].astype(bool)
a = (hh == jj).mean(); pe = hh.mean() * jj.mean() + (1 - hh.mean()) * (1 - jj.mean())
print(f"n={ok.sum()}  agreement={a:.1%}  Cohen's kappa={(a - pe) / (1 - pe):.2f}")
print("judge said yes / human said no:", int((jj & ~hh).sum()), "| judge said no / human said yes:", int((~jj & hh).sum()))
d.rename(columns={"fact_id": "fact_id"}).to_csv("spotcheck_judge_filled.csv", index=False)
