# PDF Template

Reusable presentation-style PDF template built with Vivliostyle.

## Quick Start: Vibe

This repo has enough context for Codex or similar tools to get the template running for you. Download the ZIP from the GitHub `Code` dropdown, add it to Codex or a similar tool, and ask it to run the repo. From there, you can start prompting changes or craft the files yourself.

The rest of this README is technical setup and reference. You do not need to understand all of it to use the template.

## Quick Start: Code

```sh
npm install
python3 -m pip install -r requirements.txt
npm run dev
```

Then open `http://127.0.0.1:13003`.

## Structure

- `src/manuscript/pack.md`: example PDF pages.
- `src/styles/pack.css`: page layout and print styling.
- `Design.md`: plain grayscale design direction and CSS variable reference.
- `src/assets/images/image.jpg`: placeholder image used by the example pages.
- `scripts/build.py`: builds the base PDF, curated output profiles, and optimized variants.
- `scripts/curate_pdf.py`: creates curated PDFs from selected pages of the base PDF.
- `scripts/optimize_pdf.py`: compresses images inside a built PDF.
- `dist/`: generated PDF outputs.

## Working With IDE

- Craft the sample pages in `src/manuscript/pack.md`.
- Adjust foundational tokens and layout rules in `src/styles/pack.css`.
- Add source images in `src/assets/` and reference them from the manuscript.

## Working With Codex

If working with Codex, it can help to set the foundation with a `Design.md` that informs the CSS variables and theme in `src/styles/pack.css`. It is not required, but it is useful context when asking Codex to create or adjust a PDF theme.

Codex is also useful for mapping curated assets into `src/manuscript/pack.md`, iterating against the localhost preview, opening the generated PDF, and rebuilding the final output when the layout is ready.

## Install

Install the project dependencies first:

```sh
npm install
python3 -m pip install -r requirements.txt
```

## Local Preview

Run the local preview server:

```sh
npm run dev
```

Then open `http://127.0.0.1:13003`.

The local preview uses `index.html`, which mirrors the sample pages from `src/manuscript/pack.md` and uses the placeholder image in `src/assets/images/image.jpg`.

## Build

Run the full build:

```sh
npm run build
```

This creates:

- `dist/base/template-pack.pdf`
- `dist/version-a/template-pack-version-a.pdf`
- `dist/version-b/template-pack-version-b.pdf`

Each output folder also includes `-q60`, `-q72`, and `-q85` PDF-level optimized variants. Source images remain unchanged in `src/assets/`.

## Curated Versions

The template builds one base PDF first, then creates curated versions by copying selected pages into separate folders. This is useful when one source document needs different exports for different readers, contexts, or levels of detail.

Output profiles are configured in `scripts/build.py` in the `PROFILES` map:

- `base`: the full source PDF.
- `version-a`: generic example version using pages `1-2,4`.
- `version-b`: generic example version using pages `1,3,4`.

Rename `version-a` and `version-b` to match your own use case. For example, a resume might use audience-specific versions, while a proposal might use short, detailed, or appendix-heavy versions.

Build a single profile:

```sh
npm run build -- version-a
npm run build -- version-b
```

To add a new version, add another profile:

```py
"proposal": {
    "pages": "1,3-4",
    "folder": DIST / "proposal",
    "basename": "template-pack-proposal",
},
```

Use `pages: None` only for the full base PDF. Curated outputs should list the pages to copy from `dist/base/template-pack.pdf`.

## Other Commands

Build only the base PDF:

```sh
npm run build:pdf
```

Create the default optimized PDF from an existing full PDF:

```sh
npm run optimize
```

Create the smaller optimized PDF:

```sh
npm run optimize:small
```

## Notes

`dist/` is generated output and is ignored by git by default.
