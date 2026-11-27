---
name: capture-requirement
description: Captures raw requirement input (stage 1) into one consolidated markdown file under docs/requirement/, from pasted text, local files, links/tickets or meeting transcripts, then asks about gaps in Source, Type and bug details. Use whenever the user pastes customer notes, an idea, a feature request, a change request, a bug report, a ticket link or a meeting transcript, or says "lưu requirement", "ghi lại yêu cầu", "save this requirement", "capture this", even if they do not name the skill. Also use at stage 7 (Maintain) when a new bug or idea arrives. Output is docs/requirement/YYYY-MM-DD-task-name.md. It does not write the intent, spec or plan.
license: MIT
---

# Capture requirement

Stage 1 of the workflow in `CLAUDE.md`: turn whatever the user brings into one requirement file, so every later stage starts from a faithful record. The value of this file is that it is *raw*: stage 2 restructures it into an intent, and that only works if nothing was interpreted away here. So preserve, do not summarize or fix.

## Workflow

### 1. Collect every source

The input can be a mix of: text pasted in chat, local files (md, txt, pdf, docx, screenshots), links or tickets (Jira, Redmine, Google Docs, Notion), and meeting transcripts (claude.ai Meetings). Gather all of them for the task, using whatever tool or skill reaches the source. If a link cannot be read (private, no connector), say so, keep the link in the file and ask the user to paste the content. Never read or copy secrets (`.env`, credentials, API keys) even if a source contains them; redact and tell the user.

### 2. Decide how many files

Read the sources and check whether they hold one task or several unrelated ones. If several, propose a split (task names plus which parts of the input go where) and wait for the user to confirm before writing. If one, continue. Each task gets exactly one consolidated file, however many sources feed it.

### 3. Write the file

Create `docs/requirement/YYYY-MM-DD-task-name.md` from `.claude/skills/init-project/templates/requirement.md`. That template is the only format; do not invent another. Use today's date and a kebab-case task name. If a file for the same task already exists, append the new input to it in place instead of creating a second one.

- **Source / Type:** fill what the input states or clearly implies (`feature`, `change` or `bug`); leave a `?` for anything unknown and ask in step 4. Do not guess.
- **Raw input:** one sub-heading per source (`### Pasted by user`, `### File: path`, `### Ticket: link`, `### Meeting: title, date`), each holding the content verbatim. Fix nothing: typos, contradictions, half sentences and the original language stay. For a file or screenshot that cannot be inlined, reference its path or link and transcribe any text in it. Do not copy binaries into `docs/`.
- **Bug report block:** keep and fill it for `Type: bug`; delete it otherwise.

### 4. Ask about gaps

After saving, list only what is missing and ask in one round (AskUserQuestion when options are clear, plain questions otherwise):

- unknown Source or Type;
- for a bug: where, steps to reproduce, expected vs actual, environment;
- a source that could not be read.

Do not ask product questions (scope, edge cases, priorities); those are stage 2's brainstorm. Write the answers into the file (Source, Type, Bug report block). If the user does not know, leave `?` and move on.

### 5. Report

Tell the user the file path(s), what is still `?`, and stop. Do not write an intent, spec or plan, and do not touch `docs/plan/`. Mention the next step only as information: a feature or change goes to stage 2, a bug goes to 5c (`superpowers:systematic-debugging`). Commit only when the user asks, following `.claude/rules/git-workflow.md`.
