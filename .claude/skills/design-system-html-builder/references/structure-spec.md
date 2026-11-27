# Structure & conventions for `design.html`

`references/design-system-template.html` is the canonical page, built from the DESIGN.md template of the `design-md-builder` skill (`references/design-md-template.md`). Every new `design.html` is a **copy of it with the brand-specific values swapped**, never a page written from scratch. This document says what is fixed, what changes per brand, and how to extend it.

## 1. Fixed (keep as is)

**Page frame**
- `<html lang="en" data-theme="light">`, one `<style>`, one `<script>` (an IIFE at the end of `<body>`), no external framework. Only the Google Fonts `<link>` is external, and only for the font DESIGN.md names.
- Sticky `.topbar`: `.brand`, the theme toggle `#theme-toggle` (a `.btn.icon`), and `nav.nav-inline#inline-nav` for small screens. Then `.wrap.page` = sticky sidebar `aside.side` with `nav.nav#side-nav` (wide screens) + `<main>`. Both navs are filled by JS from the `sections` array.
- A hidden SVG sprite of Lucide icons: `i-check i-x i-info i-ok i-warn i-err i-bell i-user i-loader i-chevron-left i-chevron-right i-sun i-moon`, used as `<svg class="i"><use href="#i-..."/></svg>`.
- Section ids in DESIGN.md order: `overview colors typography layout elevation shapes motion voice components rules`. Each is `<section id aria-labelledby="h-...">` with a heading, a `p.lede` that states the rule (the same rule as the DESIGN.md prose), then specimens. **No numbered section labels.**
- `#components` holds groups (`.group` = `h3.t-title-md` + specimens + a closing `p.lede` of usage rules): `#buttons #inputs #selection #content #feedback #progress #links #navigation #overlays #icons`.

**Behaviour in the script (keep the ids and data attributes it reads)**
- `#color-groups` and `#pairs` are built from the `groups` and `pairs` arrays; `[data-hex]` shows each token's value; `[data-pair]` shows each pair's live contrast ratio ("passes AA" at 4.5:1 or better).
- `#side-nav`, `#inline-nav`, driven by `sections`; the current section gets `aria-current`.
- `#theme-toggle` flips `aria-pressed` and `data-theme` on `<html>`.
- `[data-play]` / `[data-demo]` run the motion demos with the durations and easings read from the `--dur-*` and `--ease-*` vars.
- `[data-open]` opens the `<dialog>` with that id (`#dlg`); clicking the backdrop closes it.

**Theme**
- The template defines **no dark values**: the toggle only changes `data-theme`. If DESIGN.md defines a dark theme, add a `:root[data-theme="dark"]` block that redefines the color vars (and shadows if needed); components must not branch on theme. If DESIGN.md has none, leave the toggle as the template has it. There is no primary-color picker.

## 2. DESIGN.md → page mapping (what you change)

`scripts/sync_tokens.py` applies every row marked *(script)* and reports the rest; the other rows are by hand.

| In the page | Comes from DESIGN.md |
|---|---|
| *(script)* `:root` color vars (`--primary`, `--on-primary`, `--surface-container`, ...) | `colors` front matter, same key names (`--<key>`) |
| *(script)* `--space-*`, `--control-*`, `--icon-*`, `--gutter`, `--margin`, `--columns` | `spacing` (the `medium` and `expanded` overrides feed the "Grid by window size" table) |
| *(script)* `--r-*` | `rounded` |
| `--shadow-2`, `--shadow-3` | Elevation & Depth levels 2 and 3 |
| *(script)* `--dur-<name>`, `--ease-<name>` for `state-change`, `surface-enter`, `surface-exit` | `motion` front matter |
| *(script)* `--font` and the Fonts `<link>` | `typography.*.fontFamily` and the Typography prose |
| `.t-display-lg`, `.t-headline-lg|md`, `.t-title-lg|md`, `.t-body-lg|md|sm`, `.t-label-lg|md` and the type-scale rows | `typography` tokens (size, weight, line height, letter spacing) and the Typography prose |
| `groups` array (color swatches) | the Colors bullets, grouped as in the template |
| `pairs` array | every on-color/background pair plus text-on-surface pairs DESIGN.md relies on |
| Role table "Which token for which case" and `.lede` rules | the Colors, Layout, Elevation, Shapes bullets |
| `.btn`, `.input`, `.chip`, `.card`, `.list-item`, `.alert`, `.progress`, `.crumbs`, `.pg`, ... | `components` entries and the Components prose. Values come from the same tokens, no raw hex |
| *(script)* Brand name (`.brand`, `<title>`, `h1`), description, hero copy and the three `.facts` | DESIGN.md `name`, `description`, Overview prose and its main rules (font, touch target, contrast) |
| Motion and Voice sections | the Motion & Micro-interaction and Voice & Content Strategy prose |

If DESIGN.md lacks a value the page needs, do not invent one: ask, or derive it from an existing token and say so in the closing message.

## 3. Class vocabulary (reuse, don't add parallels)

- **Layout:** `.wrap`, `.page`, `.group`, `.grid`, `.row`, `.stack` (`.tight`), `.lede`, `.card`, `.scroll-x`, `.table-simple`, `.window-grid`.
- **Type:** `.t-display-lg`, `.t-headline-lg|md`, `.t-title-lg|md`, `.t-body-lg|md|sm`, `.t-label-lg|md`.
- **Controls:** `.btn` + `primary|secondary|icon`, `.link`, `.field`, `.input`, `.check`, `.option-list`.
- **Content and feedback:** `.chip`, `.list` / `.list-item`, `.card` (+ `.card-title`, `.card-desc`, `.card-foot`), `.alert` + `success|warning|error`, `.progress`, `.spinner`, `.divider`.
- **Navigation and overlays:** `.crumbs`, `.pager` / `.pg` / `.pg-gap`, `<dialog class="dialog">`, `.dialog-static`, `.scrim-layer`.
- **Specimens and docs:** `.swatch`, `.chips-grid`, `.pairs` / `.pair`, `.type-row`, `.space-row`, `.space-bar`, `.shape-grid`, `.shape`, `.elev`, `.motion-grid`, `.demo-tile`, `.demo-stage`, `.stage-box`, `.rules`, `.variant`, `.spec-note`.
- **State demos:** `.is-hover`, `.is-pressed`, `.is-focus`, `.is-loading`, `.is-selected` render a state statically, so every state shows without interaction.

## 4. Adding or removing a component

1. Read DESIGN.md for the component's tokens. A missing token is a question to the user, not an invention.
2. Add CSS at the end of the existing `<style>`, next to the block for its group, using only `var(--token)` values.
3. Add the specimen to the matching `.group` in `#components` (or a new `.group` with its own id before `#icons`), showing the real states with the `.is-*` classes, a short `p.lede` rule, and an `aria-label` or visible label for every control.
4. Wire any behaviour into the existing IIFE; never add a second `<script>` or `<style>`.
5. If the component adds a color pair, add it to `pairs` so its contrast is measured.
6. Components DESIGN.md does not define are removed from the page along with their CSS and script wiring, so the page never shows something DESIGN.md can't back.

## 5. Checks before finishing

- Serve the repo (`python3 -m http.server`) or open the file, and confirm: the sidebar lists every section and highlights the one in view; every contrast pair shows "passes AA"; the theme toggle works without breaking layout; the dialog opens and closes; the motion demos play; with `prefers-reduced-motion` the enter/exit demos do not animate.
- At 320, 768 and 1280px nothing overflows horizontally.
- No leftover template content: `[Design system name]`, the template's description and the Roboto/40px/WCAG facts are replaced or still true for this brand; sample content is deliberately neutral.
