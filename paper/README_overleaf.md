# Paper draft (IEEE conference format): how to compile

1. In Overleaf: New Project -> Upload Project -> upload this zip. Compile with pdfLaTeX.
   IEEEtran.cls (official v1.8b) is included; Overleaf also has it built in.
2. Search for TODO (shown in red in the PDF) and fill in:
   - author names and emails (5 authors)
   - the Trelis model-card access date (reference 7)
   - confirm the AI-use statement against your venue's policy
   - optional acknowledgment (commented out near the end of main.tex)

Files:
- main.tex: the paper (6 pages)
- figures/noise.pdf, figures/enfate.pdf: audio-branch figures (from results/final/)
- figures/screen.pdf: screen-text figure (from results/video/judgements_video_clean.csv)
- scripts/fig_screen.py: regenerates figures/screen.pdf

Every number comes from results/final/ and results/video/ in
https://github.com/ItyGaur/hinglish-asr-summarisation
