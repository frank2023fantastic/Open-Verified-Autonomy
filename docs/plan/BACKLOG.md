# Task backlog

GitHub Issues are the execution record. This file defines task scope and dependency order.
Initial Issues are created for T01–T08; T09–T12 are later work to expand when entry evidence is ready.
Owner roles below are proposed. Record named owners/reviewers at kickoff; no GitHub assignee is presumed.

| Task | Gate | Lead | Depends on | Deliverable |
| --- | --- | --- | --- | --- |
| T01 | G0 | Frank + partner | None | Confirm team roles, equipment and working agreement |
| T02 | G0 | Partner | T01 | Review command authority, interfaces and the stop path |
| T03 | G0 | Partner | T01 | Compare three chassis suppliers and propose a compatible BOM |
| T04 | G0 | Frank | T01 | Record the development environment and first reproducible setup |
| T05 | G0/G1 | Partner | T02, T03 | Complete hardware-specific G1 acceptance and measurement methods |
| T06 | G0/G2 | Partner | T02, T04 | Define the 20-trial navigation protocol |
| T07 | G0 | Frank | T04 | Rehearse evidence capture with one labeled dry-run record |
| T08 | G0/G1 | Both | T03, T04, T05, T06, T07 | Review G0 readiness and prepare the first manual-robot test |
| T09 | G1 | Partner | T08 | Execute and cross-review manual control and stop tests |
| T10 | G2 | Partner | T09 | Implement navigation and execute the frozen 20-trial protocol |
| T11 | G3/G4 | Frank | T10 | Benchmark edge perception and build enrolled-target identity |
| T12 | G5-G8 | Both | T11 | Integrate following, inject faults and obtain independent reproduction |

## Execution rules

- T01 starts first. T02/T03/T04 can be divided between the two teammates after kickoff.
- Keep one active implementation task per person; pair on interface and physical-test review.
- A dependency is complete only when its checklist and relevant evidence are recorded.
- Closing a task does not close a gate. Record actual gate decisions separately.
- T08 prepares G1; it does not fabricate a completed manual-robot test.
- Later tasks are deliberately coarse and must be split before implementation.

## T01: Confirm team roles, equipment and working agreement

Gate: G0. Lead: Frank + partner. Reviewer: Mentor.

Files: `docs/plan/TEAM.md`, `docs/plan/STATUS.md`.

- [ ] Record partner name/handle and equipment actually available.
- [ ] Agree on time and hardware spending envelope.
- [ ] Choose one owner and a different reviewer per first task.
- [ ] Record the maintainer responsible for the pending license decision.

## T02: Review command authority, interfaces and the stop path

Gate: G0. Lead: Partner. Reviewer: Frank + mentor.

Files: `docs/architecture/three-plane-v0.1.md`, `docs/architecture/interfaces-v0.1.md`.

- [ ] Both teammates explain the three-plane boundary.
- [ ] List units, frames, clocks and the command-expiry contract.
- [ ] Record the required electrical stop behavior and hardware questions to ask suppliers.
- [ ] Record review findings and the owner of each unresolved item.

## T03: Compare three chassis suppliers and propose a compatible BOM

Gate: G0. Lead: Partner. Reviewer: Mentor + Frank.

Files: `hardware/bom.csv`, `hardware/selection.md`.

- [ ] Collect dated answers from at least three suppliers.
- [ ] Attach protocol/source, watchdog, stop-path and ROS 2 evidence.
- [ ] Confirm whether the base can be bought without the main computer.
- [ ] Record itemized prices and a recommended combination with unresolved compatibility items.

## T04: Record the development environment and first reproducible setup

Gate: G0. Lead: Frank. Reviewer: Partner.

Files: `docs/setup/development-environment.md`, `third_party/upstream-register.csv`.

- [ ] Record the actual development computer and OS.
- [ ] Choose and document a candidate ROS 2/simulator setup from official sources.
- [ ] Exercise a minimal setup example and preserve exact commands/errors.
- [ ] Separate PC-only setup from untested RK3588/driver compatibility.

## T05: Complete hardware-specific G1 acceptance and measurement methods

Gate: G0/G1. Lead: Partner. Reviewer: Frank + mentor.

Files: `verification/specs/G1-manual-robot.yaml`, `hardware/bringup-checklist.md`.

- [ ] Resolve speed, command timeout, stopping time/distance and measurement uncertainty.
- [ ] Define repetitions, measured-stop condition and explicit rearm checks.
- [ ] Include physical stop, process crash and MCU link-loss trials.
- [ ] Record independent review and freeze only when all required fields are resolved.

## T06: Define the 20-trial navigation protocol

Gate: G0/G2. Lead: Partner. Reviewer: Frank.

Files: `verification/specs/G2-navigation.yaml`.

- [ ] Define route/reset procedure, pose reference and per-trial timeout.
- [ ] Set the required success count out of 20 and intervention/failure rules before tests.
- [ ] Define speed, clearance and localization/data-loss behavior.
- [ ] Record review; complete hardware-dependent details before freezing the qualifying spec.

## T07: Rehearse evidence capture with one labeled dry-run record

Gate: G0. Lead: Frank. Reviewer: Partner.

Files: `experiments/`, `verification/verifiers/REVIEW_PROTOCOL.md`.

- [ ] Use new_experiment.py to create a uniquely named dry_run directory.
- [ ] Explain where each metadata field, timestamp and raw artifact will come from.
- [ ] Record missing instrumentation and storage decisions.
- [ ] Keep practice results NOT_RUN / NOT_REVIEWED; review does not claim physical evidence.

## T08: Review G0 readiness and prepare the first manual-robot test

Gate: G0/G1. Lead: Both. Reviewer: Mentor.

Files: `verification/specs/G0-architecture.yaml`, `hardware/bringup-checklist.md`, `docs/plan/STATUS.md`.

- [ ] Review the actual G0 evidence and record open blockers.
- [ ] Record a supported G0 verdict/decision without treating scaffold checks as robot evidence.
- [ ] Confirm G1 specification, test fixture, operator, stop access and recorder readiness.
- [ ] Identify the next bounded bench task; run it only when its entry conditions are met.

## T09: Execute and cross-review manual control and stop tests

Gate: G1. Lead: Partner. Reviewer: Frank + mentor.

Files: `firmware/`, `ros2_ws/src/`, `experiments/`, `docs/plan/STATUS.md`.

- [ ] Implement only the required base interface and logging.
- [ ] Execute the frozen G1 protocol on the actual base.
- [ ] Retain all trials, failures and measured stopping evidence.
- [ ] Record independent review and human gate decision.

## T10: Implement navigation and execute the frozen 20-trial protocol

Gate: G2. Lead: Partner. Reviewer: Frank.

Files: `ros2_ws/src/`, `experiments/`, `docs/plan/STATUS.md`.

- [ ] Pin the robot description, map, driver and navigation configuration.
- [ ] Execute all 20 scheduled trials and retain interventions/failures.
- [ ] Calculate metrics from raw results.
- [ ] Cross-review evidence and record the G2 decision.

## T11: Benchmark edge perception and build enrolled-target identity

Gate: G3/G4. Lead: Frank. Reviewer: Partner.

Files: `ai/`, `ros2_ws/src/`, `verification/specs/G3-edge-ai.yaml`, `verification/specs/G4-target-identity.yaml`.

- [ ] Freeze each gate specification before its qualifying runs.
- [ ] Record reproducible model conversion and sustained RK3588 measurements.
- [ ] Implement explicit enrollment and identity/uncertainty policy.
- [ ] Complete separate G3 then G4 evidence decisions; do not infer identity quality from detection FPS.

## T12: Integrate following, inject faults and obtain independent reproduction

Gate: G5-G8. Lead: Both. Reviewer: Independent reviewer + external reproducer.

Files: `verification/`, `experiments/`, `docs/setup/`, `media/`.

- [ ] Split this later work into bounded Issues when G4 evidence is ready.
- [ ] Complete S01-S12 and supplementary required faults under frozen criteria.
- [ ] Independently review evidence and challenge the verifier with negative cases.
- [ ] Publish a pinned, reproducible core demo and independent build log.
