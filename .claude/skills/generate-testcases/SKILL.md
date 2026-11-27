---
name: generate-testcases
description: Generates the test case document for a feature (stage 5a) from its spec and screens, covering functional, edge case, error handling and state transition scenarios with requirement traceability. Use when the user asks to generate test cases, plan QA, create test scenarios or test documentation for a feature, or when stage 4 is done and stage 5a starts. Output is docs/test/CODE-feature-name.testcase.md.
license: MIT
---

# Generate test cases

Adapted from [stellarlinkco/myclaude `test-cases`](https://github.com/stellarlinkco/myclaude/tree/master/skills/test-cases) (MIT). Same testing philosophy and test case structure; input and output are bound to this template's `docs/` layout.

Turn a feature's requirements into structured test cases that cover functionality, edge cases, error scenarios and state transitions. Test what matters: every requirement gets coverage, quality over quantity.

## Principles

1. **Requirement-driven, not implementation-driven**: each case maps to a spec rule, error, acceptance criterion or screen state, never to code details.
2. **Complete coverage**: every requirement has at least one case. Cover the happy path, edge cases (boundaries, empty inputs, max limits), error handling (invalid input, failures, permission errors) and state transitions (if stateful).
3. **Clear and actionable**: a QA engineer (or the AI) can execute each case without ambiguity.
4. **Traceable**: every case names its requirement; the coverage matrix shows the mapping.

Details and design patterns: `references/testing-principles.md`.

## Workflow

### 1. Gather requirements

Read, in this order: the feature's `docs/specs/CODE-feature-name.spec.md`, its `docs/screens/*.screen.md` (states, validation, copy) and the matching prototype `.screen.html`, then `docs/api/` and `docs/database/db.md` if the spec references them. If the user names a different source, use it. If requirements are unclear or incomplete, ask with AskUserQuestion (core flows, acceptance criteria, edge cases, state transitions, platforms) instead of guessing. Do not invent behavior the docs do not state; report the gap.

### 2. Extract scenarios

Per requirement, list the functional, edge, error and state transition scenarios, with preconditions, steps, expected results and postconditions. Include every spec'd error, every screen state, validation limits and accessibility basics.

### 3. Write the document

Create `docs/test/CODE-feature-name.testcase.md` from `.claude/skills/init-project/templates/testcase.md`. That template is the only format; do not invent another (change the template if the format must change). If the file exists, extend it in place and keep existing IDs and results.

- IDs: `<CODE>-F-001` functional, `-E-` edge, `-ERR-` error, `-ST-` state transition (optional `-SEC-`, `-PERF-`, `-A11Y-`). Unique, sequential per prefix.
- Priority: High for critical paths and data integrity, Medium for normal flows, Low for cosmetic.
- Every case starts with `Result: Not run`.
- Remove a category that does not apply (for example state transitions for a stateless feature) rather than leaving it empty.

### 4. Validate coverage

- [ ] Every requirement has at least one case; the coverage matrix is complete
- [ ] Happy path covered for all user flows
- [ ] Boundary values, empty inputs and max limits covered
- [ ] Every error in the spec and every error state on the screens covered
- [ ] State transitions covered if the feature is stateful
- [ ] IDs unique and prefixed correctly
- [ ] Steps executable; expected results measurable and tied to a spec rule or screen state

Fill gaps with more cases before finishing.

### 5. Summarize

Reply in the user's language: total number of cases, breakdown per category, assumptions or spec gaps found, and the file path. Stage 5b (run cases) and 5c (fix bugs) follow; if a gap means the spec is wrong or incomplete, send it back to stage 2/3 instead of patching the test case.

## References

- `references/testing-principles.md`: core principles, coverage requirements and design patterns
- `.claude/skills/init-project/templates/testcase.md`: the document format
