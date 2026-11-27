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
| **5. Test** (require)                          | 5a. Generate cases        | AI (no dedicated skill)                        | specs, screens                               | `docs/test/CODE-feature-name.testcase.md`                                                           |
|                                                | 5b. Run cases             | developer or AI                                | code, test cases                             | results; user confirms the feature works                                                            |
|                                                | 5c. Fix bugs              | `superpowers:systematic-debugging`             | failing cases                                | root cause fixed; if docs must change, restart from stage 2                                         |
| **6. Deploy** (require)                        | Deploy                    | the project's own deploy skill                 | code the user confirmed                      | release                                                                                             |
| **7. Maintain**                                | Intake                    | —                                              | bug report, new idea or feature              | bug → save in `docs/requirement/`, then 5c; idea or feature → stage 1                               |

Notes:

- In stages 2 and 3, brainstorming must not hand off to `writing-plans`: stop after writing the files above; the plan is written in 4a.
- Stage 3: a task only does the sub-steps it needs, not all of 3a–3e.
- Specs and screens stay `Draft` in `01_spec.md` / `01_screen.md` until the user approves them (`Approved`); Build starts after that.
- Architecture is written in a project's first loop, from the closest generic reference, and confirmed by the user.
- Merge / PR is outside the flow; the deploy skill decides how code reaches the main branch.

## 4. Rules

- `docs/` is the **single source of truth**: read it before any change and update it the moment something changes.
