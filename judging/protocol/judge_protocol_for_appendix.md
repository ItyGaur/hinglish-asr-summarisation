# Fact-judging protocol (for the paper appendix)

**Judge:** Claude Sonnet 5.5 (Anthropic), used through the chat interface (not the API), after the planned
Gemini judge hit its free-tier quota. Temperature/seed could not be controlled and the run is not
bit-reproducible; the raw decisions are released in `judge_raw_bitstrings_and_blind_mapping.json`.
**Blinding:** for each window the summaries were shuffled and given ids (W00-01 ...); the judge did not see
which condition (oracle / ASR / noise level) produced a summary.
**Input per item:** one summary + the numbered silver facts of that window; one 0/1 decision per fact.
**Items judged:** 16 windows x (oracle, 2 real-ASR, noise hi/en at 20/40/50 %) = 144 English summaries
+ 16 silver reference summaries (judge ceiling: 87.6 %). Not judged: Hinglish-output summaries, noise 10/30 %,
script-shift condition (quota/time).

**Decision rules (applied identically to every item):**
1. A fact is supported if the summary states its core information or clearly implies it, in other words.
2. Facts whose core is a specific path, shortcut, value or name (e.g. "File > Save", "Ctrl+Alt+T", "gcc ... -o args",
   "right to top", "228") need that specific element; a generic mention ("saves the file") does not count.
3. A contradicted fact (wrong value/direction) is unsupported.
4. A garbled product name does not by itself cancel a correctly stated fact (e.g. "Atit Text Editor is pre-installed").
5. Hallucinated content never supports a fact.

**Agreement with the original Gemini judge** (10 oracle summaries, 104 fact decisions, W00-W09):
agreement 82.7 %, Cohen's kappa 0.62; Claude was more lenient (recall 0.40 vs 0.25). Because one judge is used
for all conditions, between-condition differences are comparable; absolute recall levels are judge-dependent.

**Suggested disclosure sentence:** "Silver references and the script-shift lexicon were produced with Gemini;
summaries with Qwen2.5-7B-Instruct (4-bit); fact support was judged by Claude Sonnet 5.5 (blind to condition,
via chat interface). Three different models were used for writing references, summarising and judging.
Judge decisions were checked against 30 manual labels (agreement/kappa: ___)."
