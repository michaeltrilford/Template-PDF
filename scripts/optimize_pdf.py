#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def human_size(size: int) -> str:
    value = float(size)
    for unit in ("B", "KB", "MB"):
        if value < 1024 or unit == "MB":
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{size} B"


def optimize_pdf(source: Path, output: Path, quality: int) -> None:
    reader = PdfReader(str(source))
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)

    image_count = 0
    for page in writer.pages:
        for image_file in page.images:
            image = image_file.image
            if image.mode != "RGB":
                image = image.convert("RGB")

            image_file.replace(image, quality=quality, optimize=True)
            image_count += 1

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as pdf_file:
        writer.write(pdf_file)

    print(
        f"Optimized {image_count} images: "
        f"{source} ({human_size(source.stat().st_size)}) -> "
        f"{output} ({human_size(output.stat().st_size)})"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a compressed copy of a built PDF without changing source assets."
    )
    parser.add_argument("--input", default="dist/base/template-pack.pdf", type=Path)
    parser.add_argument("--output", default="dist/base/template-pack-q85.pdf", type=Path)
    parser.add_argument("--quality", default=85, type=int)
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input PDF not found: {args.input}")
    if not 1 <= args.quality <= 100:
        raise SystemExit("--quality must be between 1 and 100")

    optimize_pdf(args.input, args.output, args.quality)


if __name__ == "__main__":
    main()
