#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def parse_pages(value: str) -> list[int]:
    pages: list[int] = []
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = [int(item) for item in part.split("-", 1)]
            pages.extend(range(start, end + 1))
        else:
            pages.append(int(part))
    return pages


def curate_pdf(source: Path, output: Path, pages: list[int]) -> None:
    reader = PdfReader(str(source))
    writer = PdfWriter()

    page_count = len(reader.pages)
    for page_number in pages:
        if page_number < 1 or page_number > page_count:
            raise SystemExit(f"Page {page_number} is outside the source range 1-{page_count}")
        writer.add_page(reader.pages[page_number - 1])

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as pdf_file:
        writer.write(pdf_file)

    print(f"Curated {source} pages {pages} -> {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a curated PDF from selected pages.")
    parser.add_argument("--input", default="dist/base/template-pack.pdf", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--pages", required=True, type=parse_pages)
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input PDF not found: {args.input}")

    curate_pdf(args.input, args.output, args.pages)


if __name__ == "__main__":
    main()
