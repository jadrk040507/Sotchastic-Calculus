import sys
from typing import List, Tuple

try:
    from PyPDF2 import PdfReader, PdfWriter
except ModuleNotFoundError:
    sys.stderr.write("PyPDF2 is required to run this script.\n")
    raise


def parse_ranges(args: List[str]) -> List[Tuple[int, int]]:
    ranges = []
    for arg in args:
        try:
            start, end = map(int, arg.split('-'))
        except ValueError:
            raise ValueError(f"Invalid page range: {arg}")
        if start < 1 or end < start:
            raise ValueError(f"Invalid page range: {arg}")
        ranges.append((start, end))
    return ranges


def split_pdf(src: str, ranges: List[Tuple[int, int]], output_prefix: str = "chapter") -> None:
    reader = PdfReader(src)
    for i, (start, end) in enumerate(ranges, 1):
        writer = PdfWriter()
        for p in range(start - 1, min(end, len(reader.pages))):
            writer.add_page(reader.pages[p])
        out_name = f"{output_prefix}{i}.pdf"
        with open(out_name, "wb") as f:
            writer.write(f)
        print(f"Wrote {out_name}")


def main(argv: List[str]) -> None:
    if len(argv) < 3:
        print("Usage: python split_pdf.py input.pdf start-end [start-end ...]")
        print("Example: python split_pdf.py lecture-notes.pdf 1-10 11-20")
        return
    src = argv[1]
    ranges = parse_ranges(argv[2:])
    split_pdf(src, ranges)


if __name__ == "__main__":
    main(sys.argv)
