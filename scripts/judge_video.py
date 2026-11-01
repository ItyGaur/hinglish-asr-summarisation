"""Blind judging packets for the video (screen-text) conditions, and scoring of the judge's answers.

Step A - packets (after summaries_video.csv exists):
    python judge_video.py packets --root hinglish_asr_sum --res video_results [--windows W00,W02,...]
  -> video_results/judge_packets_video[_<tag>].md   paste the instructions block once, then ONE window at a time
  -> video_results/judge_mapping_video_HIDDEN.json  (never show to the judge; merged across runs)

  Each window gets 7 summaries, shuffled with a per-window seed (so a window's packet never changes):
    oracle+screen, asr:trelis-hinglish-preview+screen, asr:whisper-small+screen, screen_only   (new, video)
    oracle, asr:trelis-hinglish-preview, asr:whisper-small    (ORIGINAL Step-2 English summaries = same-session
                                                               anchors; also give judge test-retest vs passes 1-4)

Step B - paste every reply line ("VD-W00-a: 1011001110") into video_results/judge_video_responses.txt
    python judge_video.py score --root hinglish_asr_sum --res video_results --passes judgements_all_passes.csv
  -> judgements_video.csv, video_paired.csv, video_gain_loss.csv, video_recall_table.csv, fact_screen_overlap.csv, printed summary
"""
import argparse
import json
import os
import random
import re

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

ap = argparse.ArgumentParser()
ap.add_argument("cmd", choices=["packets", "score"])
ap.add_argument("--root", required=True)
ap.add_argument("--res", required=True)
ap.add_argument("--video", help="summaries_video.csv (default: <root>/outputs/video/summaries_video.csv)")
ap.add_argument("--windows", help="comma list; default all 25")
ap.add_argument("--tag", default="", help="suffix for the packet file name")
ap.add_argument("--screen", help="screen_text.csv (default: <root>/outputs/video/screen_text.csv)")
ap.add_argument("--set", choices=["raw", "clean"], default="raw")
ap.add_argument("--raw-video", help="clean set only: the raw summaries_video.csv (for the raw-screen anchors)")
ap.add_argument("--passes", help="judgements_all_passes.csv from final_analysis.py (for test-retest)")
a = ap.parse_args()
S2 = f"{a.root}/outputs/step2"
os.makedirs(a.res, exist_ok=True)
SFX = "" if a.set == "raw" else "_clean"
PFX = "VD" if a.set == "raw" else "VC"
MAPF = f"{a.res}/judge_mapping_video{SFX}_HIDDEN.json"
facts = pd.read_csv(f"{S2}/silver_facts.csv", keep_default_na=False)
facts = facts[facts.located.astype(str) == "True"].sort_values("fact_id")
WINS = sorted(facts.window_id.unique())
VIDEO = ["oracle+screen", "asr:trelis-hinglish-preview+screen", "asr:whisper-small+screen", "screen_only"]
ANCH = ["oracle", "asr:trelis-hinglish-preview", "asr:whisper-small"]
PAIRS = [("oracle+screen", "oracle"), ("asr:trelis-hinglish-preview+screen", "asr:trelis-hinglish-preview"),
         ("asr:whisper-small+screen", "asr:whisper-small"), ("screen_only", "oracle")]
RAW_ANCH = []
if a.set == "clean":
    # 8 per window: 4 clean + original oracle / whisper-small + raw-OCR oracle / whisper-small (all same session)
    VIDEO = ["oracle+screen_clean", "asr:trelis-hinglish-preview+screen_clean", "asr:whisper-small+screen_clean",
             "screen_clean_only"]
    ANCH = ["oracle", "asr:whisper-small"]
    RAW_ANCH = ["oracle+screen", "asr:whisper-small+screen"]
    PAIRS = [("oracle+screen_clean", "oracle"), ("oracle+screen_clean", "oracle+screen"), ("oracle+screen", "oracle"),
             ("asr:whisper-small+screen_clean", "asr:whisper-small"),
             ("asr:whisper-small+screen_clean", "asr:whisper-small+screen"),
             ("asr:whisper-small+screen", "asr:whisper-small")]
LETTERS = "abcdefgh"

SYSTEM = "You are a strict, consistent evaluator of summary content."
RULES = """Decide, for each numbered fact, whether the SUMMARY conveys it.

A fact is supported if the summary states its core information or clearly implies it, even in different words, in another language (English, Hindi or Hinglish) or in another script. It is not supported if it is missing, only vaguely related, or contradicted. Judge each fact independently, using only the summary.

Additional rules (apply identically to every summary):
1. Facts whose core is a specific path, shortcut, value or name (e.g. "File > Save", "Ctrl+Alt+T", "228") need that specific element; a generic mention does not count.
2. A contradicted fact (wrong value/direction) is unsupported.
3. A garbled product name does not by itself cancel a correctly stated fact.
4. Hallucinated content never supports a fact."""

STOP = set("""the a an and or of to in on for with by from into onto as at is are be can its it this that these those
using use used via then also which when while their there will was were has have been than through each""".split())
def content_words(t):
    return {w for w in re.findall(r"[a-z0-9][a-z0-9+.#_-]*", t.lower()) if len(w) >= 4 and w not in STOP}
def on_screen_share(fact, screen):
    cw = content_words(fact)
    scr = content_words(screen)
    return len(cw & scr) / len(cw) if cw else 0.0

if a.cmd == "packets":
    vid = pd.read_csv(a.video or f"{a.root}/outputs/video/summaries_video{SFX}.csv", keep_default_na=False)
    if RAW_ANCH:
        raw = pd.read_csv(a.raw_video or f"{a.root}/outputs/video/summaries_video.csv", keep_default_na=False)
    old = pd.read_csv(f"{S2}/summaries.csv", keep_default_na=False)
    old = old[old.out_lang == "en"].set_index(["window_id", "condition"]).summary
    wins = a.windows.split(",") if a.windows else WINS
    mapping = json.load(open(MAPF)) if os.path.exists(MAPF) else {}
    parts = ["# Video (screen-text) judging packets\n\nJudge: the SAME judge as the paper (Claude Sonnet 5.5, chat). "
             "Start a NEW chat, paste the instructions block once, then paste one window block at a time and copy "
             "the reply lines into judge_video_responses.txt. If the chat gets long (about 8 windows), start a new "
             "chat and paste the instructions block again.\n\n## Instructions block (paste first)\n\n```\n" + SYSTEM +
             "\n\n" + RULES + "\n\nFor each SUMMARY id I send, reply with exactly one line: <id>: <bit string>, one "
             "digit per fact in order (1 = supported, 0 = not supported). No other text.\n```\n"]
    for w in wins:
        items = [(c, "video", vid[(vid.window_id == w) & (vid.condition == c)].summary.iloc[0]) for c in VIDEO]
        items += [(c, "anchor_original", old[(w, c)]) for c in ANCH]
        items += [(c, "anchor_raw_screen", raw[(raw.window_id == w) & (raw.condition == c)].summary.iloc[0])
                  for c in RAW_ANCH]
        n_items = len(items)
        random.Random(f"video{SFX}-{w}").shuffle(items)
        fl = facts[facts.window_id == w]
        ftxt = "\n".join(f"{i + 1}. {t}" for i, t in enumerate(fl.fact))
        sec = [f"## Window {w}  ({len(fl)} facts, {n_items} summaries)\n\n```\nFACTS:\n{ftxt}\n"]
        for k, (c, kind, s) in enumerate(items):
            bid = f"{PFX}-{w}-{LETTERS[k]}"
            mapping[bid] = {"window_id": w, "condition": c, "kind": kind}
            sec.append(f"\nSUMMARY {bid}:\n<<<\n{s}\n>>>\n")
        sec.append("```\n")
        parts.append("".join(sec))
    name = f"{a.res}/judge_packets_video{SFX}{'_' + a.tag if a.tag else ''}.md"
    open(name, "w").write("\n".join(parts))
    json.dump(mapping, open(MAPF, "w"), indent=1)
    print(f"{len(wins)} windows, {n_items * len(wins)} summaries -> {name}")

else:
    mapping = json.load(open(MAPF))
    txt = open(f"{a.res}/judge_video{SFX}_responses.txt").read()
    got = dict(re.findall(PFX + r"(-W\d\d-[a-h])\s*[:=\-]\s*([01]+)", txt))
    got = {PFX + k: v for k, v in got.items()}
    missing = sorted(set(mapping) - set(got))
    if missing:
        print(f"MISSING answers for {len(missing)} ids:", missing)
    rows = []
    for bid, bits in got.items():
        m = mapping[bid]
        fl = facts[facts.window_id == m["window_id"]]
        if len(bits) != len(fl):
            print(f"WARNING {bid}: {len(bits)} digits for {len(fl)} facts - skipped")
            continue
        rows += [dict(bid=bid, **m, fact_id=f, supported=int(b)) for f, b in zip(fl.fact_id, bits)]
    # fact_type: is the fact visibly on screen? share of its content words (>=4 letters) found in the window's OCR text
    scr = pd.read_csv(a.screen or f"{a.root}/outputs/video/screen_text.csv", keep_default_na=False)
    scr = scr.set_index("window_id").screen_text
    facts["screen_share"] = [on_screen_share(f, scr.get(w, "")) for f, w in zip(facts.fact, facts.window_id)]
    facts["fact_type"] = np.where(facts.screen_share >= 0.5, "on_screen", "speech_only")
    facts[["window_id", "fact_id", "fact", "tag", "screen_share", "fact_type"]].to_csv(f"{a.res}/fact_screen_overlap.csv", index=False)
    print(facts.fact_type.value_counts().to_string())
    j = pd.DataFrame(rows).merge(facts[["fact_id", "tag", "fact_type"]], on="fact_id")
    j.to_csv(f"{a.res}/judgements_video{SFX}.csv", index=False)
    n_w = j.window_id.nunique()
    print(f"{len(got)} summaries scored, {n_w} windows, {len(j)} fact decisions")

    # 1. test-retest of the anchors against the mean of passes 1-4
    if a.passes:
        p = pd.read_csv(a.passes)
        p = p[p.out_lang == "en"].groupby(["condition", "fact_id"]).supported.mean().rename("prev").reset_index()
        anc = j[j.kind == "anchor_original"].merge(p, on=["condition", "fact_id"])
        anc["prev_major"] = (anc.prev >= 0.5).astype(int)
        for c, g in anc.groupby("condition"):
            x, y = g.supported, g.prev_major
            po = (x == y).mean(); pe = x.mean() * y.mean() + (1 - x.mean()) * (1 - y.mean())
            print(f"  retest {c:30s} n={len(g)} agree={po:.3f} kappa={(po - pe) / (1 - pe):.2f} "
                  f"recall now {x.mean():.3f} vs earlier passes {g.prev.mean():.3f}")

    # 1b. clean set: re-judged raw-OCR anchors vs their judgements in the raw video session
    if a.set == "clean" and os.path.exists(f"{a.res}/judgements_video.csv"):
        prev = pd.read_csv(f"{a.res}/judgements_video.csv")[["condition", "fact_id", "supported"]]
        rr_ = j[j.kind == "anchor_raw_screen"].merge(prev, on=["condition", "fact_id"], suffixes=("", "_prev"))
        for c, g in rr_.groupby("condition"):
            x, y = g.supported, g.supported_prev
            po = (x == y).mean(); pe = x.mean() * y.mean() + (1 - x.mean()) * (1 - y.mean())
            print(f"  retest {c:30s} n={len(g)} agree={po:.3f} kappa={(po - pe) / (1 - pe):.2f} "
                  f"recall now {x.mean():.3f} vs raw-video session {y.mean():.3f}")

    # 2. recall table
    tab = j.pivot_table(index="condition", columns="tag", values="supported", aggfunc="mean")
    tab["all"] = j.groupby("condition").supported.mean()
    tab2 = j.pivot_table(index="condition", columns="fact_type", values="supported", aggfunc="mean")
    print("\nRecall (micro, this session):\n", tab.join(tab2).round(3).to_string())

    # 3. paired window-level tests (each video condition vs its no-screen counterpart, same session)
    pw = j.groupby(["window_id", "condition"]).supported.mean().unstack()
    rng = np.random.default_rng(13)
    res = []
    for c, b in PAIRS:
        for ft in ["all", "on_screen", "speech_only"]:
            d = j if ft == "all" else j[j.fact_type == ft]
            q = d.groupby(["window_id", "condition"]).supported.mean().unstack()[[c, b]].dropna()
            diff = (q[c] - q[b]).values
            pval = wilcoxon(diff).pvalue if (diff != 0).any() else 1.0
            boot = [diff[rng.integers(0, len(diff), len(diff))].mean() for _ in range(2000)]
            res.append(dict(condition=c, baseline=b, facts=ft, n_windows=len(q), base=q[b].mean(), cond=q[c].mean(),
                            diff=diff.mean(), ci_lo=np.percentile(boot, 2.5), ci_hi=np.percentile(boot, 97.5),
                            wins=int((diff > 0).sum()), losses=int((diff < 0).sum()), wilcoxon_p=pval))
    res = pd.DataFrame(res)
    allp = res.facts == "all"
    order = res[allp].wilcoxon_p.sort_values().index
    m = len(order); run = 0
    for k, i in enumerate(order):                       # Holm over the primary ("all facts") tests
        run = max(run, min(1, (m - k) * res.loc[i, "wilcoxon_p"])); res.loc[i, "holm_p"] = run
    res.to_csv(f"{a.res}/video_paired{SFX}.csv", index=False)
    print("\nPaired window-level (mean of per-window recall), Holm over the 'all' rows:\n",
          res.round(3).to_string(index=False))

    # 4. gained / lost facts relative to the no-screen counterpart
    wide = j.pivot_table(index=["fact_id", "fact_type"], columns="condition", values="supported").reset_index()
    rr = []
    for c, b in PAIRS:
        k = wide[[c, b, "fact_type"]].dropna()
        rr.append(dict(condition=c, baseline=b, gained=int(((k[c] == 1) & (k[b] == 0)).sum()),
                       lost=int(((k[c] == 0) & (k[b] == 1)).sum()), both=int(((k[c] == 1) & (k[b] == 1)).sum()),
                       gained_on_screen=int(((k[c] == 1) & (k[b] == 0) & (k.fact_type == "on_screen")).sum()),
                       n_facts=len(k)))
    pd.DataFrame(rr).to_csv(f"{a.res}/video_gain_loss{SFX}.csv", index=False)
    print("\nFacts gained/lost vs counterpart:\n", pd.DataFrame(rr).to_string(index=False))
    tab.join(tab2).to_csv(f"{a.res}/video_recall_table{SFX}.csv")
