"""Summarise the two new conditions (+ regenerated controls) with the SAME Qwen setup as Step 2.

Colab (T4) or Kaggle (T4/P100). In a notebook cell:
    !pip install -q "transformers>=4.45" bitsandbytes accelerate
    !python run_qwen_v2.py --root /content/drive/MyDrive/hinglish_asr_sum
Kaggle: upload hinglish_asr_sum as a dataset, then
    !python run_qwen_v2.py --root /kaggle/working/hinglish_asr_sum   (copy the dataset there first)

Resumable: every summary is cached to <root>/cache/qwen_v2/<key>.json the moment it is
made, so if the GPU quota cuts you off just run the same command again later.

Work: script_shift_v2 (25) then asr:trelis+backtranslit (25) = 50 summaries, about 15-20 min on a T4.
Add --controls to also regenerate oracle + Trelis (normally unnecessary).

Settings copied from logs/run_config_step2.json: Qwen/Qwen2.5-7B-Instruct @ a09a354,
bnb nf4 4-bit, fp16 compute, greedy, max_new_tokens 320, batch 4, prompt template
summary_en (checked against logs/prompts_log.jsonl at start-up). Writes outputs/step2/summaries_v2.csv at the end.
"""
import argparse
import datetime as dt
import glob
import hashlib
import json
import os

import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

MODEL = "Qwen/Qwen2.5-7B-Instruct"
REV = "a09a35458c702b33eeacc393d103063234e8bc28"
SYSTEM = "You are a helpful assistant that summarises lecture transcripts."
USER_T = (
    "The following is an automatic transcript of part of a recorded computer-software tutorial. "
    "The speaker mixes Hindi and English (Hinglish); Hindi may be written in Devanagari and English "
    "in Latin script, and words of either language may appear in either script.\n\n"
    "Write a summary in English of 120-180 words covering the main steps, concepts and facts taught. "
    "Write plain prose: no bullet points, no title.\n\n"
    "Transcript:\n<<<\n{transcript}\n>>>"
)
GEN = dict(max_new_tokens=320, do_sample=False, temperature=None, top_p=None, top_k=None)
BATCH = 4

ap = argparse.ArgumentParser()
ap.add_argument("--root", required=True)
ap.add_argument("--controls", action="store_true",
                help="also regenerate oracle + Trelis (not needed: the 400-summary rerun reproduced all 256 originals exactly)")
args = ap.parse_args()
ROOT = args.root
S2 = f"{ROOT}/outputs/step2"
CACHE = f"{ROOT}/cache/qwen_v2"
os.makedirs(CACHE, exist_ok=True)

# Check the prompt text is identical to the summary_en template logged in Step 2.
logged = [json.loads(l) for l in open(f"{ROOT}/logs/prompts_log.jsonl")]
logged = [d["prompt"] for d in logged if d.get("component") == "summary_en" and d.get("step") == "2-templates"]
assert logged and logged[0]["system"] == SYSTEM and logged[0]["user_template"] == USER_T, \
    "Prompt differs from the Step-2 template in prompts_log.jsonl - stop and check."
print("prompt template: identical to Step 2")

new = pd.read_csv(f"{S2}/conditions_v2.csv")
WINS = sorted(new.window_id.unique())
old = pd.read_csv(f"{S2}/conditions.csv")
jobs = []
for c in ["script_shift_v2", "asr:trelis+backtranslit"]:
    jobs += [(w, c, new[(new.window_id == w) & (new.condition == c)].text.iloc[0]) for w in WINS]
if args.controls:
    for c in ["oracle", "asr:trelis-hinglish-preview"]:
        jobs += [(w, c, old[(old.window_id == w) & (old.condition == c)].text.iloc[0]) for w in WINS]

key = lambda w, c: hashlib.sha256(f"{w}|{c}|en|v2".encode()).hexdigest()[:24]
todo = [j for j in jobs if not os.path.exists(f"{CACHE}/{key(j[0], j[1])}.json")]
print(f"{len(jobs) - len(todo)} cached, {len(todo)} to generate")

if todo:
    tok = AutoTokenizer.from_pretrained(MODEL, revision=REV)
    tok.padding_side = "left"
    bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                             bnb_4bit_compute_dtype=torch.float16)
    model = AutoModelForCausalLM.from_pretrained(MODEL, revision=REV, quantization_config=bnb,
                                                 device_map="auto", dtype=torch.float16)
    model.eval()
    gen = {k: v for k, v in GEN.items() if v is not None}
    for i in range(0, len(todo), BATCH):
        batch = todo[i:i + BATCH]
        prompts = [tok.apply_chat_template(
            [{"role": "system", "content": SYSTEM},
             {"role": "user", "content": USER_T.format(transcript=t)}],
            tokenize=False, add_generation_prompt=True) for _, _, t in batch]
        enc = tok(prompts, return_tensors="pt", padding=True).to(model.device)
        with torch.no_grad():
            out = model.generate(**enc, **gen, pad_token_id=tok.eos_token_id)
        for k_, (w, c, _) in enumerate(batch):
            n_in = int(enc["attention_mask"][k_].sum())
            text = tok.decode(out[k_][enc["input_ids"].shape[1]:], skip_special_tokens=True).strip()
            rec = dict(created=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                       model=MODEL, revision=REV, gen=str(GEN), batch=BATCH, window_id=w,
                       condition=c, out_lang="en", input_tokens=n_in, summary=text,
                       gpu=torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
                       transformers=__import__("transformers").__version__)
            json.dump(rec, open(f"{CACHE}/{key(w, c)}.json", "w"), ensure_ascii=False)
        print(f"done {min(i + BATCH, len(todo))}/{len(todo)}  ({batch[0][1]})", flush=True)
    with open(f"{ROOT}/logs/prompts_log.jsonl", "a") as f:
        f.write(json.dumps({"ts": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                            "step": "2-v2", "component": "summary_en", "model": MODEL,
                            "params": {"revision": REV, "gen": GEN, "batch": BATCH,
                                       "conditions": sorted({c for _, c, _ in jobs})},
                            "prompt": {"system": SYSTEM, "user_template": USER_T}},
                           ensure_ascii=False) + "\n")

recs = [json.load(open(p)) for p in glob.glob(f"{CACHE}/*.json")]
df = pd.DataFrame(recs)
df["summary_words"] = df.summary.str.split().str.len()
df.sort_values(["condition", "window_id"]).to_csv(f"{S2}/summaries_v2.csv", index=False)
print("wrote", f"{S2}/summaries_v2.csv", df.groupby("condition").size().to_dict())

# Reproducibility check: regenerated controls vs the summaries used in the paper
saved = pd.read_csv(f"{S2}/summaries.csv")
saved = saved[saved.out_lang == "en"].set_index(["window_id", "condition"]).summary
for c in ["oracle", "asr:trelis-hinglish-preview"]:
    g = df[df.condition == c]
    if len(g):
        same = sum(str(r.summary).strip() == str(saved.get((r.window_id, c), "")).strip()
                   for r in g.itertuples())
        print(f"regenerated {c}: {same}/{len(g)} identical to the original summaries")
