---
name: write-screen-spec
description: Writes the screen documents for a feature (stage 3c) - one .screen.md spec plus a same-named .screen.html prototype per screen, derived from the feature spec and the design system, and registers each in docs/screens/01_screen.md as Draft. Use when the user asks to design screens, write a screen spec, build a screen prototype or mockup, or when stage 3b is done and 3c starts. Also use when a spec change affects an existing screen. Output is docs/screens/CODE-screen-name-00.screen.md + .screen.html.
license: MIT
---

# Write screen spec

Stage 3c of the workflow in `CLAUDE.md`. The `.screen.md` says what is on the screen and how it behaves; the `.screen.html` is the visual source of truth that stage 4 must follow strictly. Both come from the approved-or-draft spec, never from imagination: every screen element and state traces back to a spec rule.

Use inside the stage 3 brainstorm (`superpowers:brainstorming`); the prototype itself is built with `frontend-design:frontend-design` (step 5). This skill defines what to read, what to write and how to check it.

## Workflow

### 1. Read before writing

Read, in this order: the intent in `docs/plan/`, `docs/specs/CODE-feature-name.spec.md`, the stack's `docs/architecture/*_ARCHITECTURE.md` (routing, component conventions), `docs/design/DESIGN.md`, `docs/design/theme.css`, `docs/design/design-system.html`, existing screens in `docs/screens/` of the same feature, and `docs/api/` if the spec references endpoints.

Stop and tell the user if the spec or any `docs/design/` file is missing: the spec comes from 3b, the design files from the `design-md-builder` and `design-system-html-builder` skills. Do not invent tokens or fall back to the template's placeholder colors.

### 2. Propose the screen list

From the spec, list every distinct user-visible view (page, modal, sheet, empty/blocked variant that has its own layout) and which spec requirements each one covers. A flow of N steps on one view is one screen with states, not N screens. Show the list with the reason for each screen and wait for the user to confirm before writing. Check that every spec requirement and every spec'd error lands on some screen; report the ones that do not.

### 3. Ask only about what the spec cannot answer

Ask about layout intent, copy, or behavior only where the spec is silent and the answer changes the screen (AskUserQuestion when options are clear). Anything the user cannot decide goes to the screen's `Open Questions` and is carried forward, never guessed into the prototype. Do not reopen decisions the spec already made; if the spec looks wrong, say so and send the user back to 3b.

### 4. Write the `.screen.md`

Create `docs/screens/CODE-screen-name-00.screen.md` from `.claude/skills/init-project/templates/screen.md`. That template is the only format; do not invent another. `CODE` is the spec's feature code, `screen-name` is kebab-case, and `-00` is kept from the template (use the next number only for an alternate version of the same screen).

- **Layout:** element tree top to bottom, no styling values; the prototype owns those.
- **Elements:** one row per interactive or data element, with the validation and the API field or spec rule it maps to.
- **States:** one section per state. Cover every error the spec lists that surfaces on this screen, plus Default, Loading and Success where they apply; delete Empty if not applicable. For each error state write the message intent, what is retained or cleared, and where focus goes. Keep wording that must not leak information (for example account existence) exactly as the spec requires.
- **Validation:** client-side convenience only; say the server owns business rules.
- **Accessibility and Responsive:** concrete (labels, roles, live regions, focus order, keyboard; behavior across 320-1920, touch targets), not generic advice.
- **Open Questions:** from step 3. Delete the section if empty.

### 5. Write the `.screen.html`

Invoke the `frontend-design:frontend-design` skill first and build the prototype with it. It supplies the craft (hierarchy, spacing rhythm, typography, designed hover/focus/active states, no templated look); `docs/design/DESIGN.md` and `design-system.html` supply the identity. When they conflict, the design system wins: frontend-design may shape composition and polish within the system, never introduce a new palette, font, radius or component style.

Create the same-named `.screen.html` from `.claude/skills/init-project/templates/screen.html`, following its header rules:

- Render the real screen at full viewport, with no doc-preview chrome.
- Follow `DESIGN.md` strictly (principles, do's and don'ts, component rules). Copy tokens from `docs/design/theme.css`; build every component as shown in `design-system.html`, including its states. No ad-hoc colors, spacing, radii or fonts, and none of the template's placeholder values left over. If the screen needs a component or token the design system lacks, stop and ask the user whether to extend the design system first; do not improvise it in the prototype.
- Every state in the `.screen.md` is one entry in the floating state panel, switching on the one layout via `data-state`. Never duplicate the screen side by side.
- Use semantic HTML, real `label`s, and the ARIA the `.screen.md` states.

### 6. Check, then register

Verify before reporting, with evidence rather than a read-through:

1. Every state heading in the `.screen.md` has a matching button in the panel, and clicking each renders it (open the file in a browser, or at least confirm the `data-state` hooks exist for all of them).
2. No hardcoded color or font outside the `:root` token block: `grep -nE '#[0-9a-fA-F]{3,8}\b|rgb\(' file.screen.html` should only hit `:root`.
3. Components and states match `design-system.html`, and nothing contradicts a `DESIGN.md` rule (list any rule you checked against).
4. Every spec'd error and requirement for this screen appears in Elements or States.

Then add an entry with `Status: Draft` to `docs/screens/01_screen.md`, under its `CODE` heading, using `.claude/skills/init-project/templates/screen-index.md`. Update the entry in place when a screen changes.

### 7. Report

Give the file paths, the spec requirements not yet covered (if any), the carried-forward Open Questions, and the check results. Screens stay `Draft` until the user reviews them; then set `Approved` and commit only when the user asks, following `.claude/rules/git-workflow.md`. Do not start 3d (API) or any build work, and do not edit the spec: if a screen exposes a spec gap, report it and let the user take it back to 3b.
