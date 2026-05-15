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
FULL_PDF = DIST / "base/template-pack.pdf"
QUALITIES = (60, 72, 85)

PROFILES = {
    "base": {
        "pages": None,
        "folder": DIST / "base",
        "basename": "template-pack",
    },
    "version-a": {
        "pages": "1-2,4",
        "folder": DIST / "version-a",
        "basename": "template-pack-version-a",
    },
    "version-b": {
        "pages": "1,3,4",
        "folder": DIST / "version-b",
        "basename": "template-pack-version-b",
    },
}


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


def optimize(source: Path, output: Path, quality: int) -> None:
    run(
        [
            sys.executable,
            str(Path(__file__).with_name("optimize_pdf.py")),
            "--input",
            str(source.relative_to(ROOT)),
            "--output",
            str(output.relative_to(ROOT)),
            "--quality",
            str(quality),
        ]
    )


def optimize_variants(source: Path, folder: Path, basename: str, qualities: tuple[int, ...]) -> None:
    for quality in qualities:
        optimize(source, folder / f"{basename}-q{quality}.pdf", quality)


def build_profile(profile_name: str, qualities: tuple[int, ...]) -> None:
    profile = PROFILES[profile_name]
    folder = profile["folder"]
    basename = profile["basename"]
    output = folder / f"{basename}.pdf"
    folder.mkdir(parents=True, exist_ok=True)

    if profile["pages"] is None:
        output = FULL_PDF
    else:
        run(
            [
                sys.executable,
                str(Path(__file__).with_name("curate_pdf.py")),
                "--input",
                str(FULL_PDF.relative_to(ROOT)),
                "--output",
                str(output.relative_to(ROOT)),
                "--pages",
                profile["pages"],
            ]
        )

    optimize_variants(output, folder, basename, qualities)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the base template PDF and curated output profiles.")
    parser.add_argument(
        "profile",
        nargs="?",
        default="all",
        help="Use 'all' for every output folder or a profile name.",
    )
    parser.add_argument(
        "--quality",
        type=int,
        choices=QUALITIES,
        help="Only build one optimized variant for each selected profile.",
    )
    args = parser.parse_args()

    if args.profile != "all" and args.profile not in PROFILES:
        valid = ", ".join(["all", *PROFILES.keys()])
        raise SystemExit(f"Unknown build profile '{args.profile}'. Valid profiles: {valid}")

    build_full_pdf()

    qualities = (args.quality,) if args.quality else QUALITIES
    if args.profile == "all":
        for profile_name in PROFILES:
            build_profile(profile_name, qualities)
    else:
        build_profile(args.profile, qualities)


if __name__ == "__main__":
    main()
