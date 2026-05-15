# Design

## Direction

Plain grayscale presentation PDF template.

The default design should feel neutral, reusable, and content-first. It should not depend on brand colour, decorative gradients, or project-specific visual language.

## Palette

- `--page-background`: near black page background.
- `--panel-background`: dark gray content block background.
- `--image-background`: black image background.
- `--text-primary`: white primary text.
- `--text-secondary`: light gray supporting text.
- `--text-muted`: mid gray labels and metadata.
- `--accent`: white emphasis colour.
- `--accent-muted`: light gray secondary emphasis colour.

## Layout

- Widescreen landscape pages: `13.333in` by `7.5in`.
- Full-bleed dark page background.
- `--page-width`: `13.333in` fixed PDF page width.
- `--page-height`: `7.5in` fixed PDF page height.
- `--page-gutter-block`: `0.55in` top and bottom page gutter.
- `--page-gutter-inline`: `0.68in` left and right page gutter.
- `--overview-gap`: `0.2in` spacing between overview blocks.
- `--feature-gap`: `0.58in` spacing between feature copy and image.
- `--content-block-padding`: `0.2in` padding inside repeated content blocks.
- Simple cover, overview grid, feature page, and closing page examples.
- Repeated content blocks are plain filled surfaces with no visible border.
- Local browser preview scales the whole fixed page proportionally.
- Example imagery uses the placeholder image in `src/assets/images/image.png`.

## Typography

- Sans-serif system stack.
- Large cover title, medium section headings, compact card headings.
- Letter spacing stays at `0` except uppercase kicker labels.

## Output

- Main PDF: `dist/template-pack.pdf`.
- Optimized variants: `dist/template-pack-q60.pdf`, `dist/template-pack-q72.pdf`, and `dist/template-pack-q85.pdf`.
