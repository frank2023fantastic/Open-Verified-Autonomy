# Task backlog

Updated 2026-09-06 for the [two-stage plan](TWO_STAGE_PLAN.md).
Existing Issue numbers are retained; scope and dependencies are rescheduled.
Owners are proposed and Harry's GitHub handle remains to be confirmed.

| Task | When | Lead | Depends on | Outcome |
| --- | --- | --- | --- | --- |
| [T01](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/1) | Stage 1 — start | Frank + Harry | None | Confirm Frank/Harry roles, time and Stage 1 budget |
| [T02](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/2) | Stage 1 — understand | Harry | T01 | Explain the chosen kit's data flow and stop controls |
| [T03](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/3) | Stage 1 — select | Harry | T01 | Compare mature complete kits and select a learning baseline |
| [T04](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/4) | Stage 1 — set up | Frank | T01 | Restore the vendor environment and reproduce a first example |
| [T05](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/5) | Stage 1 — before motion | Harry | T02, T03 | Check supervised tutorial motion and stop readiness |
| [T06](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/6) | Later formal validation — deferred | Harry | T08 | Later: define the formal 20-trial navigation protocol |
| [T07](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/7) | Stage 1 — record and review | Frank | T01 | Keep a learning log and rehearse evidence capture |
| [T08](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/8) | Stage 1 — hands-on outcome | Frank + Harry | T03, T04, T05 | Reproduce core tutorials, make one change and review Stage 1 |

T01 starts first. T02/T03/T04 preparation can overlap, with one active implementation task per person.
T04 completion needs the chosen kit; T05 precedes any T08 motion.
T07 accompanies learning and finishes with an actual exercise log.
T06 does not block T08. Unsupported kit examples stay explicitly unresolved.

## T01: Confirm Frank/Harry roles, time and Stage 1 budget

Lead: Frank + Harry. Reviewer: Mentor.

- [ ] Record Harry's GitHub handle and equipment actually available; Harry is Frank's classmate.
- [ ] Agree on weekly time and a Stage 1 complete-kit budget; keep a later RK3588 budget separate.
- [ ] Confirm one owner and a different reviewer per task; both teammates should operate the kit.
- [ ] Record the maintainer responsible for the pending license decision.

## T02: Explain the chosen kit's data flow and stop controls

Lead: Harry. Reviewer: Frank + mentor.

Start from candidate documentation, then finish against the selected T03 kit. Designing a replacement controller or full safety supervisor is not this task.

- [ ] Sketch the vendor system: sensors, computer, ROS nodes, controller and motors; annotate sources and unknowns.
- [ ] Locate manual/autonomous command selection, units, measured encoder feedback and actual stop controls.
- [ ] Read the vendor's command-loss, startup and rearm behavior; use this in T05 before floor motion.
- [ ] Both teammates explain the flow and compare it with the project's three-plane target; log gaps without implementing every project interface now.

## T03: Compare mature complete kits and select a learning baseline

Lead: Harry. Reviewer: Frank + mentor.

Replace the earlier bare-chassis/C30D-first procurement direction. No exact kit is selected by this issue. The earlier L150 proposal remains a historical Stage 2 reference. Formal G0 supplier-evidence requirements remain in the unchanged specification.

- [ ] Compare three mature complete-kit candidates using dated product, tutorial and source links; record unknown answers honestly.
- [ ] Prioritize reproducible ROS 2 tutorials, a recoverable supplied image, accessible source/protocols, support, stop controls and complete working sensor/compute combinations.
- [ ] Get an itemized current quote for the preferred package including computer, sensors, controller, battery, charger and necessary accessories; record the decision within the agreed budget.
- [ ] Check whether the controller and sensors can later be reused with a different computer. Treat RK3588 compatibility as future investigation, not a Stage 1 purchase gate.
- [ ] Explain the chosen geometry; differential drive remains preferred for v0.1, while an easier mature kit with another geometry needs an explicit learning-only tradeoff and future reuse note.

## T04: Restore the vendor environment and reproduce a first example

Lead: Frank. Reviewer: Harry.

PC preparation may start after T01; completion needs the selected kit or a clearly identified available equivalent. Motion examples require T05 first.

- [ ] Record the actual development computer; after T03 selection pin the supplied board, vendor image, ROS 2 and firmware versions.
- [ ] Record backup/recovery instructions and preserve the original configuration before editing.
- [ ] Follow the official quick start and reproduce a non-motion example such as camera viewing or telemetry; record exact commands, errors and sources.
- [ ] Have Harry repeat the setup/restart from the notes; distinguish exercised steps from recovery instructions not yet tested.
- [ ] Use the vendor-supported runtime first. Do not require RKNN conversion, a custom OS image or RK3588 migration.

## T05: Check supervised tutorial motion and stop readiness

Lead: Harry. Reviewer: Frank + mentor.

- [ ] Record the exact vendor procedure, operator/observer, bounded test area, actual low-speed setting and immediately accessible physical drive stop.
- [ ] Check power, mounts, cables and startup/disarmed behavior against vendor documentation; use a supported secured-base setup for initial movement checks.
- [ ] Observe manual stop, command/link loss and explicit restart behavior before floor motion; record coasting or braking and unresolved behavior.
- [ ] Review readiness with the mentor; if stopping cannot be established, continue non-motion learning and resolve it with the supplier.
- [ ] Record the limited scope and results as tutorial observations, with no G1 PASS or assumed stopping distance.

Preserved formal work: Before qualifying G1 runs, still resolve numerical speed/timeout/stop-time/stop-distance limits and uncertainty, trial counts, measured-stop definition, process-crash/link-loss tests and rearm checks. A separate reviewer must review and freeze the full G1 specification. These original requirements move to T09's formal entry preparation; tutorial readiness does not satisfy them.

## T06: Later: define the formal 20-trial navigation protocol

Lead: Harry. Reviewer: Frank.

Not a prerequisite for the first manual run or vendor navigation tutorial. Preserve failed learning attempts separately; do not relabel selected tutorial successes as the formal 20 trials.

- [ ] Use the reproduced vendor mapping/navigation baseline to choose a route, reset procedure, pose reference and per-trial timeout.
- [ ] Set the required success count out of 20 and intervention/failure rules before qualifying tests.
- [ ] Define speed, clearance and localization/data-loss behavior and measurement methods.
- [ ] Record review and complete hardware-dependent details before freezing the qualifying specification.

## T07: Keep a learning log and rehearse evidence capture

Lead: Frank. Reviewer: Harry.

- [ ] For each exercise record goal, kit/software version, source tutorial, actual commands, expected/observed behavior, failures and next step.
- [ ] Link an actual screenshot, video or telemetry record when available; the teammate repeats or reviews the observation.
- [ ] Optionally rehearse the seven-file format with new_experiment.py as dry_run; keep NOT_RUN / NOT_REVIEWED and never invent measurements.
- [ ] Record where evidence lives and what instrumentation is missing. Complete one real learning log as T04/T08 work proceeds.

Preserved formal work: The seven-file dry-run exercise remains mandatory before formal G0 completion under its existing specification. Full qualifying evidence bundles are not required for every initial learning exercise; actual physical tutorials must not be labeled dry_run.

## T08: Reproduce core tutorials, make one change and review Stage 1

Lead: Frank + Harry. Reviewer: Mentor + teammate who did not author the change.

No kit demonstrations or learning milestones complete G0–G8. The former T08 formal G0/G1 readiness review is preserved as a prerequisite to T09 in BACKLOG and ROADMAP. RK3588 migration is not automatically authorized by a successful demo.

- [ ] Start with a bounded manual-control exercise after T05; do not wait for the formal 20-trial protocol.
- [ ] Progress through sensor reading, vendor mapping/navigation and, where supplied, visual-following examples. Review each motion mode's stopping and supervision needs before use; record missing/unsupported features explicitly.
- [ ] Explain the relevant data/control flow and have both teammates restart and operate the baseline from notes.
- [ ] Make one reversible, understood change such as extra wheel-telemetry logging or a lower speed cap; keep a diff, rollback and before/after observation.
- [ ] Record one real failure, investigate it and document a repeat check; use T07's lightweight log.
- [ ] Review what each teammate can explain and reproduce. Record whether to keep learning, pursue formal validation on the kit, or prepare an RK3588 desktop comparison with a concrete motivation.

## Later formal work: T09–T12

These have no active Issues yet. Split them into bounded tasks when ready.
Formal verification can use the mature kit; RK3588 is not an entry dependency.

- **T09 / G1:** after T08, complete the former T08 formal G0 review: actual supplier/compatibility
  evidence, G1/G2 drafts, required seven-file dry-run record and human G0 decision.
  Complete and independently freeze G1 criteria (the deferred T05 work), confirm fixture/operator/
  recorder readiness, then execute and cross-review manual-control and stop trials.
- **T10 / G2:** after T09 and T06, pin map/description/drivers, run all 20 qualifying trials,
  preserve failures/interventions, calculate metrics and record the G2 decision.
- **T11 / G3–G4:** after T10 for gate decisions, benchmark the chosen backend and enrolled-target
  identity under separately frozen specifications. Offline learning can happen earlier.
  Resolve any backend-specific draft wording before freeze; detection FPS is not identity evidence.
- **T12 / G5–G8:** after G4, split following, integrated fault injection, independent review and
  external reproduction into tasks. Preserve S01–S12 and supplementary required fault coverage.

## Later platform work: T13 — RK3588 desktop comparison

Create an Issue when T08's review identifies a concrete motivation, budget and owner.
Keep the original system working. Compare equivalent sensor/model inputs on a selected RK3588
board without motor authority, record power/thermal/driver limits, then decide whether migration
is justified. Revalidate motion and fault behavior before adopting the new computer.
This task does not inherit a capability verdict from either platform.

Closing a learning task completes its documented scope only; all gate decisions remain separate.
