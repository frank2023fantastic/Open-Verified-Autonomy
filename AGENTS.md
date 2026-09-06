# Working in Open Verified Autonomy

Read `README.md`, `docs/START_HERE.md`, and `docs/plan/STATUS.md` before changing this repository.

- Keep repository documentation in English. Explain the work to the user in their preferred language.
- v0.1 is a supervised, low-speed indoor differential-drive platform for following one enrolled target.
- Preserve the Autonomy / Safety / Verification boundaries. Generative AI cannot override motor protection.
- Follow docs/plan/TWO_STAGE_PLAN.md: Stage 1 uses a mature complete robot with its supported computer/image; RK3588 is a longer-term Stage 2 direction, not a starting dependency. Exact kit and later board choices remain open.
- Distinguish supervised vendor learning exercises from qualifying G0–G8 tests. Use the Stage 1 motion-readiness checks before tutorials; retain complete frozen criteria and independent evidence requirements for verified claims.
- Use the default `main` workflow. Do not create branches or PRs unless requested. Refresh remote state before writing; never force-push or overwrite another contributor's work.
- Make small commits scoped to the assigned task. Record the task ID, what changed, and what was checked.
- The current repository is a planning scaffold. Do not describe templates, generated examples, or documentation checks as tested robot capabilities.
- All acceptance YAML starts as DRAFT. Missing thresholds and unresolved measurement methods prevent freezing a specification.
- Never invent hardware readings, run counts, model benchmarks, supplier quotes, or a PASS verdict.
- Preserve failed runs. Distinguish dry runs, simulation, replay, and physical tests in every report.
- Builder and verifier are separate roles. Do not alter the implementation or criteria while acting as its independent verifier.
- Keep large raw recordings and model binaries outside normal Git; commit retrievable evidence indexes and integrity hashes.
- Reuse upstream work with version and license records. Do not invent a license decision for this project.
- Add working setup instructions only when the corresponding implementation exists and has been exercised.
- Scope validation to the change. A documentation/tooling check cannot complete a robot evidence gate.
