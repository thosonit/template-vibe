---
name: design-system-html-builder
description: Build a self-contained design.html file (colors, typography, spacing, radius, elevation, motion, every component with its states, contrast checks) from a DESIGN.md design-token file, so other AI coding agents have a rich, visual, copy-pasteable reference for building UI consistent with the brand. Use this skill whenever the user asks to "generate a design system page/site", "visualize my DESIGN.md", "create a design.html", "showcase my design tokens", or wants to add/extend components in an existing design.html. Also use it if the user has an existing design.html they want updated after DESIGN.md changed.
---

# Design System HTML Builder

Generate `designs/<slug>/design.html` — a static, self-contained page that shows every token and component of `designs/<slug>/DESIGN.md`. DESIGN.md is the machine-readable source of truth; this page is its visual twin, so an agent (and a human) can *see* the system before writing UI, which reduces drift.

The page is **not written from scratch**. `references/design-system-template.html` is the canonical page (built from the matching DESIGN.md template of the `design-md-builder` skill). Every new page is a copy of it with the brand-specific values swapped. Read `references/structure-spec.md` first: it lists what is fixed, the DESIGN.md → page mapping, the class vocabulary and the rules for adding a component.

Two modes: **(A) Create new** and **(B) Update / extend** an existing file. If the user points at an existing `design.html`, use B.

## Mode A — Create a new design.html

### Step 1 — Find and read DESIGN.md

- Look in `designs/<slug>/DESIGN.md` (project standard, see `CLAUDE.md`), or the path the user gives. The page is written next to it as `design.html`.
- If it doesn't exist, ask for it, or run the `design-md-builder` skill first. Never invent tokens.
- If DESIGN.md has lint errors (`broken-ref` etc.), tell the user before building: broken tokens make the page render wrong. (One `token-like-ignored` warning on `motion` is expected.)

### Step 2 — Map DESIGN.md onto the template

Read `references/design-system-template.html` in full, then compare it with DESIGN.md:

1. Copy the template to `designs/<slug>/design.html`.
2. Run `python3 scripts/sync_tokens.py designs/<slug>/DESIGN.md designs/<slug>/design.html`. It rewrites everything that is a plain copy of a token: the `:root` vars (colors, spacing, controls, radii, motion, font), the medium/expanded overrides, the Fonts link, `<title>`, brand name, `h1` and the two hero ledes. It also reports what it can't decide: tokens with no CSS variable, color tokens missing from `groups`, `pairs` below 4.5:1, placeholders still in the page. Needs PyYAML (`pip install pyyaml`). Use `--check` to see the report without writing.
3. Do by hand what the script reports and what it doesn't cover (`structure-spec.md` §2): the `.t-*` type classes and type-scale rows, shadows (Elevation levels 2 and 3), the `groups` and `pairs` arrays, the three `.facts` figures other than the font, and the role table.
4. Reconcile the component set: components the template shows but DESIGN.md doesn't define are removed (HTML, CSS, script wiring); components DESIGN.md defines but the template lacks are added by the rules in `structure-spec.md` §4.
5. Update the section ledes, usage lists and Do's and Don'ts so they say the same thing as DESIGN.md's prose.
6. Re-run the script with `--check`: it must report nothing before you move on.

Keep the structure, class names, element ids and script behaviour from the template. If DESIGN.md defines a dark theme, add the `:root[data-theme="dark"]` block (structure-spec §1, Theme); otherwise leave the toggle as is.

### Step 3 — Design judgment only where the template is silent

The template already carries the layout and look. Call `Skill({skill: "frontend-design:frontend-design"})` only for what DESIGN.md defines and the template doesn't cover (a new component, an illustration, an unusual brand personality), and keep that addition in the same tone: same radii, motion and spacing as its neighbours, no new signature element.

### Step 4 — Verify

Follow `structure-spec.md` §5: render it, check the contrast pairs, interactions and motion demos, and widths 320 / 768 / 1280. Fix anything that overflows or reads below 4.5:1 by correcting the token or the usage, not by hardcoding a color.

### Step 5 — Present

Report: the path written, which components were added or removed relative to the template, and any value inferred beyond DESIGN.md and why. Remind the user that the `SYSTEMS` array in `index.html` needs an entry for the system (the `design-md-builder` skill adds it).

## Mode B — Update or extend an existing file

Use when the user says "add component X", "DESIGN.md changed, refresh the page", or similar.

1. Read DESIGN.md and the existing `design.html` (its `:root` vars, class vocabulary, `groups`, `pairs`, `sections`).
2. **DESIGN.md changed:** run `scripts/sync_tokens.py` (it is safe to re-run; it only touches token-driven values), then handle its report and update type rows, shadows, specimens and prose that no longer match.
3. **New component:** follow `structure-spec.md` §4 (CSS next to its group, specimen in the matching group with `.is-*` state classes, behaviour in the existing IIFE, new pairs added to `pairs`). If it needs a token DESIGN.md lacks, ask: use the closest existing token, or update DESIGN.md first (and re-lint through `design-md-builder`).
4. Edit with `Edit`, never rebuild the file. Re-run the checks in `structure-spec.md` §5 for the touched area.
5. Report what changed and where.

## Notes

- The page keeps its one `<script>` for the section nav, theme toggle, live contrast, motion demos and dialog. That JS exists to demonstrate real states, so keep it; don't add behaviour beyond what a component needs.
- The Lucide icon sprite is part of the template. If DESIGN.md names a different icon set, replace the sprite symbols with that set's equivalents under the same ids.
- `CLAUDE.md` makes this file the visual reference for UI work, so keep it accurate rather than approximate.
