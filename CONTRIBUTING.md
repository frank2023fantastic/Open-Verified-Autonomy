# Contributing

Start with [the first 72 hours](docs/START_HERE.md) and [the task backlog](docs/plan/BACKLOG.md).
Code, scenario design, measurements, documentation, and independent reproduction are all useful contributions.

## One task at a time

1. Choose a ready task and record one owner and a different reviewer in its GitHub Issue.
2. Read the relevant architecture, interface, and acceptance draft.
3. Agree on the files being changed so two people do not edit the same file concurrently.
4. Refresh `main` before editing. Inspect local changes before pulling or copying files.
5. Make the smallest useful change; record what was checked and what is still unknown.
6. Commit and push to `main` with the task ID in the message. Use a non-forced update; reconcile concurrent changes if necessary.
7. Link the commit and evidence from the Issue. Close it only when its completion checklist is met.

Do not reset or discard a collaborator's work to resolve a conflict. Review can happen before a coordinated
main commit and in the Issue; the starting workflow does not require a PR.

## Completion is specific

A task can finish a document, a setup experiment, or a hardware test. State which one.
Finishing a task is not automatically completion of its parent gate. Gate decisions follow
[the verification protocol](verification/verifiers/REVIEW_PROTOCOL.md).

Include the problem, expected behavior, actual observation, commit/configuration, reproduction steps,
and evidence when reporting a failure. Simulation and dry-run records must remain labeled as such.
Keep failed runs and document exclusions. Publish recordings only when their participants agreed to sharing.

## Dependencies and licensing

Record upstream source, exact revision, license, local modifications, and verification in
`third_party/upstream-register.csv`. The maintainer still needs to select the project license.
