# PDF Template

Reusable presentation-style PDF template built with Vivliostyle.

## Structure

- `src/manuscript/pack.md`: example PDF pages.
- `src/styles/pack.css`: page layout and print styling.
- `Design.md`: plain grayscale design direction and CSS variable reference.
- `src/assets/images/image.png`: placeholder image used by the example pages.
- `scripts/build.py`: builds the full PDF and optimized PDF variants.
- `scripts/optimize_pdf.py`: compresses images inside a built PDF.
- `dist/`: generated PDF outputs.

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

The local preview uses `index.html`, which mirrors the sample pages from `src/manuscript/pack.md` and uses the placeholder image in `src/assets/images/image.png`.

## Build

Run the full build:

```sh
npm run build
```

This creates:

- `dist/template-pack.pdf`
- `dist/template-pack-q60.pdf`
- `dist/template-pack-q72.pdf`
- `dist/template-pack-q85.pdf`

The `q60`, `q72`, and `q85` files are PDF-level optimized variants. Source images remain unchanged in `src/assets/`.

## Other Commands

Build only the full PDF:

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

Replace the sample copy in `src/manuscript/pack.md`, update the theme in `src/styles/pack.css`, and keep source imagery in `src/assets/`.
