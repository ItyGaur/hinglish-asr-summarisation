"""Video branch: align each window to its Spoken Tutorial video, OCR the screen, build inputs.

Usage (Colab, from the Drive project folder):
    python video_pipeline.py download --root ROOT          (reads ROOT/video_urls.csv)
    python video_pipeline.py align   --root ROOT --mucs /content/mucs_data/raw/extracted
    python video_pipeline.py ocr     --root ROOT
    python video_pipeline.py build   --root ROOT

Inputs:  ROOT/videos/W00.<ext> ... W24.<ext>   (Hindi Spoken Tutorial videos, any ffmpeg-readable format)
         ROOT/outputs/selected_windows.csv, ROOT/outputs/step2/conditions.csv
Outputs (all new files under ROOT/outputs/video/):
  alignment.csv        window -> [t_start, t_end] in the video, how it was found, confidence
  frames/W00/*.png     kept (de-duplicated) frames
  ocr_lines.csv        every kept OCR line: window, time (s from window start), text, confidence
  screen_text.csv      one row per window: the de-duplicated screen text in time order
  conditions_video.csv inputs for the summariser (transcript + screen text, and screen text only)
"""
import argparse, glob, json, os, re, subprocess, sys
import numpy as np
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("stage", choices=["download", "align", "ocr", "build"])
ap.add_argument("--root", required=True)
ap.add_argument("--mucs", help="extracted MUCS test folder (needed for align)")
ap.add_argument("--fps", type=float, default=0.5, help="frames per second sampled before de-duplication")
ap.add_argument("--max-screen-chars", type=int, default=6000)
A = ap.parse_args()
ROOT = A.root
OUT = f"{ROOT}/outputs/video"
os.makedirs(OUT, exist_ok=True)
SR = 8000
sel = pd.read_csv(f"{ROOT}/outputs/selected_windows.csv")
WINS = list(sel.window_id)


def video_path(w):
    c = sorted(p for p in glob.glob(f"{ROOT}/videos/{w}.*") if not p.endswith(".part"))
    return c[0] if c else None


def video_audio(path):
    """Mono 8 kHz float32 audio of the video's soundtrack via ffmpeg."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def video_duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout.strip()
    return float(out)


def locate(template, signal):
    """Position (s) of template inside signal by normalised FFT cross-correlation, plus a confidence:
    peak height divided by the 99.9th percentile of the correlation (>3 = clear match)."""
    from scipy.signal import fftconvolve
    t = (template - template.mean()) / (template.std() + 1e-8)
    s = signal - signal.mean()
    corr = fftconvolve(s, t[::-1], mode="valid")
    # local energy normalisation so loud passages do not win by default
    win = np.ones(len(t))
    energy = np.sqrt(np.maximum(fftconvolve(s ** 2, win, mode="valid"), 1e-8))
    ncc = corr / energy
    k = int(np.argmax(ncc))
    conf = float(ncc[k] / (np.percentile(np.abs(ncc), 99.9) + 1e-8))
    return k / SR, conf



# --------------------------------------------------------------------------------------------- download
if A.stage == "download":
    urls = pd.read_csv(f"{ROOT}/video_urls.csv", keep_default_na=False)
    os.makedirs(f"{ROOT}/videos", exist_ok=True)
    for r in urls.itertuples():
        if video_path(r.window_id):
            print(r.window_id, "already downloaded"); continue
        ext = os.path.splitext(r.video_url)[1] or ".webm"
        dst = f"{ROOT}/videos/{r.window_id}{ext}"
        rc = subprocess.run(["wget", "-q", "--tries=3", "--timeout=60", "-O", dst + ".part", r.video_url]).returncode
        if rc == 0 and os.path.getsize(dst + ".part") > 200_000:
            os.rename(dst + ".part", dst)
            print(r.window_id, "ok", round(os.path.getsize(dst) / 1e6, 1), "MB", round(video_duration(dst) / 60, 1), "min")
        else:
            print(r.window_id, "FAILED - download it in a browser from", r.watch_url, "and save as", os.path.basename(dst))
            if os.path.exists(dst + ".part"):
                os.remove(dst + ".part")

# --------------------------------------------------------------------------------------------- align
if A.stage == "align":
    import soundfile as sf
    from scipy.signal import resample_poly
    seg_files = glob.glob(f"{A.mucs}/**/segments", recursive=True)
    scp_files = glob.glob(f"{A.mucs}/**/wav.scp", recursive=True)
    assert seg_files, "MUCS segments file not found under --mucs"
    kdir = os.path.dirname(seg_files[0])
    seg = pd.read_csv(seg_files[0], sep=r"\s+", header=None, names=["utt", "reco", "start", "end"])
    wavs = {os.path.basename(p): p for p in glob.glob(f"{A.mucs}/**/*.wav", recursive=True)}
    scp = {}
    if scp_files:
        for line in open(scp_files[0]):
            k, v = line.strip().split(None, 1)
            cand = [x for x in v.split() if x.endswith(".wav")] or [v]
            p = cand[0]
            scp[k] = p if os.path.isfile(p) else (os.path.join(kdir, p) if os.path.isfile(os.path.join(kdir, p))
                                                  else wavs.get(os.path.basename(p)))

    def mucs_span(reco, start, end):
        path = scp.get(reco) or wavs.get(reco + ".wav")
        info = sf.info(path)
        x, sr = sf.read(path, start=int(start * info.samplerate), stop=int(end * info.samplerate),
                        dtype="float32", always_2d=True)
        x = x.mean(axis=1)
        g = np.gcd(int(sr), SR)
        return resample_poly(x, SR // g, int(sr) // g).astype("float32")

    rows = []
    for w in sel.itertuples():
        vp = video_path(w.window_id)
        if not vp:
            print(f"{w.window_id}: video missing"); continue
        va = video_audio(vp)
        ids = w.utt_ids.split()
        s = seg.set_index("utt")
        first, last = s.loc[ids[0]], s.loc[ids[-1]]
        # use up to 6 s of the first and last utterance as templates
        f_t = mucs_span(w.reco_id, first.start, min(first.end, first.start + 6))
        l_t = mucs_span(w.reco_id, max(last.start, last.end - 6), last.end)
        t_first, c_first = locate(f_t, va)
        t_last, c_last = locate(l_t, va)
        t_start, t_end = t_first, t_last + len(l_t) / SR
        ok = min(c_first, c_last) > 3 and t_end > t_start
        method = "audio_xcorr"
        # sanity check: the matched span must be close to the window's speech length; if the first-utterance
        # match is weak and the span is too short, trust the (strong) last-utterance match and back off from it
        if ok and abs((t_end - t_start) - w.speech_sec) > 0.05 * w.speech_sec and c_last > 2 * c_first:
            t_start, method = max(0.0, t_end - w.speech_sec), "audio_xcorr_lastonly"
        if not ok:   # fallback: proportional position of the window's speech inside the recording's speech
            tot = seg[seg.reco == w.reco_id]
            frac = (last.end - tot.start.min()) / (tot.end.max() - tot.start.min())
            t_start, t_end, method = 0.0, frac * video_duration(vp), "proportional_fallback"
        rows.append(dict(window_id=w.window_id, video=os.path.basename(vp), t_start=round(t_start, 2),
                         t_end=round(t_end, 2), conf_first=round(c_first, 2), conf_last=round(c_last, 2),
                         method=method, video_sec=round(len(va) / SR, 1), window_speech_sec=w.speech_sec))
        print(rows[-1], flush=True)
    al = pd.DataFrame(rows)
    al.to_csv(f"{OUT}/alignment.csv", index=False)
    print(al.method.value_counts().to_string())
    print("Check: wall-clock span should be a bit longer than speech_sec (pauses):")
    print((al.t_end - al.t_start - al.window_speech_sec).describe().round(1).to_string())

# --------------------------------------------------------------------------------------------- ocr
if A.stage == "ocr":
    import pytesseract, imagehash
    from PIL import Image
    al = pd.read_csv(f"{OUT}/alignment.csv")
    done = set(pd.read_csv(f"{OUT}/ocr_lines.csv").window_id) if os.path.exists(f"{OUT}/ocr_lines.csv") else set()
    for r in al.itertuples():
        if r.window_id in done:
            continue
        fdir = f"{OUT}/frames/{r.window_id}"
        os.makedirs(fdir, exist_ok=True)
        tmp = f"/content/frames_tmp_{r.window_id}"
        os.makedirs(tmp, exist_ok=True)
        subprocess.run(["ffmpeg", "-v", "error", "-ss", str(r.t_start), "-to", str(r.t_end), "-i",
                        f"{ROOT}/videos/{r.video}", "-vf", f"fps={A.fps}", f"{tmp}/f_%05d.png"], check=True)
        frames = sorted(glob.glob(f"{tmp}/f_*.png"))
        kept, prev = [], None
        for i, fp in enumerate(frames):
            h = imagehash.phash(Image.open(fp))
            if prev is None or h - prev > 6:          # screen changed noticeably
                kept.append((i / A.fps, fp)); prev = h
        seen, lines = set(), []
        for t, fp in kept:
            img = Image.open(fp).convert("L")
            img = img.resize((img.width * 2, img.height * 2))       # small UI fonts OCR better upscaled
            d = pytesseract.image_to_data(img, lang="eng", config="--psm 11", output_type=pytesseract.Output.DATAFRAME)
            d = d[(d.conf > 60) & d.text.notna()]
            d["text"] = d.text.astype(str).str.strip()
            d = d[d.text.str.len() > 0]
            for key, g in d.groupby(["block_num", "par_num", "line_num"]):
                txt = " ".join(g.text)
                norm = re.sub(r"[^a-z0-9+.>/_\- ]", "", txt.lower()).strip()
                letters = sum(ch.isalpha() for ch in norm)
                if letters < 3 or norm in seen:
                    continue
                seen.add(norm)
                lines.append(dict(window_id=r.window_id, t=round(t, 1), text=txt, conf=round(g.conf.mean(), 1)))
            Image.open(fp).save(f"{fdir}/t{int(t):04d}.png")
        for fp in frames:
            os.remove(fp)
        pd.DataFrame(lines).to_csv(f"{OUT}/ocr_lines.csv", mode="a", header=not os.path.exists(f"{OUT}/ocr_lines.csv"),
                                   index=False)
        print(f"{r.window_id}: {len(frames)} frames sampled, {len(kept)} kept, {len(lines)} new text lines", flush=True)

# --------------------------------------------------------------------------------------------- build
if A.stage == "build":
    ocr = pd.read_csv(f"{OUT}/ocr_lines.csv", keep_default_na=False)
    cond = pd.read_csv(f"{ROOT}/outputs/step2/conditions.csv", keep_default_na=False)
    st_rows, rows = [], []
    for w in WINS:
        g = ocr[ocr.window_id == w].sort_values("t")
        text = "\n".join(f"[{int(t // 60):02d}:{int(t % 60):02d}] {x}" for t, x in zip(g.t, g.text))
        if len(text) > A.max_screen_chars:
            text = text[:A.max_screen_chars].rsplit("\n", 1)[0]
        st_rows.append(dict(window_id=w, n_lines=len(g), screen_text=text, chars=len(text)))
        for c in ["oracle", "asr:trelis-hinglish-preview", "asr:whisper-small"]:
            tr = cond[(cond.window_id == w) & (cond.condition == c)].text.iloc[0]
            rows.append(dict(window_id=w, condition=f"{c}+screen", transcript=tr, screen_text=text))
        rows.append(dict(window_id=w, condition="screen_only", transcript="", screen_text=text))
    pd.DataFrame(st_rows).to_csv(f"{OUT}/screen_text.csv", index=False)
    pd.DataFrame(rows).to_csv(f"{OUT}/conditions_video.csv", index=False)
    print(pd.DataFrame(st_rows)[["window_id", "n_lines", "chars"]].to_string(index=False))
