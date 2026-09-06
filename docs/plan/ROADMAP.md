# Roadmap: learning first, verified autonomy next

Current status: no learning milestone or G0–G8 gate is claimed complete.
See [TWO_STAGE_PLAN](TWO_STAGE_PLAN.md), [BACKLOG](BACKLOG.md) and [STATUS](STATUS.md).

| Stage | Work | Exit / next decision |
| --- | --- | --- |
| 1 — Mature kit baseline | Select complete kit; restore vendor environment; understand controls; check stopping; reproduce tutorials; log failures; make one reversible change | Frank and Harry can explain and repeat the baseline and modification. Review remaining gaps. |
| 2 — RK3588 direction | Define motivation; desktop compatibility/inference comparison; preserve original baseline; integrate only after review | Measured comparison and decision to migrate, iterate or keep the kit. Revalidate affected behavior. |

The former eight-week outline is retired as an immediate schedule.
Estimate effort after the kit and teammate availability are known.
Stage 1 is not a renamed verification gate; Stage 2 is not a requirement for starting formal
verification on the mature kit. It is a later platform investigation.

## Formal capability gates

These retain their existing sequence and acceptance requirements. No dates override evidence.

| Gate | Lead (proposed) | Entry | Exit evidence |
| --- | --- | --- | --- |
| G0 Architecture | Frank + Harry + mentor | Actual kit knowledge and selection evidence | Reviewed scope, interfaces, supplier comparison, stop path, compatibility, G1/G2 drafts and required dry-run record. |
| G1 Manual robot | Harry; Frank + mentor review | G0 and frozen G1 spec | Measured manual motion, encoders, physical stop, command timeout and rearm. |
| G2 Navigation | Harry; Frank reviews | G1 and frozen G2 spec | Formal 20-trial report, raw outcomes, interventions and verdict. |
| G3 Edge AI | Frank; Harry reviews | G2 for gate completion; frozen backend-specific spec | Model/version record; accuracy, latency, FPS and thermal observations on the selected backend. |
| G4 Target identity | Frank | G3 | Enrollment, distractor, occlusion and identity-continuity evidence. |
| G5 Following | Both | G4 | Integrated S01–S09 evidence. |
| G6 Fault injection | Harry | G5 | S10–S12 and supplementary stale-data/link-loss faults. |
| G7 Independent verification | Independent reviewer + mentor | G6 | Evidence-linked verdict; required gaps resolved. |
| G8 External reproduction | Contributor outside feature authors | G7 | Independent setup and results from a pinned revision. |

T08 now reviews the learning baseline. Its former formal G0/G1 review is preserved at T09 entry.
T06's formal navigation plan is deferred until baseline tutorial experience, before qualifying G2 runs.
Qualifying tests still require the complete frozen criteria; learning observations cannot be
retroactively promoted into passing trials.

## Continuing contribution

Learn Git/Python through reproducible changes; ROS through observed nodes, frames and telemetry;
AI through measured model behavior; scientific reasoning through recorded failures and cross-review.
Extend the evidence workflow as experiments become more demanding.
Delivery, outdoor use, custom boards and end-to-end learned control remain future scope decisions.
