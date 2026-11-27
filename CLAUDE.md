# CLAUDE.md

Starter template for "vibe coding" — fast, iterative development in conversation with an AI assistant, using short docs that grow step by step instead of a full design written up front. Multi-stack: each sub-project lives in its own `src/<project-name>/` folder, with its source architecture defined under `docs/architecture/`.

## Structure

```text
.claude/             # Assistant config: skills
src/
└── <project-name>/  # One folder per sub-project (e.g. web/, mobile/), per the
                      # architecture in docs/architecture/ — never source directly under src/
docs/                # Core reference documentation — single source of truth, always kept up to date
├── requirement/     # YYYY-MM-DD-task-name.md — raw customer info and ideas, unstructured (stage 1 output)
├── plan/            # 01_plan.md (index: overview, link, status per plan) + YYYY-MM-DD-task-name.intent.md (structured intent, input for every later stage)
├── architecture/    # NEXT_ARCHITECTURE.md, FLUTTER_ARCHITECTURE.md — source architecture per stack
├── specs/           # CODE-feature-name.spec.md (functional spec) + 01_spec.md (overview)
├── api/             # api.md (conventions/index) + endpoints/*.md (one file per endpoint group)
├── database/        # db.md — single shared schema/ERD/migration notes doc for the whole project
├── screens/         # FEATURE-CODE-screen-name-00.screen.md + paired .screen.html prototype + 01_screen.md (overview)
├── design/          # DESIGN.md + design-system.html + theme.css (generated tokens)
├── test/            # CODE-feature-name.testcase.md — AI-generated test cases per feature
└── superpowers/     # Per-task artifacts (superpowers plugin defaults), separate from core docs
    └── plans/       # YYYY-MM-DD-task-name.md — implementation plan (stage 4, Define Plan)
```

### Naming Convention

- `CODE` is a short uppercase identifier for a feature area (e.g. `AUTH`, `PAY`), used consistently across spec ↔ commit.
- Requirement: `docs/requirement/YYYY-MM-DD-task-name.md` — raw, free-format input (customer notes, ideas, tickets, issue reports from Maintain). Nothing here is structured or final.
- Intent: `docs/plan/YYYY-MM-DD-task-name.intent.md` — written by `superpowers:brainstorming` in stage 2 from the requirement file(s). Overrides the skill's default `docs/superpowers/specs/` path. It is the structured input for all later stages, with this fixed structure:

  ```markdown
  # Intent: <task name>
  Source: <links to the docs/requirement/ file(s)>

  ## Problem
  ## Proposed outcome
  ## Affected users and systems
  ## Constraints
  ## Open questions
  ```

- Plan index: `docs/plan/01_plan.md` — one entry per intent file with overview, link, and Status (`Draft` / `Accepted` / `Rejected`). Add the entry as `Draft` right after the intent is written; set `Accepted` or `Rejected` once the user decides.
- Core spec (single source of truth for what a feature does): `docs/specs/CODE-feature-name.spec.md` — only ever created/updated during stage 3 (Design), never written directly at the start of a task.
- Implementation plan: `docs/superpowers/plans/YYYY-MM-DD-task-name.md`, same task name as its intent file. Files stay in place permanently once written — no working/archive move, git history is the record. Each task creates a new dated file rather than editing an old one — history stays linear.
- DB notes: shared `docs/database/db.md`, extended in place per feature (no per-`CODE` file).
- API notes: shared `docs/api/api.md` (conventions/index) + `docs/api/endpoints/*.md` per endpoint group (not per-`CODE`).
- Screen spec: `docs/screens/FEATURE-CODE-screen-name-00.screen.md`, always paired with a same-named `FEATURE-CODE-screen-name-00.screen.html`.
- Test cases: `docs/test/CODE-feature-name.testcase.md` — one per feature, generated from its specs/screens.
- Overview files (`docs/plan/01_plan.md`, `docs/specs/01_spec.md`, `docs/screens/01_screen.md`) are shared indexes that list/summarize the plans, specs, or screens in that folder — updated whenever one is added or changed, not per-task artifacts themselves.

## Develop Instructions

Per feature/task, work through the 7 stages in order. Maintain (stage 7) feeds work back into stage 5 or stage 1.

1. **Requirement**
   - Skill: none — collect by hand (or ask the assistant to save what the user pastes)
   - Output: `docs/requirement/YYYY-MM-DD-task-name.md`
   - Notes: raw customer info and ideas, free format, no structure required. Every task starts here, new feature or change alike.

2. **Plan**
   - Skill: `superpowers:brainstorming`
   - Input: requirement file(s) in `docs/requirement/`
   - Output: `docs/plan/YYYY-MM-DD-task-name.intent.md` (structure in Naming Convention) + a `Draft` entry in `docs/plan/01_plan.md`
   - Notes: restructure the raw requirement into the intent file; never write directly to `docs/specs/` at this stage. Gate: after the user reviews the intent, set its `01_plan.md` entry to `Accepted` (or `Rejected` and stop) and commit — only an `Accepted` plan moves on to stage 3. Override: once the intent is written, stop — do not invoke `superpowers:writing-plans` (the skill's default next step); the next stage is Design, then Build.

3. **Design** (require)
   - Skill: `superpowers:brainstorming` (second pass); `frontend-design` for the UI prototype
   - Input: the `Accepted` intent file, current core docs, `docs/design/` for UI
   - Output: whichever of these sub-steps the task needs, written directly under `docs/` — 3a `architecture/` (source architecture for the sub-project's stack — written in a project's first loop by adapting the closest generic reference already in `docs/architecture/` and confirming it with the user; updated later only when a task changes it), 3b `specs/CODE-feature-name.spec.md` (functional spec) + its `01_spec.md` entry, 3c `screens/FEATURE-CODE-screen-name-00.screen.md` + paired `.screen.html` (UI/UX), 3d `api/`, 3e `database/`
   - Notes: mandatory gate, no exceptions. Start by telling the user which of the docs above this task needs and why, then create only those — a task does not have to touch all of them. Overrides the brainstorming skill's default output: write into the core docs themselves, not into `docs/superpowers/specs/`, and do not invoke `superpowers:writing-plans` afterwards — the next stage is Build (4a). Read the intent file and the current core docs first; confirm every requirement from the intent lands in them and every Open question is answered or explicitly carried forward. Afterwards, review other related core specs to resolve conflicts (overlapping scope, contradictory behavior). Gate: new/changed specs and screens stay `Draft` in `01_spec.md` / `01_screen.md` until the user reviews them; then set them to `Approved` and commit — only then move on to Build.
   - UI notes: must follow `docs/design/DESIGN.md` and `docs/design/design-system.html`. The `.screen.html` prototype is the visual source of truth for that screen — strictly follow it (layout, spacing, states) before writing new UI markup/styles. Render the actual screen's full UI as it appears in the real app (full-viewport, no doc-preview chrome — no outer page header or top bar). All states the screen spec defines (default, loading, error variants, empty, etc.) live on that one real layout, switched via a floating, collapsible panel pinned to a screen corner — not side-by-side duplicate cards.

4. **Build**
   - 4a. **Define Plan** — Skill: `superpowers:writing-plans` (or the `planner` agent). Output: `docs/superpowers/plans/YYYY-MM-DD-task-name.md`, based on the intent file (stage 2) and the design docs (stage 3). Must strictly comply with the architecture file (`docs/architecture/`) matching the sub-project's stack — no deviating from its patterns/structure without confirming first. Screens/UI in the plan must strictly follow the screen's `.screen.html` prototype and the design system (`docs/design/`).
   - 4b. **Implement** — Skill: `superpowers:executing-plans` (or `superpowers:subagent-driven-development` for independent tasks). Output: working code matching the plan. Must strictly comply with the architecture file, the screen's `.screen.html` prototype, `docs/design/design-system.html` and `docs/design/DESIGN.md` for UI — no deviating on architecture patterns/structure, layout, spacing, tokens, or component states without confirming first. Check off the checkbox in the plan file right after finishing each step. If scope diverges, update the docs (see Test stage notes) before moving on.
   - 4c. **Verify** — Skill: `superpowers:verification-before-completion`. Output: build/lint/typecheck passing, confirmed by actually running them.
   - 4d. **Code Review** (require) — Skill: `superpowers:requesting-code-review`. Output: reviewed code with CRITICAL/HIGH findings addressed. MEDIUM/LOW findings are optional per `common/code-review.md`.

5. **Test** (require)
   - 5a. **Generate test cases** — Skill: none dedicated; the assistant writes them from the specs/screens. Output: `docs/test/CODE-feature-name.testcase.md`.
   - 5b. **Run test cases** — Run by the developer (self-test) or by the AI. Output: the executed test cases with results.
   - 5c. **Fix bugs** — Skill: `superpowers:systematic-debugging`. Output: root cause identified and fixed; re-run the affected test cases.
   - Notes: this project overrides `~/.claude/rules/common/testing.md` and `~/.claude/rules/web/testing.md` — no coverage requirement and no committed unit/e2e test suite (deliberate project-level decision, not an oversight); test cases are documents run by the developer or the AI. **If a fix changes what the feature does, update the docs starting from stage 2** (intent file first, then cascade to the design docs) so the chain stays consistent. Wait for the user's explicit confirmation that the feature works before moving to stage 6 — never assume it passed.

6. **Deploy** (require)
   - Skill: the project's own deploy skill (written per project under `.claude/skills/`; the template does not ship one)
   - Output: release
   - Notes: if no deploy skill exists yet, ask the user instead of improvising a deploy. There is no separate merge step in the lifecycle — the deploy skill defines how code reaches the main branch (and release) per `git-conventions`.

7. **Maintain**
   - Skill: none — intake only
   - Notes: receive each new task and route it. A **bug** is first saved as an issue report under `docs/requirement/`, then goes to stage 5 (5c Fix bugs). A **new idea or feature** goes back to stage 1 (save it under `docs/requirement/`).

## Rules

- **Superpowers plugin required (mandatory):** confirm the Superpowers plugin (`superpowers:*` skills) is installed before doing any work.
- Use the `git-conventions` skill for git operations — GitFlow branch model + Conventional Commits.
- Follow the naming convention and folder structure above; don't create new directory structures outside the defined `docs/` layout without confirming first.
- Never read or print production secrets/config files (`.env`, `.env.production`, credentials, API keys, etc.). If a task seems to need one, ask the user instead of reading it directly.
