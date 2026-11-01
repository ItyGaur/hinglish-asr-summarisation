# Speech Errors and Screen Text in LLM Summaries of Hinglish Tutorial Videos

Code, data and results for a short NLP study (preliminary evidence, small N, silver references).
Paper draft (IEEE conference format): `paper/main.tex`. Submission link: TODO.

**Question.** When Hindi-English (Hinglish) spoken-tutorial audio is transcribed by ASR and then
summarised by an LLM, how much summary content is lost, and is the loss concentrated on
Hindi-spoken or English-spoken content (code-switching loss, CSL)? And can text shown on screen
in the tutorial video (read by OCR) make up for recognition errors?

**Setup.** 25 windows (5-10 min) from the MUCS 2021 Hi-En test set · ASR: whisper-small and
Trelis whisper-hinglish-preview · summariser: Qwen2.5-7B-Instruct (4-bit, greedy) · controlled
noise on Hindi-only / English-only tokens (10-50%) · script-shift and back-transliteration
conditions · screen text from the matching Spoken Tutorial videos (audio-aligned, Tesseract OCR,
raw and rule-cleaned) added to each transcript · metrics: judge-based fact recall (overall, by fact
language, and for on-screen vs speech-only facts), ROUGE-1/2/L, BERTScore.

**Main findings.** whisper-small (WER 0.70) cuts fact recall from 0.47 to 0.21; the Hinglish-tuned
Trelis model (WER 0.28) causes no significant loss, and much of its English-word error is English
written in Devanagari, which the summariser handles without loss. Raw screen text lowers recall from a
good transcript (0.51 → 0.39) but restores facts visible on screen when ASR is weak (0.18 → 0.30);
cleaning the OCR text roughly halves the loss (not significant).

**Who did what (disclosure).** Silver reference summaries, atomic facts and the first
English→Devanagari lexicon: **Gemini**. Summaries: **Qwen2.5-7B-Instruct**. Fact judgements:
**Claude Sonnet 5.5** (chat interface, blind to condition, four passes for the English oracle).
OCR: **Tesseract**. A human annotator checked 30 judge decisions and 105 reference facts.

## Repository structure

```
notebooks/          pipeline, in order (01 ASR → 02 summaries/references → 03-05 follow-ups →
                    06 video alignment + OCR + screen summaries → 07 cleaned screen text)
scripts/            analysis scripts (each documents its inputs/outputs in its docstring)
data/hinglish_asr_sum/
  outputs/          ASR hypotheses + metrics, selected windows, silver references/facts,
                    all input conditions, all summaries, ROUGE and BERTScore for every summary
  logs/             every prompt template and run configuration (model revisions, settings)
  cache/            raw model responses (Gemini, Qwen)
judging/
  protocol/         judge rules + Claude-vs-Gemini judge comparison
  pass1_original/   main judging pass (W00-W24): packets, raw replies, blind mappings, decisions
  pass2_script_shift/   script-shift session (+ oracle/Trelis re-judged = test-retest)
  pass3_hinglish_noise/ first Hinglish outputs (cut off at 320 tokens) + noise 10/30% (+ oracle, 3rd pass)
  pass4_hinglish_v2/    re-generated Hinglish outputs, limit 1024 tokens (+ oracle, 4th pass)
  pass5_video/          session A: raw screen text (+ no-screen summaries re-judged)
  pass6_video_clean/    session B: cleaned screen text (+ no-screen and raw-screen anchors)
data/video/         alignment, raw screen text, screen summaries (alignment_v1_before_fix.csv = before
                    the 4-window alignment fix)
data/video_clean/   cleaned screen text, per-line keep/drop log, cleaned-screen summaries
human_spotcheck/    human labels vs judge, reference-fact and tag accuracy
results/
  final/            ← main results: every condition × every metric, paired tests, noise slopes,
                      metric validity, judge reliability
  step2_16windows/  first analysis on 16 windows (kept for transparency)
  step2_25windows/  single-pass analysis on 25 windows
  two_pass_average/ oracle/Trelis averaged over two judging passes
  asr_analysis/     what happens to English words in ASR output (re-scripting vs mishearing)
  script_shift/     script-shift and back-transliteration results, judge test-retest
  video/            screen-text results: paired tests, recall tables, gained/lost facts,
                    on-screen fact split (fact_screen_overlap.csv)
paper/              IEEE LaTeX source (main.tex), figures, bibliography
```

## Reproduce the analysis

Python 3.10+, `pip install pandas numpy scipy rouge-score==0.1.2`.

```bash
python scripts/final_analysis.py --root data/hinglish_asr_sum \
  --pass1 judging/pass1_original/judgements_25w.csv \
  --pass2 judging/pass2_script_shift/judgements_script_shift.csv \
  --pass3 judging/pass3_hinglish_noise/judgements_pass3_hinglish_noise.csv \
  --v2 data/hinglish_asr_sum/outputs/step2/summaries_v2.csv \
  --bertscore data/hinglish_asr_sum/outputs/step2/bertscore_all.csv \
  --pass4 judging/pass4_hinglish_v2/judgements_pass4_hinglish_v2.csv \
  --hinglish-v2 data/hinglish_asr_sum/outputs/step2/summaries_hinglish_v2.csv \
  --out results/final
```

Screen-text results (after the judge replies are in `judging/pass5_video` and `pass6_video_clean`):

```bash
python scripts/judge_video.py score --root data/hinglish_asr_sum --res judging/pass5_video \
  --screen data/video/screen_text.csv --passes results/final/judgements_all_passes.csv
python scripts/judge_video.py score --set clean --root data/hinglish_asr_sum --res judging/pass6_video_clean \
  --screen data/video/screen_text.csv
```

Re-running the models (ASR, Qwen, BERTScore) needs a GPU (free Colab/Kaggle T4); see the notebooks.
The MUCS audio is downloaded by notebook 01 from OpenSLR and is not stored here; the tutorial videos
are downloaded by notebook 06 from spoken-tutorial.org (URLs in the notebook) and are not stored here.

## Known limitations

Silver (LLM-written) references; 25 windows, one domain (spoken software tutorials); only 28
English-tagged facts; one summariser; LLM judge with moderate test-retest agreement
(pairwise κ 0.36-0.75 across four passes; human agreement κ 0.90 on 30 decisions); the English
tag is a script-share threshold. Hinglish output: Qwen mostly wrote Devanagari Hindi rather than the
requested Roman-script Hinglish; the first run was cut off by a 320-token limit (kept as
`hinglish_320`) and was re-generated with a 1024-token limit (`hinglish`); 6/75 re-generated outputs
fell into repetition loops (`results/final/hinglish_truncation.csv`). Video: 8 of 25 windows needed a
weak or fallback alignment, OCR is English-only and noisy, and the on-screen fact split is a word-overlap
heuristic.

## Licence

Code: MIT (`LICENSE`). Data and results: CC BY-SA 4.0, derived from MUCS 2021 / OpenSLR 104
(`DATA_LICENSE.md`).
