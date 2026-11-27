<!--
Stage 5a · save as docs/test/CODE-feature-name.testcase.md. One per feature, generated from its spec and screens
by the `generate-testcases` skill. Format adapted from stellarlinkco/myclaude `test-cases` (MIT).
Test cases are documents run by the developer or the AI (no committed test suite). Record results in stage 5b.
Requirement IDs come from the spec (rules, errors, acceptance criteria) and screen states.
ID prefixes: <CODE>-F-001 functional · -E- edge · -ERR- error · -ST- state transition
(optional: -SEC- security, -PERF- performance, -A11Y- accessibility). Delete a category that does not apply.
-->

# Test cases <CODE>: <Feature name>

## Overview

- **Feature**: <Feature name>
- **Requirements source**: [CODE-feature-name.spec.md](../specs/CODE-feature-name.spec.md), [FEATURE-CODE-screen-name-00.screen.md](../screens/FEATURE-CODE-screen-name-00.screen.md)
- **Test coverage**: <summary of what is covered and what is not>
- **Last updated**: YYYY-MM-DD

## Test case categories

### 1. Functional tests

Normal user flows and core functionality.

#### <CODE>-F-001: <Test case title>

- **Requirement**: <spec rule / acceptance criterion / screen state>
- **Priority**: High | Medium | Low
- **Preconditions**:
  - <condition 1>
  - <condition 2>
- **Test steps**:
  1. <step 1>
  2. <step 2>
  3. <step 3>
- **Expected results**:
  - <observable outcome 1>
  - <observable outcome 2>
- **Postconditions**: <state after the test>
- **Result**: Not run
- **Notes**:

### 2. Edge case tests

Boundary values, empty inputs, maximum limits.

#### <CODE>-E-001: <Test case title>

<same fields as above>

### 3. Error handling tests

Invalid inputs, failure scenarios, permission errors, every error defined in the spec.

#### <CODE>-ERR-001: <Test case title>

<same fields as above>

### 4. State transition tests

Valid and invalid state changes, every screen state (only if the feature is stateful).

#### <CODE>-ST-001: <Test case title>

<same fields as above>

## Test coverage matrix

| Requirement | Test cases                  | Coverage |
| ----------- | --------------------------- | -------- |
| <REQ-001>   | <CODE>-F-001, <CODE>-E-001  | Complete |
| <REQ-002>   | <CODE>-F-002                | Partial  |

## Notes

- <additional testing considerations>
- <known limitations or assumptions>

Result values: `Not run` · `Pass` · `Fail` (link the issue in `docs/requirement/`)
