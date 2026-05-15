# Design

## Direction

Plain grayscale presentation PDF template.

The default design should feel neutral, reusable, and content-first. It should not depend on brand colour, decorative gradients, or project-specific visual language.

## Color Tokens

- `--page-background`: near black page background.
- `--panel-background`: dark gray content block background.
- `--image-background`: black image background.
- `--text-primary`: white primary text.
- `--text-secondary`: light gray supporting text.
- `--text-muted`: mid gray labels and metadata.
- `--accent`: white emphasis colour.
- `--accent-muted`: light gray secondary emphasis colour.
- `--preview-border`: gray browser-preview-only page border.

## Page Tokens

- Widescreen landscape pages: `13.333in` by `7.5in`.
- Full-bleed dark page background.
- `--page-width`: `13.333in` fixed PDF page width.
- `--page-height`: `7.5in` fixed PDF page height.
- `--page-gutter-block`: `0.55in` top and bottom page gutter.
- `--page-gutter-inline`: `0.68in` left and right page gutter.

## Layout Tokens

- `--content-width-xl`: cover title measure.
- `--content-width-l`: intro text measure.
- `--content-width-m`: section heading measure.
- `--feature-copy-width`: feature page copy column.
- `--feature-image-width`: maximum feature image width.
- `--feature-image-height`: maximum feature image height.
- `--image-board-height`: minimum feature image board height.
- `--overview-columns`: overview grid column count.
- `--principles-columns`: closing grid column count.
- `--radius-none`: square corners for the base template.

## Spacing Tokens

- `--space-xs`: smallest vertical spacing.
- `--space-s`: compact heading spacing.
- `--space-base`: list item spacing.
- `--space-m`: default block padding and related text spacing.
- `--space-ml`: medium-large grid spacing.
- `--space-l`: feature list top spacing.
- `--space-xl`: overview grid top spacing.
- `--space-2xl`: feature page column gap.
- `--space-xxl`: closing grid top spacing.
- `--block-min-height`: minimum repeated block height.

## Template Layout

- Simple cover, overview grid, feature page, and closing page examples.
- Repeated content blocks are plain filled surfaces with no visible border.
- Local browser preview scales the whole fixed page proportionally.
- Example imagery uses the placeholder image in `src/assets/images/image.jpg`.

## Typography Tokens

- `--font-family`: sans-serif system stack.
- `--font-size-heading-xl`: cover title size.
- `--font-size-heading-l`: section heading size.
- `--font-size-heading-m`: supporting heading size.
- `--font-size-body-l`: base document body size.
- `--font-size-body-m`: normal copy size.
- `--font-size-body-s`: compact list copy size.
- `--font-size-body-xs`: repeated block copy size.
- `--font-size-label-m`: metadata label size.
- `--font-size-label-s`: uppercase label size.
- `--line-height-heading-tight`: cover title line-height.
- `--line-height-heading`: heading line-height.
- `--line-height-body`: base line-height.
- `--line-height-body-tight`: supporting heading line-height.
- `--line-height-body-compact`: compact copy line-height.
- `--font-weight-regular`: normal copy weight.
- `--font-weight-bold`: heading, label, and marker weight.
- `--letter-spacing-normal`: default letter spacing.
- `--letter-spacing-label`: uppercase label letter spacing.

## Preview Tokens

- `--preview-page-gap`: browser preview spacing between pages.
- `--preview-page-padding`: browser preview padding around pages.
- `--preview-border-width`: browser preview page border width.

## Output

- Base PDF: `dist/base/template-pack.pdf`.
- Curated versions: configured in `scripts/build.py`.
- Optimized variants: `-q60`, `-q72`, and `-q85` files inside each output folder.
