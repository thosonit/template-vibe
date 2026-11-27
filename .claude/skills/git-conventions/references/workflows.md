# Workflow candidates

## GitHub Flow

Permanent: `main` (always deployable).

| Branch | Off | Into | Naming |
|---|---|---|---|
| Work | `main` | `main` via PR | `feat/`, `fix/`, `docs/`, `chore/`, `refactor/<short-description>` |

Hotfix is just a `fix/` branch. Delete branch after merge. Squash-merge keeps `main` linear. Add tags `vX.Y.Z` on `main` if releases are versioned.
Best for: solo or small teams, continuous deploy. Cost: no staging buffer.

## Trunk-based

Permanent: `main`. Work lands on `main` in very small steps (daily or faster), by direct commit or branches living under a day. Unfinished work hides behind feature flags.
Best for: experienced teams with strong CI and tests. Cost: poor fit without automated tests.

## GitLab Flow (environment branches)

Permanent: `main` plus one branch per environment (`staging`, `production`). Changes merge to `main`, then are promoted by merging down the chain.
Best for: apps deployed to several environments without versioned releases. Cost: promotion merges to maintain.

## Release-branch flow

Permanent: `main`; `release/<version>` cut from `main` for stabilisation and kept alive for patches (fixes cherry-picked back to `main`).
Best for: several supported versions (SDKs, on-prem products). Cost: lighter than Gitflow (no `develop`) but cherry-picks need care.

## Gitflow

Permanent: `main` (production), `develop` (integration, default base).

| Branch | Off | Into | Naming |
|---|---|---|---|
| Feature | `develop` | `develop` | `feature/<short-description>` |
| Release | `develop` | `main` + `develop` | `release/<version>` |
| Hotfix | `main` | `main` + `develop` | `hotfix/<short-description>` |
| Chore/docs/refactor | `develop` | `develop` | `chore/`, `docs/`, `refactor/<short-description>` |

Tag `vX.Y.Z` on `main` after every release/hotfix merge, then merge back into `develop`.
Best for: scheduled releases, staging env, QA phase. Cost: heaviest; overkill for solo or continuous deploy.

## Forking flow

Contributors fork, branch, and open PRs to the upstream `main`; maintainers merge.
Best for: open source with outside contributors.

## Shared conventions

- `<short-description>` is kebab-case; prefix with the ticket id (`feat/PROJ-123-login`) only if a tracker is in use.
- Branch type prefixes follow the commit types of the common commit rule.
- Solo with no reviewer and no CI on PRs: state "direct push to `main` allowed" explicitly in the rule and use squash merge as the default merge method. If CI runs on PRs, require a PR even when self-merged.
