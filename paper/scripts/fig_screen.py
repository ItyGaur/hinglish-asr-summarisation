"""Figure: fact recall with no / raw / cleaned screen text, by fact type (clean-session judgements, window means)."""
import sys, pandas as pd, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
j = pd.read_csv(sys.argv[1]); out = sys.argv[2]
SER = [("", "No screen text", "#2a78d6", None), ("+screen", "Raw OCR", "#eb6834", None),
       ("+screen_clean", "Cleaned OCR", "#1baf7a", "////")]
TR = [("oracle", "Oracle"), ("asr:whisper-small", "whisper-small")]
plt.rcParams.update({"font.size": 7, "font.family": "serif", "axes.spines.top": False, "axes.spines.right": False,
                     "hatch.linewidth": 0.6, "hatch.color": "white"})
fig, axes = plt.subplots(1, 2, figsize=(3.5, 1.9), sharey=True)
for ax, (ft, title) in zip(axes, [("on_screen", "Facts visible on screen (90)"), ("speech_only", "Speech-only facts (178)")]):
    q = j[j.fact_type == ft].groupby(["window_id", "condition"]).supported.mean().unstack().mean()
    w = 0.26
    for k, (sfx, lab, col, hat) in enumerate(SER):
        xs = [i + (k - 1) * (w + 0.02) for i in range(len(TR))]
        ys = [q[t + sfx] for t, _ in TR]
        ax.bar(xs, ys, w, color=col, hatch=hat, label=lab, edgecolor="none")
        for x, y in zip(xs, ys):
            ax.text(x, y + 0.012, f"{y:.2f}", ha="center", va="bottom", fontsize=5.5, color="#3a3a38")
    ax.set_xticks(range(len(TR))); ax.set_xticklabels([n for _, n in TR])
    ax.set_title(title, fontsize=7); ax.set_ylim(0, 0.65); ax.tick_params(length=2)
    ax.yaxis.grid(True, color="#e4e4e0", linewidth=0.5); ax.set_axisbelow(True)
axes[0].set_ylabel("Fact recall (window mean)")
axes[1].legend(frameon=False, fontsize=6, loc="upper right", handlelength=1.2, borderaxespad=0.1)
fig.tight_layout(pad=0.3, w_pad=0.6); fig.savefig(out); fig.savefig(out.replace(".pdf", ".png"), dpi=200)
print(out)
