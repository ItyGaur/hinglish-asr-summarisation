"""Rule-based cleaning of OCR screen text (frozen rules; no LLM, deterministic).

Input : outputs/video/ocr_lines.csv   (window_id, t, text, conf)  - raw Tesseract lines
Output: outputs/video/screen_text_clean.csv   (window_id, n_lines, screen_text, chars)
        outputs/video/conditions_video_clean.csv (same 4 conditions as the raw run, *_clean names)
        outputs/video/clean_line_log.csv  (every raw line with keep/drop and the reason - for the paper)

    python clean_screen.py --root /content/drive/MyDrive/hinglish_asr_sum

Rules, applied in this order to each OCR line:
  1. strip bullet / OCR-symbol prefixes (», >, e, @, ®, ©, •, -, *, =)
  2. DROP credits/boilerplate: project credits, URLs, funding lines, workshop/certificate text
  3. DROP status bars / window chrome: '|', Ln/Col counters, Page n/m, Slide n/m, clock times,
     INSRT/STD, Tab Width, recorder user names
  4. DROP menu bars: >= 60% of the words are standard menu words (File, Edit, View, ...)
  5. KEEP code / commands / program output: line has code characters or tokens (; ( ) # $ ./ % == gcc printf ...)
  6. otherwise KEEP only sentence-like text: >= 4 words and >= 75% of alphabetic words are real English
     words (wordfreq zipf >= 2.0) - this removes garbled fragments and single menu items
  7. merge consecutive kept lines with the same timestamp when the first does not end a sentence and
     the next starts in lower case (re-joins slide bullets split by OCR)
  8. DROP near-duplicates: a line whose word set is >= 80% covered by an earlier kept line
  9. cap at 2000 characters, cut at a line boundary (time order kept, like the raw condition)
"""
import argparse
import os
import re

import pandas as pd
from wordfreq import zipf_frequency

CAP = 2000
BULLET = re.compile(r"^[\s»>«@®©•*=+\-–—~|e]{1,4}\s+(?=\S)|^[»>«@®©•]+")
CREDITS = re.compile(r"national mission|\bict\b|sakshat|talk to a teacher|desicrew|spoken[ -]?tutorial|script and "
                     r"narration|contributed by|it for change|https?:|www\.|\.org\b|\.ac\.in|mhrd|workshop|certificate|"
                     r"acknowledg|government of india|iit bombay|nmeict|what_is_a|bandwidth|online test|"
                     r"write to contact|pvt\.? ?ltd", re.I)
STATUS = re.compile(r"\||\bln\s*\d|\bcol\s*\d|page\s*\d+\s*/\s*\d+|slide\s*\d+\s*/\s*\d+|\d{1,2}:\d{2}\s*[ap]m|"
                    r"\binsrt\b|\bstd\b|tab width|\bins\b$|ttt@ttt|recordmydesktop|applications places", re.I)
MENU = set("file edit view insert format tools table window help slide show search documents go message "
           "applications places system bookmarks history project run terminal".split())
CODE = re.compile(r"[;{}#$]|\(\s*\)|\w\(|\./\w|%[ds]|==|\bgcc\b|\bprintf\b|\bscanf\b|\bint\b|\bchar\b|"
                  r"\bvoid\b|\breturn\b|\.c\b|\.h\b|->|\bargc\b|\bargv\b")
WORD = re.compile(r"[A-Za-z][A-Za-z'\-]*")


def is_word(w):
    return zipf_frequency(w.lower().strip("'-"), "en") >= 2.0


def classify(text):
    t = BULLET.sub("", text).strip()
    words = WORD.findall(t)
    if not t:
        return t, "drop:empty"
    if CREDITS.search(t):
        return t, "drop:credits"
    if STATUS.search(t):
        return t, "drop:status_bar"
    if words and sum(w.lower() in MENU for w in words) / len(words) >= 0.6:
        return t, "drop:menu_bar"
    if CODE.search(t) and len(t) >= 6:
        return t, "keep:code"
    if len(words) >= 4 and sum(is_word(w) for w in words) / len(words) >= 0.75:
        return t, "keep:sentence"
    return t, "drop:fragment"


def clean_window(g):
    """g: DataFrame of one window's raw lines with columns t, text (any order). Returns (text, log rows)."""
    log, kept = [], []
    for t, raw in zip(g.t, g.text):
        txt, why = classify(str(raw))
        log.append(dict(t=t, raw=raw, cleaned=txt, decision=why))
        if why.startswith("keep"):
            kept.append([t, txt])
    merged = []                                                     # rule 7
    for t, txt in kept:
        if merged and merged[-1][0] == t and not re.search(r"[.!?:;]$", merged[-1][1]) and txt[:1].islower():
            merged[-1][1] += " " + txt
        else:
            merged.append([t, txt])
    final, seen = [], []                                            # rule 8
    for t, txt in merged:
        ws = {w.lower() for w in WORD.findall(txt)}
        if ws and any(len(ws & s) / len(ws) >= 0.8 for s in seen):
            continue
        seen.append(ws)
        final.append(f"[{int(t // 60):02d}:{int(t % 60):02d}] {txt}")
    out = "\n".join(final)
    if len(out) > CAP:                                              # rule 9
        out = out[:CAP].rsplit("\n", 1)[0]
    return out, len(final), log


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    A = ap.parse_args()
    OUT = f"{A.root}/outputs/video"
    ocr = pd.read_csv(f"{OUT}/ocr_lines.csv", keep_default_na=False)
    ocr["t"] = ocr.t.astype(float)
    cond = pd.read_csv(f"{A.root}/outputs/step2/conditions.csv", keep_default_na=False)
    wins = sorted(pd.read_csv(f"{OUT}/alignment.csv").window_id)
    st, rows, logs = [], [], []
    for w in wins:
        g = ocr[ocr.window_id == w].sort_values("t", kind="stable")
        text, n, log = clean_window(g)
        logs += [dict(window_id=w, **r) for r in log]
        st.append(dict(window_id=w, n_lines=n, screen_text=text, chars=len(text)))
        for c in ["oracle", "asr:trelis-hinglish-preview", "asr:whisper-small"]:
            tr = cond[(cond.window_id == w) & (cond.condition == c)].text.iloc[0]
            rows.append(dict(window_id=w, condition=f"{c}+screen_clean", transcript=tr, screen_text=text))
        rows.append(dict(window_id=w, condition="screen_clean_only", transcript="", screen_text=text))
    pd.DataFrame(st).to_csv(f"{OUT}/screen_text_clean.csv", index=False)
    pd.DataFrame(rows).to_csv(f"{OUT}/conditions_video_clean.csv", index=False)
    lg = pd.DataFrame(logs)
    lg.to_csv(f"{OUT}/clean_line_log.csv", index=False)
    print(lg.decision.value_counts().to_string())
    print(pd.DataFrame(st)[["window_id", "n_lines", "chars"]].to_string(index=False))
