"""Build two new input conditions (all 25 windows) for the script-shift experiment (no GPU, no API).

Usage, from inside hinglish_asr_sum/:
    python build_script_shift_v2.py

Reads only existing files. Writes:
  outputs/step2/lexicon_v2.csv          word, devanagari, source
  outputs/step2/conditions_v2.csv       same columns as conditions.csv (subset) for:
      script_shift_v2         oracle transcript with every English (Latin) token replaced
                              by its Devanagari spelling (lexicon_v2); uncovered words stay Latin
      asr:trelis+backtranslit Trelis transcript with Devanagari-spelled English words mapped
                              back to Latin. Uses a LEAVE-ONE-WINDOW-OUT lexicon (pairs harvested
                              from the other 24 windows only) plus the original Gemini lexicon.
  outputs/step2/conditions_v2_coverage.csv

Lexicon sources, in priority order:
  1. gemini   - the original script_shift_lexicon.csv (450 words)
  2. trelis   - 1:1 aligned substitutions (Latin ref word -> single Devanagari hyp word)
                harvested from Trelis output over all 25 windows; majority spelling, count >= 2
Back-transliteration safety: a Devanagari form F (for English word E) is only mapped back
if, in the OTHER windows' oracle transcripts, F occurs less often as a Devanagari token than
E occurs as a Latin token. This blocks ordinary Hindi words that collide with English
spellings (इस 'is', इन 'in', ए 'a') while keeping English words the oracle sometimes writes
in Devanagari.
"""
import collections
import difflib
import re

import pandas as pd

S2 = "outputs/step2"
sw = pd.read_csv("outputs/selected_windows.csv").set_index("window_id")
pw = pd.read_csv("outputs/asr_metrics_per_window_vad15.csv")
_g = pd.read_csv(f"{S2}/script_shift_lexicon.csv", keep_default_na=False, dtype=str)
gem = {w: d for w, d in _g.values if w and d}
cond = pd.read_csv(f"{S2}/conditions.csv")
WINDOWS = list(sw.index)

LAT = re.compile(r"^[a-z0-9']+$")
DEV = re.compile(r"^[ऀ-ॿ]+$")
NUKTA = "़"
nk = lambda s: s.replace(NUKTA, "")


def harvest(windows, model="trelis-hinglish-preview"):
    """Counter[(latin_word, devanagari_word)] from 1:1 replace ops."""
    c = collections.Counter()
    for w in windows:
        ref = sw.loc[w, "ref_norm"].split()
        hyp = str(pw[(pw.window_id == w) & (pw.model == model)].hyp_norm.iloc[0]).split()
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ref, hyp, autojunk=False).get_opcodes():
            if op == "replace" and (i2 - i1) == (j2 - j1):
                for a, b in zip(ref[i1:i2], hyp[j1:j2]):
                    if LAT.match(a) and DEV.match(b):
                        c[(a, b)] += 1
    return c


def majority(counter, min_count=2):
    best = {}
    by_word = collections.defaultdict(list)
    for (a, b), n in counter.items():
        by_word[a].append((n, b))
    for a, lst in by_word.items():
        n, b = max(lst)
        if n >= min_count:
            best[a] = b
    return best


# ---------- lexicon_v2 (all windows; used for script_shift_v2) ----------
tre_all = majority(harvest(WINDOWS))
lex = {w: (d, "gemini") for w, d in gem.items()}
for w, d in tre_all.items():
    lex.setdefault(w, (d, "trelis"))
pd.DataFrame([(w, d, s) for w, (d, s) in sorted(lex.items())],
             columns=["word", "devanagari", "source"]).to_csv(f"{S2}/lexicon_v2.csv", index=False)

# token counts in each window's oracle (for the leave-one-window-out safety check)
tok_counts = {w: collections.Counter(nk(t) for t in sw.loc[w, "ref_norm"].split()) for w in WINDOWS}

rows, cov = [], []
for w in WINDOWS:
    ref = sw.loc[w, "ref_norm"].split()
    # --- script_shift_v2 ---
    out, n_en, n_cov, src = [], 0, 0, collections.Counter()
    for t in ref:
        if LAT.match(t):
            n_en += 1
            if t in lex:
                out.append(lex[t][0]); n_cov += 1; src[lex[t][1]] += 1
            else:
                out.append(t)
        else:
            out.append(t)
    rows.append(dict(window_id=w, condition="script_shift_v2", family="script_shift",
                     text=" ".join(out), n_words=len(out)))
    cov.append(dict(window_id=w, condition="script_shift_v2", n_en_tokens=n_en,
                    n_converted=n_cov, coverage=n_cov / max(1, n_en),
                    from_gemini=src["gemini"], from_trelis=src["trelis"]))

    # --- asr:trelis+backtranslit (leave-one-window-out lexicon) ---
    lowo = majority(harvest([x for x in WINDOWS if x != w]))
    lex_w = dict(gem)
    for a, b in lowo.items():
        lex_w.setdefault(a, b)
    rev = collections.defaultdict(collections.Counter)
    for a, b in lex_w.items():
        rev[nk(b)][a] += 1
    other = collections.Counter()
    for x in WINDOWS:
        if x != w:
            other.update(tok_counts[x])
    rev = {d: c.most_common(1)[0][0] for d, c in rev.items()}
    rev = {d: e for d, e in rev.items() if other[d] < other[e]}
    hyp = str(pw[(pw.window_id == w) & (pw.model == "trelis-hinglish-preview")].hyp_norm.iloc[0]).split()
    out, n_dev, n_back = [], 0, 0
    for t in hyp:
        if DEV.match(t):
            n_dev += 1
            if nk(t) in rev:
                out.append(rev[nk(t)]); n_back += 1
                continue
        out.append(t)
    rows.append(dict(window_id=w, condition="asr:trelis+backtranslit", family="script_fix",
                     text=" ".join(out), n_words=len(out)))
    cov.append(dict(window_id=w, condition="asr:trelis+backtranslit", n_dev_tokens=n_dev,
                    n_converted=n_back, coverage=n_back / max(1, n_dev)))

# sanity: Trelis text used here must equal the text used in the original run
orig = cond[cond.condition == "asr:trelis-hinglish-preview"].set_index("window_id").text
for w in WINDOWS:
    hyp = str(pw[(pw.window_id == w) & (pw.model == "trelis-hinglish-preview")].hyp_norm.iloc[0])
    assert " ".join(hyp.split()) == " ".join(str(orig[w]).split()), f"Trelis text mismatch {w}"

pd.DataFrame(rows).to_csv(f"{S2}/conditions_v2.csv", index=False)
cv = pd.DataFrame(cov)
cv.to_csv(f"{S2}/conditions_v2_coverage.csv", index=False)
print("lexicon_v2:", pd.Series([s for _, s in lex.values()]).value_counts().to_dict())
for c, g in cv.groupby("condition"):
    print(c, "converted", int(g.n_converted.sum()), "| mean per-window coverage %.2f" % g.coverage.mean())
old = cond[cond.condition == "script_shift"]
print("old script_shift rows:", len(old))
