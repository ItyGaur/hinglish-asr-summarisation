"""What happens to English (Latin-script) reference words in each ASR hypothesis?

Run from the hinglish_asr_sum/ folder:
    python en_word_fate.py
Reads only existing outputs (never modifies them). Writes:
    outputs/analysis/en_word_fate_per_window.csv
    outputs/analysis/en_word_fate_summary.csv

Categories for each English reference word (difflib word alignment of
ref_norm vs hyp_norm):
  correct           - same Latin token in hypothesis
  dev_exact         - replaced by Devanagari, and the hypothesis segment contains
                      the script_shift_lexicon spelling of that word (a re-scripting,
                      not a mishearing). Lower bound: spelling variants are not counted.
  dev_other_in_lex  - replaced by Devanagari, word is in the lexicon, spelling differs
  dev_not_in_lex    - replaced by Devanagari, word not in the lexicon (uncheckable)
  sub_latin         - replaced by a different Latin token
  deleted           - deleted
Note: difflib alignment is not identical to jiwer's, so totals differ slightly
from en_token_err in asr_metrics_per_window_vad15.csv.
"""
import collections
import difflib
import os
import re

import pandas as pd

OUT = "outputs/analysis"
os.makedirs(OUT, exist_ok=True)

lex = dict(pd.read_csv("outputs/step2/script_shift_lexicon.csv").values)
sw = pd.read_csv("outputs/selected_windows.csv").set_index("window_id")
pw = pd.read_csv("outputs/asr_metrics_per_window_vad15.csv")

LAT = re.compile(r"^[a-z0-9']+$")
DEV = re.compile(r"[ऀ-ॿ]")
NUKTA = "़"
norm = lambda s: str(s).replace(NUKTA, "")
CATS = ["correct", "dev_exact", "dev_other_in_lex", "dev_not_in_lex", "sub_latin", "deleted"]

rows = []
for _, r in pw.iterrows():
    ref = str(sw.loc[r.window_id, "ref_norm"]).split()
    hyp = str(r.hyp_norm).split()
    c = collections.Counter()
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ref, hyp, autojunk=False).get_opcodes():
        seg = [norm(x) for x in hyp[j1:j2]]
        has_dev = any(DEV.search(x) for x in seg)
        for k in range(i1, i2):
            w = ref[k]
            if not LAT.match(w):
                continue
            if op == "equal":
                c["correct"] += 1
            elif op == "delete":
                c["deleted"] += 1
            elif has_dev:
                if w in lex:
                    c["dev_exact" if norm(lex[w]) in seg else "dev_other_in_lex"] += 1
                else:
                    c["dev_not_in_lex"] += 1
            else:
                c["sub_latin"] += 1
    rows.append({"window_id": r.window_id, "model": r.model, **{k: c[k] for k in CATS},
                 "n_en_ref": sum(c.values()), "en_token_err_jiwer": r.en_token_err,
                 "hi_token_err_jiwer": r.hi_token_err, "flag_repetition": r.flag_repetition})

per = pd.DataFrame(rows)
per.to_csv(f"{OUT}/en_word_fate_per_window.csv", index=False)


def summarise(df, label):
    t = df[CATS].sum()
    n = t.sum()
    checkable = t.dev_exact + t.dev_other_in_lex
    exact_share = t.dev_exact / checkable if checkable else float("nan")
    # error rate if exact re-scriptings were counted as correct (lower-bound fix)
    err_rescript_ok = 1 - (t.correct + t.dev_exact) / n
    # extrapolated: apply the exact share to uncheckable Devanagari subs too (ESTIMATE)
    est_ok = t.correct + t.dev_exact + exact_share * t.dev_not_in_lex
    return {"model": label, "n_en_ref_words": int(n), **{f"share_{k}": t[k] / n for k in CATS},
            "dev_exact_share_of_checkable": exact_share,
            "en_err_raw_difflib": 1 - t.correct / n,
            "en_err_if_exact_rescript_counted_correct": err_rescript_ok,
            "en_err_extrapolated_ESTIMATE": 1 - est_ok / n}


out = []
for scope, wins in [("all25", None), ("W00-W15", [f"W{i:02d}" for i in range(16)])]:
    for m, g in per.groupby("model"):
        if wins:
            g = g[g.window_id.isin(wins)]
        out.append({"scope": scope, **summarise(g, m)})
summ = pd.DataFrame(out)
summ.to_csv(f"{OUT}/en_word_fate_summary.csv", index=False)
pd.set_option("display.width", 200)
print(summ.T.to_string())
