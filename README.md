# Stochastic Calculus Notes

This repository stores concise notes on stochastic calculus.

- `lecture-notes.pdf` contains the current lecture notes.
- Notes on applications to finance and asset pricing are under development and will be added here as they are completed.

## Splitting the lecture notes

If you need separate PDFs per chapter, use `split_pdf.py` to extract page ranges.
The script requires `PyPDF2` (install with `pip install PyPDF2`).

Example:

```bash
python split_pdf.py lecture-notes.pdf 1-10 11-20 21-30
```

This creates `chapter1.pdf`, `chapter2.pdf`, and `chapter3.pdf` for the given
page ranges. Chapter titles are not detected automatically—you must provide the
page numbers manually.

