"""Summarise the video conditions with the same Qwen setup as Step 2 (resumable).
    python run_qwen_video.py --root ROOT
Reads outputs/video/conditions_video.csv; writes outputs/video/summaries_video.csv.
Settings identical to Step 2 (Qwen2.5-7B-Instruct @ a09a354, nf4 4-bit, greedy, batch 4, max_new_tokens 320).
The transcript+screen prompt is the Step-2 summary_en prompt with one added sentence and a screen-text block;
the screen-only prompt describes OCR text instead of a transcript. Both are logged to prompts_log.jsonl."""
import argparse, datetime as dt, glob, hashlib, json, os
import pandas as pd, torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

ap = argparse.ArgumentParser(); ap.add_argument("--root", required=True)
ap.add_argument("--set", choices=["raw", "clean"], default="raw", help="raw OCR (default) or cleaned OCR text")
A = ap.parse_args()
SFX = "" if A.set == "raw" else "_clean"
ROOT = A.root; OUT = f"{ROOT}/outputs/video"; CACHE = f"{ROOT}/cache/qwen_video"; os.makedirs(CACHE, exist_ok=True)
MODEL, REV, BATCH = "Qwen/Qwen2.5-7B-Instruct", "a09a35458c702b33eeacc393d103063234e8bc28", 4
GEN = dict(max_new_tokens=320, do_sample=False)

logged = [json.loads(l) for l in open(f"{ROOT}/logs/prompts_log.jsonl")]
base = [d["prompt"] for d in logged if d.get("component") == "summary_en" and d.get("step") == "2-templates"][0]
SYSTEM, BASE_T = base["system"], base["user_template"]
head, tail = BASE_T.split("\n\nTranscript:\n")            # tail = "<<<\n{transcript}\n>>>"
assert tail == "<<<\n{transcript}\n>>>", "unexpected Step-2 template"
SCREEN_T = (head + "\n\nAfter the transcript you also get the text visible on screen in the tutorial video, read "
            "by OCR in time order; it may contain menu names, commands and recognition errors.\n\nTranscript:\n"
            + tail + "\n\nScreen text:\n<<<\n{screen}\n>>>")
ONLY_T = ("The following is the text visible on screen in a recorded computer-software tutorial video, read by OCR "
          "in time order; it may contain menu names, commands and recognition errors. There is no transcript.\n\n"
          "Write a summary in English of 120-180 words covering the main steps, concepts and facts taught. "
          "Write plain prose: no bullet points, no title.\n\nScreen text:\n<<<\n{screen}\n>>>")

cv = pd.read_csv(f"{OUT}/conditions_video{SFX}.csv", keep_default_na=False)
def prompt(r):
    u = ONLY_T.format(screen=r.screen_text) if r.condition.endswith("_only") else \
        SCREEN_T.format(transcript=r.transcript, screen=r.screen_text)
    return [{"role": "system", "content": SYSTEM}, {"role": "user", "content": u}]
key = lambda w, c: hashlib.sha256(f"{w}|{c}|video".encode()).hexdigest()[:24]
todo = [r for r in cv.itertuples() if not os.path.exists(f"{CACHE}/{key(r.window_id, r.condition)}.json")]
print(f"{len(cv) - len(todo)} cached, {len(todo)} to generate")
if todo:
    tok = AutoTokenizer.from_pretrained(MODEL, revision=REV); tok.padding_side = "left"
    bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.float16)
    model = AutoModelForCausalLM.from_pretrained(MODEL, revision=REV, quantization_config=bnb, device_map="auto",
                                                 dtype=torch.float16).eval()
    for i in range(0, len(todo), BATCH):
        b = todo[i:i + BATCH]
        enc = tok([tok.apply_chat_template(prompt(r), tokenize=False, add_generation_prompt=True) for r in b],
                  return_tensors="pt", padding=True).to(model.device)
        with torch.no_grad():
            out = model.generate(**enc, **GEN, pad_token_id=tok.eos_token_id)
        for k, r in enumerate(b):
            txt = tok.decode(out[k][enc["input_ids"].shape[1]:], skip_special_tokens=True).strip()
            json.dump(dict(created=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), model=MODEL,
                           revision=REV, gen=str(GEN), batch=BATCH, window_id=r.window_id, condition=r.condition,
                           out_lang="en", input_tokens=int(enc["attention_mask"][k].sum()), summary=txt),
                      open(f"{CACHE}/{key(r.window_id, r.condition)}.json", "w"), ensure_ascii=False)
        print(f"done {min(i + BATCH, len(todo))}/{len(todo)}", flush=True)
    with open(f"{ROOT}/logs/prompts_log.jsonl", "a") as f:
        for comp, t in [("summary_en_screen", SCREEN_T), ("summary_en_screen_only", ONLY_T)]:
            f.write(json.dumps({"ts": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "step": "3-video" + SFX,
                                "component": comp, "model": MODEL, "params": dict(revision=REV, **GEN, batch=BATCH),
                                "prompt": {"system": SYSTEM, "user_template": t}}, ensure_ascii=False) + "\n")
df = pd.DataFrame([json.load(open(p)) for p in glob.glob(f"{CACHE}/*.json")])
df = df[df.condition.isin(set(cv.condition))]          # only this set's conditions
df["summary_words"] = df.summary.str.split().str.len()
df["ends_clean"] = df.summary.str.strip().str[-1].isin(list('.!?"\')'))
df.sort_values(["condition", "window_id"]).to_csv(f"{OUT}/summaries_video{SFX}.csv", index=False)
print(df.groupby("condition")[["summary_words", "input_tokens", "ends_clean"]].mean().round(1))
