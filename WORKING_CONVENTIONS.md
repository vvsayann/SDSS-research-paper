# Working conventions

A set of conventions for sustained, multi-session work on a project: which working documents to keep, how to log issues and defer verification, how generated artifacts and per-unit documentation should behave, and the discipline around scope, git, and destructive operations.
The conventions here recurred independently across several unrelated projects before being written down.
Treat this as a starting template for a new project's `CLAUDE.md`, not a rulebook — adopt what fits, drop what a given repo genuinely has no use for.

**Scope.** Written for an agent (or a person) doing sustained, multi-session work in a repo — solo or small-team, autonomous or supervised.
It's overhead for a one-shot script, a throwaway notebook, or anything small enough to hold entirely in one session's head; don't reach for any of this until a project has outlived a single sitting.
When a new project's `CLAUDE.md` ends up a strict subset of what's here, say so in one line at the top of that file (e.g. "derived from `WORKING_CONVENTIONS.md`; §4/§11/§14 dropped — no deferred-verification need, no VCS, no randomness") so a later session can tell an intentional omission from an oversight.

**This file is not exhaustive, and it is not a gate.** A convention the user states in the moment applies immediately, whether or not it's written down here — never withhold or hedge on an instruction because "it isn't in `WORKING_CONVENTIONS.md`."
Fold it into this file, as a durable addition for next time, only when asked to; the file catching up is a separate step from the instruction being valid.
The same goes for a durable override, not just an omission: a project whose own convention deliberately contradicts one here (e.g. §11's "never commit unless asked," overridden by a project that commits after each phase) records that override explicitly — in the project's own `CLAUDE.md`, alongside its dropped-sections note — rather than leaving it to read as drift from this file.

**First adoption.** If this is the first time a project is adopting from this file, start with §1–5 (working documents, the shared timestamp format, the bug/issue log, the verify queue, verify-don't-assume — the timestamp format is included because §1, §3, §4, §8, and §15 all depend on it) and add the rest — §6 onward — only when a specific need actually appears; that's cheaper than deciding up front which of a dozen-plus sections to drop.
§1's `PLAN.md` subsection stays conditional even within this starting set — "start with §1–5" means the trio, the timestamp format, and the verify queue, not `PLAN.md` by default.

---

## 1. Long-running-project working documents

For any project spanning multiple sessions, keep a small set of root-level `.md` files rather than letting state live only in chat history or scattered code comments:

- **`BUGS.md`** (or `ISSUES.md`) — the bug/observation log (format in §3).
- **`HANDOFF.md`** — a current-state narrative for picking work back up after a gap.
  Dated explicitly with date and time together, not a bare date (§2 — "written on X, last extended on Y").
  If it stops being updated while the project keeps moving, add a **staleness note** saying so and pointing at a more current source (commit history, the bug log) rather than letting stale prose quietly pass as current state.
- **`VERIFY.md`** — a queue of pending verification requests for checks the agent can't or shouldn't perform itself (format in §4).

Any sustained multi-session work accumulates these three needs — open questions worth tracking, problems found along the way, and a resumption point for picking things back up — which is why this trio is a reasonable default the moment work outlives a single sitting.
A bug log, a verify-queue, and a handoff are the shapes those needs typically take in a repo; the same three needs show up in other sustained work too, just described differently.

Read the handoff/state file **first** when resuming a project, before touching anything else — it should point at everything else that matters.
The full resume sequence — not just "read the handoff" — is in §15.

If a project spans multiple machines or environments, don't hardcode one as canonical.
State which environment each set of paths/assumptions belongs to, and re-derive the active one each session from the actual environment rather than trusting a stale memory of a prior session.

**Naming.** Root working docs are `SCREAMING_CASE.md` (`BUGS.md`, `HANDOFF.md`, `VERIFY.md`, `PLAN.md`).
Per-unit notes (§7) live in a named directory (`notes/`, `docs/units/`) with lowercase or kebab-case names.
Generated indexes get a `.generated.md` suffix, or live in a directory a reader can tell apart from hand-written docs at a glance.
The point isn't the specific casing — it's that "this is a doc I edit" versus "this is a doc a script regenerates" is legible from the filename alone, without opening the file and reading its header.

### `PLAN.md` — add separately, for major overhauls

A phased plan (numbered phases, each with concrete actions, marked complete/in-progress/not-started as work lands) is a different kind of artifact from the three above: it's generic project-management structure with nothing repo-specific about it — it would organize a research arc, a migration, or a piece of writing exactly as well as a codebase rewrite.
That generality cuts both ways: it isn't earned by "this project has multiple sessions" alone, the way the trio above is.

**Add it when the work is a genuine major overhaul** — distinct sequential phases, large enough that "which phase are we in, what's left" needs to persist across sessions rather than living in the last message or a to-do list.
Don't add it for ordinary iterative work; a bug log and a handoff note already cover that, and an unnecessary phase plan just adds a file to keep in sync.

When it is warranted:
- Unplanned work that happens anyway gets its own "Unplanned — `<what>`" entry, rather than being silently folded into an existing phase it doesn't belong to.
- Treat phase status as a fact that can go stale exactly like `HANDOFF.md` — update it as phases actually complete, don't let it silently drift from what `git log`/the bug log show.

## 2. Timestamps

Any dated entry, in any working document — a `BUGS.md`/`VERIFY.md` status change, a `HANDOFF.md` update, a `PLAN.md` phase change, a dated addendum (§8), a commit message that references one of them — carries date and time together, never a bare date.
This is stated once here rather than repeated in every section that dates something, so there's exactly one format to check and one place it can drift from.

- **Multiple entries routinely land on the same calendar day** across a long session; a date-only stamp makes their order and relative staleness ambiguous the moment that happens.
- **Use one consistent, sortable format with an explicit timezone/offset throughout a project** — ISO 8601, e.g. `2026-09-25T14:30Z` or `2026-09-25 14:30 UTC` — never a bare date and never local time with no offset.
- **This applies uniformly across every working document, not just one of them.** §1's handoff, §3's bug log, §4's verify queue, and §8's addenda all use the same format, so a reader never has to guess whether two timestamps from different files are even comparable.

## 3. Bug/issue log format

- **Status key** — kept deliberately short, since a status vocabulary that's easy to jumble is worse than a coarser one that isn't:
  - `OPEN`
    - Needs a decision or isn't fixed yet.
  - `FIXED`
    - Changed in the working tree, not yet confirmed.
  - `VERIFIED`
    - The fix was tested directly against the code/repo itself — re-run, recomputed, or otherwise executed, not just read — and confirmed correct.
  - `CLOSED`
    - No longer open for some other reason — superseded by another entry, or a deliberate no-action decision — state which in the entry text rather than adding a tag per reason.
  - `DEFERRED`
    - Tracked for later, explicitly not forgotten.

  Don't conflate `FIXED` with `VERIFIED` — a working-tree change and a directly-tested one are different claims, and collapsing them is how an unconfirmed "fix" quietly ships as done.
  A fix that swaps one function call for a superficially similar one can look equally plausible either way on inspection — the difference only shows up when something is actually executed and compared, which is exactly what `VERIFIED` certifies and a code read alone can't.
  Reopening is normally just moving an entry back to `OPEN` with a note — a `VERIFIED` entry is the one exception, and stays `VERIFIED` unless the underlying code undergoes a breaking change that could invalidate the original check, in which case it reopens to `OPEN` like anything else, with a note on what changed.
- **Stable, prefixed IDs** (`BUG-042`, `OBS-011`), assigned once and never reused or renumbered — so `VERIFY.md` entries, commit messages, or another log can reference the exact same issue instead of re-describing it.
  - **The prefix marks where an entry came from, not its severity or current status.**
    1. `BUG-` for a defect found in the code or data itself;
    2. `OBS-` for something surfaced by discussion or judgment rather than a concrete defect (a design tradeoff, a "is this actually right?" question, a deliberate choice worth recording).

  Both share the exact same status key above — an `OBS-` entry ends up `FIXED` just as often as a `BUG-` ends up `CLOSED` as deliberate-and-not-a-defect.
  Two is the base case here; a project is free to add its own further prefixes for other entry origins it actually and repeatedly has, but that's a per-project call, not something to standardize in advance.
- **The ID namespace is project-global, not per-file**: `BUG-042` is the same issue whether it's cited from `BUGS.md`, a `VERIFY.md` entry, a commit message (§11), or a unit note (§7).
  Don't stand up a parallel numbering scheme for a second log ("verify item 1," "note 3") — it's exactly how two logs silently drift into describing the same fact with different names.
- **Newest entry at the bottom**, IDs assigned in discovery order.
  A separate index table up top can sort/group differently, as long as it's clearly generated ("regenerate rather than hand-edit"), not maintained by hand alongside it.
- **Stamp date and time together when logging an event, never a bare date** — §2 has the shared format and the reasoning; it applies to this log the same way it applies to every other dated document.
- **Link to `VERIFY.md` when a fix needs human confirmation.** A `FIXED` entry that still needs someone to look at the actual result, and the `VERIFY.md` entry for that same check, are two halves of one fact — cross-reference the IDs both ways so "fixed" and "confirmed" can't quietly drift apart on the same issue.
- **A one-line index table**: ID, one-line description, status — the whole log should be skimmable without opening any entry.
  For a `CLOSED` entry specifically, the status column names the reason inline (`CLOSED: superseded by BUG-051`, `CLOSED: no action`) rather than the bare tag — the coarser status key shouldn't cost the skimmability it was designed to protect.
- A status change on an entry and the corresponding index-row update are the same change, not two.
- **Entry structure for a fixed issue**: the resolution first (what was actually true, what changed), then the original diagnosis preserved underneath, labeled as such.
  Never delete the original reasoning — a wrong-but-reasoned guess is useful history, and rewriting it hides how a wrong conclusion was reached.
- **Show impact, not just the fix**: what was affected, and what downstream artifacts inherited the problem.
- **Re-verify status against current state before re-asserting it.** An entry can silently already be resolved by an unrelated later change; check current state before restating an old diagnosis from memory.
- **A wrong "fix" gets reverted and marked as such**, with a pointer to the entry that has the correct diagnosis — don't just quietly delete the mistake.

## 4. Deferred-verification queue

Use this when a check is expensive — in wall-clock time, in access the agent doesn't have, or simply in the **context/tokens it would cost** to pull a large build log or a full rendered output into the conversation just to confirm something short (a compile-and-render pass, a full test-suite dump, a long query result) — or when it's fundamentally a judgment call only a human can make (does this look right, does this read well, does this behave correctly in a real environment).
"The agent technically could run this" is not the bar; a context-expensive check deserves deferral for the same reason a wall-clock-expensive one does.
Rather than skipping the check, or paying its full cost every time:

- **Status key**:
  - `PENDING`
    1. Needs a manual check.
  - `CONFIRMED`
    1. Checked, matches.
  - `FAILED`
    1. Checked, doesn't match.
  - `STALE`/`SUPERSEDED`
    1. The change it was checking has since moved on — don't leave it reading as an open question about something that no longer exists.
- **Reference the originating log entry's ID** (see §3) when an item exists because of a specific fix, so the two logs stay linked instead of describing the same fact twice.
- **Name what or who can close it.** A `PENDING` entry with no defined closer ("needs a manual check") has no endpoint — it can only age.
  Say which specific person, environment, external system, or scheduled event resolves it (e.g. "user, on real hardware," "next full training run," "CI on the next push").
  This is what makes the triage rule below actionable instead of decorative.
- **Give the queue a triage mechanism, not just an add path.** Without one, `PENDING` entries accumulate indefinitely.
  Even something lightweight works: an entry untouched for N sessions gets surfaced at the top instead of silently aging in place forever.
- **Each entry has three parts**: *What changed* (one line), *What to check* (precise enough that the check is unambiguous — not "make sure it looks okay"), *Why* (what a failed check would actually mean, so entries aren't skimmed as boilerplate).
- **Batch entries by unit of work**, not per edit — log after a coherent chunk of related changes, not after every small change.
- **An unconfirmed entry is an open question, not a passed check.** Never report a change as done on the strength of a clean build/exit code/green test run alone if the actual thing being changed is content or behavior that check doesn't cover.
- State which lighter checks the agent *can* still run itself (a syntax/compile check, a source-level grep) versus the heavier one that's deferred — don't defer everything just because part of the verification is expensive.
- At session end, every new or status-changed `VERIFY.md` entry is accounted for — see §15's session-end sweep.

## 5. "Verify, don't assume"

The single most important discipline in this file: replace "this should have worked" with one concrete, reproducible check, every time.

- A clean build, a successful run, or exit code 0 proves the thing is well-formed, not that its output or content is correct.
  Inspect the actual output.
- A change that "should be behavior-preserving" gets a concrete before/after comparison, not a read-through that the logic looks equivalent.
- A dependency or interface change gets checked against the live environment (does it actually resolve/work now), not assumed safe from the diff.
- A "should be closed" log entry gets re-checked against current state, not re-stated from memory.
- Review a log, metric, or history across its **full run**, not just the final/endpoint value — an endpoint-only summary can hide a problem-and-recovery in the middle that changes the conclusion.
- A new test, linter, or diagnostic tool is untrusted until it correctly handles a known-good case (and ideally a known-bad one) — verify the tool before trusting its verdict on the real target.
- Running something to check it works can itself change state (stray files, side effects) — check what actually happened afterward, don't assume a "just testing" run was inert.
- **State what result would falsify the assumption before running the check**, not just what success looks like — a check that can only confirm and never disconfirm isn't testing anything.
- **A fix earns a regression test wherever a test suite already exists** for that code; where one doesn't, the checks above stand in for it, but say so explicitly rather than letting "verified once, informally" pass as equivalent to "covered by a test."
- **When a check comes back ambiguous, surprising, or just doesn't sit right, that's a decision point for the user, not a discrepancy to quietly resolve.** Picking whichever explanation lets the work continue is itself an unverified assumption — flag it and let the user decide, the same reason an `OPEN` bug-log entry (§3) exists instead of the agent silently closing it one way.
- Once a claim about state has been made, label it — §16 is the reporting half of this section.

## 6. Generated-artifact conventions

- **Generated content is never hand-retyped into its destination.** Anything derived from data or code is produced by a script/build step and consumed by direct inclusion or reference — hand-copying a computed value into docs, a `README`, or another file is exactly how it silently drifts out of sync with the thing that actually computes it.
  Auto-generated files say so at the top and are never hand-edited.
- **Every generated file is self-contained enough to check without its generating script**: whatever identifies what it's describing, whatever assumptions/config produced it, and (for anything computed) its provenance — not just the bare result with no way to sanity-check it.
- **Style/format constants live in one place**, and every new piece of output pulls from it rather than hardcoding a literal that duplicates it — a hardcoded value silently defeats the single-source-of-truth design and reintroduces drift the next time the shared value changes.
- **An input that can't be derived from what's in the repo must fail loudly, not sit quietly wrong.** Keep it as one clearly-named, version-checked constant and assert it against whatever *is* derivable, so a stale value crashes instead of silently producing a wrong result.
- **Derive generated formatting/precision programmatically, not by eye** — eyeballing produces inconsistent results across a batch and is how a rounded value ends up silently misleading.
- **Tables in any generated documentation (LaTeX, Markdown, a report) are code-generated from the underlying data file, never hand-assembled** — a small script reads the CSV (or equivalent) and emits the table markup directly, regardless of target format.
  This is the same rule as "generated content is never hand-retyped" above, applied specifically to tables, since a hand-built table is the most common place that rule gets silently broken.
- **Where a project produces rendered figures, generate the full triple together, from the same script run**: a data file (CSV or equivalent — the source of truth), a quick-preview raster (PNG), and a durable/vector format for inclusion elsewhere (PDF/SVG).
  Never produce just one or two and reconstruct the rest later — a plot regenerated by hand from a differently-shaped export is exactly how a figure and its underlying numbers quietly stop matching.

## 7. Per-unit-of-work documentation

- **Any non-trivial piece of work (a module, an experiment, a feature area) carries its own short note**, written for future-you, not for the end deliverable: what it does and why (the actual reasoning/source, not just what), every judgment call and who made it (attribute explicitly, and record rejected alternatives so a decision doesn't get silently re-litigated), what was validated, and known limitations.
  Written as the work happens, not reconstructed afterward.
- **An experiment that forked off a parent piece of work reports its outcome back to that parent** — success or failure — once it concludes, in whatever document tracks the parent's state (`HANDOFF.md`, the parent's own note).
  A detached experiment whose result never reaches the thing it was meant to inform is wasted effort even when the experiment itself was run well.
  If the experiment *is* the top-level unit of work — nothing it detached from — this doesn't apply; standalone is fine.
- **A living index for any growing collection of files/experiments/outputs**: one row per item with a one-line description, plus a running "what's still open" note.
  A new item gets its index row in the same change that creates it; a status change sweeps the index in the same change — the index is never allowed to drift from reality.
  Where the collection is large or the entries are already structured, generate the index from them by script rather than hand-maintaining both; for a handful of entries, doing it by hand is fine as long as the same-change rule actually holds.
- **A unit note is superseded, not deleted, when the unit is removed or absorbed.** If a module is deleted, split, or merged into another, its note gets a one-line `superseded by <X>` header (and, if the repo has an archive convention, is moved there) rather than disappearing.
  Same reasoning as §3's preserved diagnoses: the record of what a decision was for, and why it stopped being the right shape, is exactly what a future reader needs when the same question comes up again.

## 8. Frozen vs. living documents

- **Anything pre-committed before results exist (a preregistration, a frozen spec, a fixed set of acceptance criteria, a dated snapshot) is never rewritten after the fact** — amend with a dated addendum (its own heading, e.g. `## Addendum 2026-09-25T14:30Z — <reason>`, timestamped per §2, never blended into the original text), never edit the original.
  The moment it's editable after the fact, it stops meaning anything as a pre-commitment.
  **This is a different object from the phased `PLAN.md` in §1**, which is an execution tracker meant to be updated in place as work lands — don't let the shared word "plan" conflate the two; if a project has both, say so explicitly, since the naming collision invites exactly that confusion.
- **Living documents are updated in place**, and a fact that appears in more than one document gets updated in all of them in the same change — not just in whichever file happened to be open.
- **Report exceptions per-case, never averaged away**: "3 of 4 done, 1 still open," not "mostly done" — a summary that erases which case is the holdout is actively misleading.

## 9. Scope boundaries and subagent use

- **State the working boundary explicitly** for any project scoped to specific directories/repos: every read/edit/write/command should resolve inside it, no destructive or global operation runs outside it, and searches are rooted at the specific subdirectory, never at a parent directory or home.
- **Don't spawn subagents by default.** They help for genuinely independent, parallelizable work; a tightly-coupled serial task is simpler and more reliable as one agent working through it in order.
- **When agents are spawned, verify their actual output/diffs before relying on them** — a subagent's summary describes what it intended to do, not necessarily what it did.
- **Every subagent prompt restates the scope boundary explicitly** — a fresh agent has no way to infer a boundary it was never told about.
- §10 lists the operations that require confirming with the user regardless of scope.

## 10. Destructive and irreversible operations

Confirm with the user before any of the following, regardless of scope (§9).
Grouped by *kind* of risk, not by how the thought occurred:

**Data destruction:**

- `rm` outside the working tree; `rm -rf` anywhere without a specific, listed path.
- Dropping a database or table, invalidating a cache other work depends on.
- Overwriting a non-generated file wholesale (`>` redirect, `mv` over an existing file) rather than editing it in place.

**History rewrite on shared state:**

- Force-push, branch deletion, tag deletion, or history rewrite (`rebase`, `squash`, `filter-branch`) on a branch that's been pushed or shared.

**Blast radius beyond scope:**

- Any operation touching a path outside the stated working boundary (§9).
- Mass renames, moves, or refactors that touch more files than the current change was scoped to.

**Irreversible external side effects:**

- Deleting a cloud resource, revoking a credential.

The default is to propose the operation and let the user confirm; "the user asked for X" is not blanket authorization for the destructive sub-step unless X is the destructive step itself.
The test that catches whatever this list misses: if undoing the operation would require anything other than a `git checkout` or a re-run of a script, it belongs on this list.

## 11. Git and commit discipline

- **Never commit unless explicitly asked**, and treat that as authorization for this instance, not a standing one — default to working-tree-only for exploratory/iterative work.
  (This is written for an autonomous or semi-autonomous agent; it isn't a claim about how human teammates should work with each other.)
- **Never commit secrets or credentials.** Check file contents before staging anything whose name merely *looks* safe (a `.env`, a config file, a fixture) — the risk is in the content, not the filename.
- **Check what actually got staged before committing** (`git status` after a broad `git add`) — unrelated pre-existing staged files can silently ride along; if caught after the fact, fix with a new commit, not an amend.
- **Only amend a commit that hasn't been pushed.** Once pushed, correct with a new commit.
- **The same caution extends to any history rewrite on a branch that's been pushed or shared, not just amending** — §10 has the specific confirmation rule.
- **If the project defines its own commit-message format, follow it exactly** rather than defaulting to a generic style — check for a documented convention and recent history before the first commit in an unfamiliar repo.
- **Reference the relevant log ID when a commit addresses a logged item** (`fix: <subject> (BUG-042)`) — so `git log` and `BUGS.md`/`VERIFY.md` can be cross-checked without a separate mapping file, and so a reader of either can find the other.
- Keep any required attribution/trailer on every commit made, appended after the message body, regardless of the project's own format.

## 12. Code style: match the project, don't default

- Match the project's actual configured style (formatter/linter config, existing patterns) even when it differs from a tool's stock default — check the repo's own config before assuming one.
- **Copy rather than fight a fragile cross-module import.** If reusing code from elsewhere in the same repo would require awkward path manipulation or restructuring, a verbatim copy with a one-line comment noting the source is preferable to a fragile import — but log the duplication somewhere visible (the relevant unit's note, per §7) so it can become a proper shared import later, deliberately.
- Don't add error handling, validation, or abstraction for scenarios that can't occur — trust what's already guaranteed by the surrounding code, and keep changes scoped to what was asked.
- **Match the project's dependency-pinning discipline.** If it pins versions or commits a lockfile, don't introduce an unpinned dependency; if a lockfile and the manifest it's derived from disagree, treat that as a bug to flag, not a mismatch to silently resolve one way.

## 13. Prose formatting (when a project has substantial written docs)

For projects with real prose documentation (design docs, long-form notes, papers, changelogs):

- **One sentence per line** (semantic line breaks) in prose files — never wrap a sentence across lines, never put two sentences on one line.
  Reflow existing paragraphs when editing them, even if they didn't start that way.
- **Why it's worth adopting**: it keeps diffs legible — a one-sentence edit shows as a one-line diff instead of a reflowed paragraph.
- Tables, code blocks, and other structured blocks are exempt and keep their own layout.
- **Descriptive text describes, it doesn't interpret.** A caption or status note should let a reader parse the referenced thing standalone, but shouldn't assert a conclusion — that belongs in the surrounding narrative.
  Test: if the sentence would still be true after the underlying thing changed, it's description; if a later change could make it false, it's interpretation and belongs elsewhere.

## 14. Determinism (when a project involves randomness)

- Don't scatter or duplicate literal seeds across scripts, and never re-seed inside a loop over runs/iterations meant to be independent — a fresh identically-seeded generator per iteration silently correlates or duplicates results that were supposed to be independent.
  One named master-seed constant is fine; derive per-run seeds from it deterministically rather than hand-picking a new literal each time.
- Derive a per-run seed deterministically from a single auditable master value, build one generator, and thread that generator object through every downstream call rather than re-passing a bare seed value repeatedly.
- To verify determinism after a seeding change, temporarily shrink the workload (fewer iterations/samples) rather than paying full cost twice — determinism doesn't depend on scale.
  Never leave the shrunk value as the on-disk default; revert it before finishing.

## 15. Session-end and resume protocol

§1 says to read the handoff first when resuming and to keep it current while working; this section is the concrete checklist for both ends of that gap.
It's written for a single agent picking work up cold — every step is something the previous session's notes can't be assumed to have already done for you.
Written in git-repo terms below, since that's the common case §1's trio actually targets; a project without version control adapts the same shape (its own change record in place of `git log`, its own way of stating outstanding work in place of `git status`) rather than skipping the checklist entirely.

**Resuming:**

1. Read `HANDOFF.md` first (§1).
   Nothing else until it's read.
   If §1's staleness note applies — the handoff says it's stale and points at a more current source — anchor every step below on that source instead of the handoff's own (admittedly stale) timestamp.
2. Re-derive the active environment from the actual environment — hostname, working directory, tool versions, active virtualenv/container — rather than trusting the environment assumed by the handoff (§1).
3. Use `git log` since that timestamp (the handoff's, or the more-current source's if the handoff was stale).
   Commits may have moved state past what the handoff describes; the handoff is a narrative, the commit log is a fact.
4. Open every `BUGS.md` entry whose status changed since that timestamp, and every `PENDING` `VERIFY.md` entry.
   Both are candidate work.
5. If `PLAN.md` exists, check current phase status against `git log`/`BUGS.md` rather than trusting the phase marker alone (§1's staleness note applies here too).
6. Only then pick up new work.

**Ending a session (or a deliberate pause):**

1. Update `HANDOFF.md` with date and time together (§2 format): what landed, what's mid-flight, what's next.
2. Sweep the `VERIFY.md` queue: anything new from this session is logged; anything the session confirmed is marked `CONFIRMED`; anything superseded by a later change is marked `STALE`/`SUPERSEDED` (§4).
3. Update `BUGS.md` statuses for anything touched this session, including the cross-reference to the corresponding `VERIFY.md` entry (§3).
4. If `PLAN.md` exists, update phase markers to match what actually landed.
5. Leave the working tree in a stated condition — either "committed as `<sha>`" or "uncommitted: `<files>`" — named explicitly in the handoff, not left for the next session to discover by `git status`.

The reason both halves are checklists and not prose: the failure mode this section exists for is a session that ends "cleanly" in memory but not in the repo — the handoff still describes last week, the verify queue has three stale `PENDING` entries, and the next session burns its first twenty minutes rebuilding state that was available for free five minutes before the last one ended.
This protocol assumes there was a clean ending to run it at; §17 covers what to do about the sessions that don't get one.

## 16. Claim vocabulary

When reporting state to the user — or writing it into a log, handoff, or note — label every non-trivial claim about what is true, and keep the label honest:

- **verified** — a specific check was run; name it and where (`pytest tests/x.py::test_y`, `git log -n 3`, rendered `out/fig1.pdf`).
- **inferred** — follows from something verified, but not itself directly checked.
- **assumed** — not checked, and the reasoning it was arrived at should be stated.
- **unknown** — explicitly not established; don't let this read as either `assumed` or `verified`.

§3's `VERIFIED` and §4's `CONFIRMED` are file-specific instances of exactly this `verified` label; a bare `FIXED` (§3) sits somewhere between `inferred` and `assumed` depending on how it was actually reached.
This section names the general vocabulary those two status keys already narrow down for their own purposes — not a third, unrelated one.

Why this is a section and not a bullet: §5 says to run a check instead of assuming; §3/§4 give you somewhere to record the result.
This is what to do *after* the check — how to phrase a claim so the reader (the user, a future session, future-you) can tell what evidence stands behind it.
Unlabeled prose defaults to reading as `verified`, which is exactly the failure mode §5 exists to prevent — §5 without this section fixes the action and leaves the reporting open.

This isn't a demand to hedge every sentence.
"The file is 340 lines" is a `verified` claim if you counted, and doesn't need the label spelled out.
The label matters for anything where "probably true" and "checked" would lead to different next actions.

## 17. Regular updates, not only at session end

§15's session-end sweep assumes there's a clean ending moment to run it at — but a session can end without warning (a dropped connection, a closed window, the user simply not returning), and nothing forces that sweep to actually happen.
Relying on session-end alone means `HANDOFF.md`, `VERIFY.md`, and `BUGS.md` — exactly the three files §1 already flags as able to go stale — can go stale for an entire session, or several, with no natural trigger to catch it.

- **Every fix or finding lands in its working document as it happens, not batched for later.** A `BUGS.md` entry gets written the moment something is found or fixed, not saved up for an end-of-session pass — §3's "newest entry at the bottom" convention only holds if entries are actually added as they occur, not reconstructed afterward.
- **After a major, coherent piece of work — not only at the literal end of a session — run the same sweep §15 describes for session end, at that natural checkpoint**: update `HANDOFF.md`, close out or add `VERIFY.md` entries, update `BUGS.md` statuses.
  "Major" here is the same unit-of-work granularity as §4's "batch entries by unit of work," not an arbitrary timer or a fixed number of edits.
- **Treat staleness in these three files as a risk to manage continuously, not a problem only visible at resume time.** §1's staleness note is the fallback for when this discipline lapsed anyway; it isn't a substitute for updating often enough that it rarely has to be invoked.
- §15's session-end protocol is still the definitive, thorough version of this sweep — the point of doing it regularly is that the session-end pass then confirms already-current state instead of reconstructing an entire session's drift in one go.
