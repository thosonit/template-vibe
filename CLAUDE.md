# CLAUDE.md

Starter template for "vibe coding": fast, iterative development in conversation with an AI assistant, using short docs that grow step by step instead of a full design up front. Multi-stack: each sub-project lives in `src/<project-name>/`, with its architecture defined under `docs/architecture/`.

## Project

<!-- Filled in by the `init-project` skill: project name, target system, stacks. -->

## Structure

`docs/` is the **single source of truth**: read it before any change, update it the moment something changes.

```text
.claude/             # Assistant config: skills
src/<project-name>/  # One folder per sub-project (web/, mobile/) — never source directly under src/
docs/
├── requirement/     # YYYY-MM-DD-task-name.md — raw customer info, ideas, bug reports (free format)
├── plan/            # 01_plan.md (index: overview, link, status) + YYYY-MM-DD-task-name.intent.md
├── architecture/    # NEXT_ARCHITECTURE.md, FLUTTER_ARCHITECTURE.md — one per stack
├── specs/           # CODE-feature-name.spec.md + 01_spec.md (index)
├── api/             # api.md (conventions/index) + endpoints/*.md (one per endpoint group)
├── database/        # db.md — one shared schema/ERD/migration doc, extended in place
├── screens/         # FEATURE-CODE-screen-name-00.screen.md + same-named .screen.html + 01_screen.md (index)
├── design/          # DESIGN.md, design-system.html, theme.css
├── test/            # CODE-feature-name.testcase.md — one per feature
└── superpowers/plans/  # YYYY-MM-DD-task-name.md — implementation plan, one new dated file per task
```

- `CODE` = short uppercase feature-area id (`AUTH`, `PAY`), used consistently across spec, test case and commit.
- `01_*.md` index files are updated whenever an entry is added or changed.
- Files stay in place permanently; git history is the record.
- **Document format:** every doc is created from the matching template in `.claude/skills/init-project/templates/` (requirement, intent, spec, screen `.md` + `.html`, API, DB, test case, plan, index files). Never invent a format; change the template if the format must change.

## Workflow

Per feature/task, work through the stages in order. Every task starts at stage 1, new feature or change alike.

| Stage                    | Step              | Skill                                          | Output                                                                  |
| ------------------------ | ----------------- | ---------------------------------------------- | ----------------------------------------------------------------------- |
| **1. Requirement**       | Collect           | none (save what the user pastes)               | `docs/requirement/` file                                                |
| **2. Plan**              | Brainstorm intent | `superpowers:brainstorming`                    | intent file + `Draft` entry in `01_plan.md`                             |
| **3. Design** (require)  | 3a Architecture   | `superpowers:brainstorming`                    | `docs/architecture/<STACK>_ARCHITECTURE.md`                             |
|                          | 3b Spec           | `superpowers:brainstorming`                    | `docs/specs/CODE-feature-name.spec.md` + `01_spec.md` entry             |
|                          | 3c Screens        | `superpowers:brainstorming`, `frontend-design` | `.screen.md` + `.screen.html` + `01_screen.md` entry                    |
|                          | 3d API            | `superpowers:brainstorming`                    | `docs/api/api.md`, `endpoints/*.md`                                     |
|                          | 3e Database       | `superpowers:brainstorming`                    | `docs/database/db.md`                                                   |
| **4. Build**             | 4a Define plan    | `superpowers:writing-plans` (or `planner`)     | `docs/superpowers/plans/YYYY-MM-DD-task-name.md`                        |
|                          | 4b Implement      | `superpowers:executing-plans` (or `subagent-driven-development`) | working code; check off each plan step as it is done  |
|                          | 4c Verify         | `superpowers:verification-before-completion`   | build/lint/typecheck passing, actually run                              |
|                          | 4d Code review (require) | `superpowers:requesting-code-review`    | CRITICAL/HIGH findings fixed                                            |
| **5. Test** (require)    | 5a Generate cases | `generate-testcases`                           | `docs/test/CODE-feature-name.testcase.md`                               |
|                          | 5b Run cases      | developer or AI                                | executed cases with results                                             |
|                          | 5c Fix bugs       | `superpowers:systematic-debugging`             | root cause fixed, affected cases re-run                                 |
| **6. Deploy** (require)  | Deploy            | the project's own skill in `.claude/skills/`   | release                                                                 |
| **7. Maintain**          | Intake            | none                                           | bug → save in `docs/requirement/`, then 5c; idea/feature → stage 1      |

### Gates

- **Stage 2:** restructure the raw requirement into the intent file; never write to `docs/specs/` here. After the user reviews it, set its `01_plan.md` entry to `Accepted` (or `Rejected` and stop) and commit. Only `Accepted` plans move on.
- **Stage 3 (mandatory):** first tell the user which sub-steps the task needs and why, then create only those. Read the intent and current core docs first; every requirement lands in them and every Open question is answered or carried forward. Then check related specs for conflicts. 3a is written in a project's first loop by adapting the closest reference in `docs/architecture/`, confirmed with the user. New/changed specs and screens stay `Draft` in their index until the user reviews them, then `Approved` and commit.
- **Stages 2 and 3:** write into `docs/` (not the skill's default `docs/superpowers/specs/`), and do not invoke `superpowers:writing-plans` afterwards. That is 4a.
- **UI (3c, 4):** follow `docs/design/DESIGN.md` and `design-system.html`. The `.screen.html` prototype is the visual source of truth for its screen; follow it strictly.
- **Build:** comply strictly with the stack's architecture file, the screen prototype and the design system. Confirm with the user before deviating on patterns, structure, layout, spacing, tokens or component states.
- **Test:** this project overrides `~/.claude/rules/common/testing.md` and `web/testing.md`: no coverage requirement, no committed test suite; test cases are documents. If a fix changes what the feature does, update docs from stage 2 (intent first, then cascade). Wait for the user's explicit confirmation that the feature works before Deploy.
- **Deploy:** if no deploy skill exists, ask the user; never improvise. The deploy skill defines how code reaches `main`, per `git-conventions`. There is no separate merge step.

## Rules

- **Superpowers plugin required:** confirm `superpowers:*` skills are installed before any work.
- Use the `git-conventions` skill for git: GitFlow branches + Conventional Commits.
- Don't create directories outside the layout above without confirming first.
- Never read or print production secrets/config (`.env`, `.env.production`, credentials, API keys). If a task seems to need one, ask the user.
