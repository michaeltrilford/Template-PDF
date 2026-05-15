#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
FULL_PDF = DIST / "template-pack.pdf"
QUALITIES = (60, 72, 85)


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def vivliostyle_command() -> list[str]:
    env_cli = os.environ.get("VIVLIOSTYLE_CLI")
    if env_cli:
        return ["node", env_cli]

    local_cli = ROOT / "node_modules/@vivliostyle/cli/dist/cli.js"
    if local_cli.exists():
        return ["node", str(local_cli)]

    bin_cli = shutil.which("vivliostyle")
    if bin_cli:
        return [bin_cli]

    raise SystemExit("Vivliostyle CLI not found. Run `npm install` or set VIVLIOSTYLE_CLI.")


def build_full_pdf() -> None:
    FULL_PDF.parent.mkdir(parents=True, exist_ok=True)
    run([*vivliostyle_command(), "build", "-o", str(FULL_PDF.relative_to(ROOT))])


def optimize(quality: int) -> None:
    run(
        [
            sys.executable,
            str(Path(__file__).with_name("optimize_pdf.py")),
            "--input",
            str(FULL_PDF.relative_to(ROOT)),
            "--output",
            str((DIST / f"template-pack-q{quality}.pdf").relative_to(ROOT)),
            "--quality",
            str(quality),
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the template PDF and optimized PDF variants.")
    parser.add_argument(
        "--quality",
        type=int,
        choices=QUALITIES,
        help="Only build one optimized variant after the full PDF.",
    )
    args = parser.parse_args()

    build_full_pdf()

    qualities = (args.quality,) if args.quality else QUALITIES
    for quality in qualities:
        optimize(quality)


if __name__ == "__main__":
    main()
