---
name: design-md-builder
description: Build, lint, fix, and export DESIGN.md files — Google's open format for describing a visual identity/design system (colors, typography, spacing, components) to AI coding agents. Use this skill whenever the user wants to create a design system file, a DESIGN.md, a brand style guide for AI agents, wants to define design tokens for their project, mentions "DESIGN.md", "design tokens for agents", or wants to export a design system to Tailwind/DTCG/tokens.json. Also use it if the user has an existing DESIGN.md they want validated, linted, fixed, or updated.
---

# DESIGN.md Builder

Build a `DESIGN.md` file that conforms to Google's open spec (`google-labs-code/design.md`, currently `version: alpha`) — a file describing a design system (design tokens + rationale) for AI coding agents to read and produce UI consistently.

The workflow has 4 fixed steps. Don't skip the lint step — it's what guarantees the file is actually valid per spec, not just "looks right."

## The template

`references/design-md-template.md` is the canonical DESIGN.md: a Material Design 3 role-named system with one font family. **Every new DESIGN.md starts from a copy of it** — don't write the structure from scratch, and read it in full before Step 2. It is the only list of tokens and components; read the names from it instead of from memory, so this skill never drifts from it. What stays fixed:

- **Color tokens are named by role, never by hue.** `primary` and `secondary` each come with `on-*`, `*-container`, `on-*-container`, `*-hover`; `error`, `success`, `warning` with the first three; then neutrals (`background`, `surface`, `surface-container`, `on-surface`, `outline`, `scrim`, ...).
- **Every component value is a `{token}` reference**, one entry per variant or state (`button-primary-hover`, `input-error`, ...). No raw colors or sizes where a token exists.
- **Section order**: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Motion & Micro-interaction, Voice & Content Strategy, Components, Do's and Don'ts. Each section says *which token for which case*, so agents don't invent values.
- **Front matter and prose agree.** The same hex appears in both the front matter and the Colors bullets; change both or neither.

## Step 1 — Ask what the user wants

Only the brand-specific parts of the template change, so ask only for those. If the user already gave them, don't ask again.

Use `AskUserQuestion`, at most 3 questions per call. Ask these three first, since nothing can be built without them:

- **Name** of the design system and its **slug** (folder name under `designs/`). If none, pick a descriptive pair.
- **Primary (brand) color**: an existing brand hex, or let Claude propose one.
- **Anything that should differ from the template**: extra components, a dark theme, an additional brand color, sharper or rounder corners.

Don't ask about these; default silently and say so in the reply, because most users have no opinion: **font** (Roboto, the template's single family; if the user names another, take a Google Fonts family and update every `fontFamily` and the Typography sentence) and **icon set** (Lucide, unless the project already has an icon package installed: detect it, reuse it, and rewrite the icon rule).

## Step 2 — Build the DESIGN.md file

Read `references/spec.md` (the condensed spec) and `references/design-md-template.md` before writing.

1. Copy the template to `designs/<slug>/DESIGN.md`.
2. Replace the `[Design system name]` / `[One-sentence description ...]` placeholders in `name`, `description` and the `#` title, and write the Overview paragraph for this brand.
3. **Rebrand the primary family.** Run `python3 scripts/derive_primary.py "<brand hex>"`. It prints the five tokens (`primary`, `on-primary`, `primary-container`, `on-primary-container`, `primary-hover`) and checks every pair at 4.5:1, the primary on a white surface, and the 30° hue distance from `error`. Paste its values into the front matter **and** the matching Colors bullets. If it exits 1, don't ship the output: tell the user what failed (for example a yellow brand color can't carry white text and sits too close to the error red) and either adjust the color with them or keep the derived values and say which rule is bent. Don't touch neutrals, status colors, shapes or spacing unless the user asked.
4. Apply any font and icon choice (front matter `fontFamily`, Typography prose, Do's and Don'ts).
5. If the user asked for deviations, edit the matching tokens, bullets and prose together so front matter and body never contradict each other. An additional brand color follows the template's Do's rule: M3 name (such as `tertiary`) with all four tokens (`x`, `on-x`, `x-container`, `on-x-container`).
6. New components copy the template's pattern: separate entry per variant/state, `{token}` references only, plus a line in the Components section.
7. Keep the `##` section order and the template's heading names.
8. Add one entry to the `SYSTEMS` array in `index.html`: `{ "slug", "name", "description", "primary" }` with `primary` the hex you set, so `index.html` lists the new system.

Check contrast (4.5:1) for any pair you changed by hand; the script already covers the primary family.

## Step 3 — Lint and self-fix

This step is mandatory — don't eyeball it and assume "probably fine," always run the real linter:

```bash
npx -y @google/design.md lint designs/<slug>/DESIGN.md 2>&1 | grep -v "npm error config prefix"
```

(The line `npm error config prefix cannot be changed...` is harmless sandbox-environment noise, not a real error — always filter it out when reading the output, don't mistake it for a file error.)

The result is JSON with `findings[]` (each finding has a `severity`: `error`/`warning`/`info`) and a `summary`. Handle by severity:

- **`error`** (e.g. `broken-ref` — a token reference pointing to a token that doesn't exist): MUST be fixed immediately with `Edit` — this makes the file invalid.
- **`warning`**: fix if it makes sense (e.g. `missing-primary`, `missing-typography`, `contrast-ratio` below 4.5:1, `section-order` out of sequence, `unknown-key` — possibly a typo like `colours:` instead of `colors:`). Two are expected with the template and are kept deliberately:
  - `token-like-ignored` on `motion`: the linter doesn't know the `motion` key, but the HTML showcase reads it. Keep it and tell the user.
  - `orphaned-tokens` for a color no component uses (for example a reserved status color): keep it and explain, don't force it onto a component.
- **`info`**: reference only (e.g. `token-summary`), no action needed.

After fixing, re-run lint to confirm `errors: 0`. Repeat up to a few times until clean. If any warning is deliberately kept, tell the user why instead of silently ignoring it.

Summarize the lint result briefly for the user (how many errors/warnings were fixed, what was kept and why) — don't paste the raw JSON into the response.

## Step 4 — Export to other formats (only when requested)

Don't do this automatically unless the user asks, or already told you their stack in Step 1 (e.g. "I use Tailwind"). If that signal is there, you can proactively ask a short question like "Want me to export this to a Tailwind config too?" instead of exporting extra files unprompted. The `motion` block is ignored by exports.

Export commands:

```bash
# Tailwind v4 (CSS @theme block) — most common for new projects
npx -y @google/design.md export --format css-tailwind designs/<slug>/DESIGN.md > designs/<slug>/theme.css

# Tailwind v3 (theme.extend JSON, used in tailwind.config.js)
npx -y @google/design.md export --format json-tailwind designs/<slug>/DESIGN.md > designs/<slug>/tailwind.theme.json

# W3C DTCG tokens.json — for Figma Variables / Storybook compatibility
npx -y @google/design.md export --format dtcg designs/<slug>/DESIGN.md > designs/<slug>/tokens.json
```

After exporting, tell the user which file(s) were written — always mention both the original `DESIGN.md` and the export file, not just the export in isolation.

If the user wants to compare against an older version, use the `diff` command:

```bash
npx -y @google/design.md diff DESIGN-v1.md DESIGN-v2.md 2>&1 | grep -v "npm error config prefix"
```

## Important notes

- The format is currently `version: alpha` and may change. If the CLI returns an unexpected error that doesn't match `references/spec.md`, the package has likely been updated; run `npx -y @google/design.md spec --rules` to get the latest spec directly from the CLI instead of trusting the static doc alone.
- No need to install the package beforehand — always use `npx -y @google/design.md ...`, it will fetch from the npm registry automatically.
- If the user only wants to see/understand the spec and doesn't want a file created yet, you can answer directly from `references/spec.md` without running the CLI or creating a file.
- The visual twin of a DESIGN.md is `designs/<slug>/design.html`, built by the `design-system-html-builder` skill. Offer it after the file is lint-clean.
