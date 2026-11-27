# Vibe Template

## 1. Overview

Starter template for **vibe coding**: build software through fast, iterative conversation with an AI assistant, using short docs that grow step by step. Work follows a 7-stage SDLC and loops back through Maintain. Requires the Superpowers plugin. 

## 2. Folder Structure

```text
.claude/             # Skills
src/<project-name>/  # One folder per sub-project (web/, mobile/), per docs/architecture/
docs/                # Single source of truth
├── requirement/     # Raw customer info and ideas
├── plan/            # 01_plan.md index + *.intent.md
├── architecture/    # Source architecture per stack
├── specs/           # CODE-feature-name.spec.md + 01_spec.md
├── api/             # api.md + endpoints/*.md
├── database/        # db.md
├── screens/         # FEATURE-CODE-screen-name-00.screen.md + .screen.html + 01_screen.md
├── design/          # DESIGN.md, design-system.html, theme.css
├── test/            # CODE-feature-name.testcase.md
└── superpowers/plans/  # YYYY-MM-DD-task-name.md (implementation plan)
```

## 3. SDLC

### One-time setup

1. **CLAUDE.md** — project overview, structure, conventions.
2. **Git convention** — GitFlow + Conventional Commits (`git-conventions`).
3. **Design system** — `docs/design/DESIGN.md`, `docs/design/design-system.html`.

### Per feature / task

Each stage ends by committing the artifact the next stage reads.

| Stage                                          | Step                      | Skill                                          | Input                                        | Output                                                                                              |
| ---------------------------------------------- | ------------------------- | ---------------------------------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **1. Requirement**                             | Collect                   | — (manual)                                     | customer info, ideas, tickets, bug reports   | `docs/requirement/YYYY-MM-DD-task-name.md`                                                          |
| **2. Plan**                                    | Brainstorm intent         | `superpowers:brainstorming`                    | requirement files                            | `docs/plan/YYYY-MM-DD-task-name.intent.md` + `01_plan.md` entry (`Draft` → `Accepted` / `Rejected`) |
| **3. Design** (require, `Accepted` plans only) | 3a. Architecture          | `superpowers:brainstorming`                    | `Accepted` intent, core docs                 | `docs/architecture/<STACK>_ARCHITECTURE.md`                                                         |
|                                                | 3b. Spec                  | `superpowers:brainstorming`                    | `Accepted` intent, core docs                 | `docs/specs/CODE-feature-name.spec.md` + `01_spec.md` entry                                         |
|                                                | 3c. Screens               | `superpowers:brainstorming`, `frontend-design` | spec, `docs/design/`                         | `docs/screens/FEATURE-CODE-screen-name-00.screen.md` + `.screen.html`                               |
|                                                | 3d. API                   | `superpowers:brainstorming`                    | spec                                         | `docs/api/api.md`, `docs/api/endpoints/*.md`                                                        |
|                                                | 3e. Database              | `superpowers:brainstorming`                    | spec                                         | `docs/database/db.md`                                                                               |
| **4. Build**                                   | 4a. Define Plan           | `superpowers:writing-plans`                    | intent, design docs                          | `docs/superpowers/plans/YYYY-MM-DD-task-name.md`                                                    |
|                                                | 4b. Implement             | `superpowers:executing-plans`                  | plan, architecture, prototype, design system | working code                                                                                        |
|                                                | 4c. Verify                | `superpowers:verification-before-completion`   | code                                         | build/lint/typecheck pass                                                                           |
|                                                | 4d. Code Review (require) | `superpowers:requesting-code-review`           | diff, plan, docs                             | CRITICAL/HIGH findings fixed                                                                        |
| **5. Test** (require)                          | 5a. Generate cases        | `generate-testcases`                           | specs, screens                               | `docs/test/CODE-feature-name.testcase.md`                                                           |
|                                                | 5b. Run cases             | developer or AI                                | code, test cases                             | results; user confirms the feature works                                                            |
|                                                | 5c. Fix bugs              | `superpowers:systematic-debugging`             | failing cases                                | root cause fixed; if docs must change, restart from stage 2                                         |
| **6. Deploy** (require)                        | Deploy                    | the project's own deploy skill                 | code the user confirmed                      | release                                                                                             |
| **7. Maintain**                                | Intake                    | —                                              | bug report, new idea or feature              | bug → save in `docs/requirement/`, then 5c; idea or feature → stage 1                               |

Notes:

- Stages 2 and 3 stop after writing their files; don't hand off to `writing-plans` (that is 4a).
- Stage 3 does only the sub-steps the task needs; 3a is written in a project's first loop.
- Specs and screens stay `Draft` in `01_spec.md` / `01_screen.md` until the user approves them (`Approved`); then Build starts.
- Merge / PR is outside the flow; the deploy skill decides how code reaches `main`.

## 4. Skills

Status: ✅ available · 🚧 not yet created.

### Repo skills (`.claude/skills/`)

| Skill                        | Stage    | Purpose                                                                 | Status |
| ---------------------------- | -------- | ----------------------------------------------------------------------- | ------ |
| `init-project`               | Setup    | Confirm the system and stacks, record them in CLAUDE.md                 | ✅     |
| `git-conventions`            | Setup, 6 | GitFlow branches + Conventional Commits                                 | ✅     |
| `design-md-builder`          | Setup, 3c | Build / lint `docs/design/DESIGN.md`                                   | ✅     |
| `design-system-html-builder` | Setup, 3c | Build `design-system.html` from DESIGN.md                              | ✅     |
| `scaffold-nextjs-app`        | 3a, 4    | Next.js architecture doc + project skeleton                             | ✅     |
| `scaffold-flutter-app`       | 3a, 4    | Flutter architecture doc + project skeleton                             | ✅     |
| `flutter-dart-code-review`   | 4d       | Flutter/Dart review checklist                                           | ✅     |
| `capture-requirement`        | 1, 7     | Save raw info or bug reports to `docs/requirement/YYYY-MM-DD-task-name.md` | 🚧  |
| `write-spec`                 | 3b       | `CODE-feature-name.spec.md` from template + `01_spec.md` entry          | 🚧     |
| `write-screen-spec`          | 3c       | `.screen.md` + `.screen.html` prototype with state-switch panel         | 🚧     |
| `write-api-db-docs`          | 3d, 3e   | Update `docs/api/` and `docs/database/db.md` from the spec              | 🚧     |
| `generate-testcases`         | 5a       | `CODE-feature-name.testcase.md` from specs and screens                  | ✅     |
| `nextjs-code-review`         | 4d       | Next.js review checklist (counterpart of the Flutter one)               | 🚧     |
| `deploy`                     | 6        | Written per project; the template does not ship one                     | 🚧     |

### External skills (plugin / global)

| Skill                                                                                                                                                          | Stage            | Purpose                                         | Status |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------- | ------ |
| `superpowers:*` (`brainstorming`, `writing-plans`, `executing-plans`, `verification-before-completion`, `requesting-code-review`, `systematic-debugging`) | 2, 3, 4, 5       | Core workflow skills; Superpowers plugin required | ✅   |
| `frontend-design`                                                                                                                                              | 3c               | Distinctive UI for screen prototypes            | ✅     |
| `review-spec-docs`                                                                                                                                             | 3 (before approval) | Review the spec set for gaps and consistency | ✅     |

## 5. Rules

- `docs/` is the **single source of truth**: read it before any change and update it the moment something changes.
