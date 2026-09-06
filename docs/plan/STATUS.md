# Project status

Snapshot: 2026-09-06. Update this file when a gate decision or material plan change is recorded.
GitHub Issues track individual task execution; this file tracks capability evidence.

| Area | Status | Meaning |
| --- | --- | --- |
| Mission and README | Published | The project direction is documented. |
| Repository structure and startup plan | Prepared | Directories, drafts, and experiment templates are available. |
| Architecture and interfaces | Draft | Hardware-specific details and team review remain open. |
| G0 | NOT VERIFIED | Scaffold exists; team, hardware selection, and reviews are incomplete. |
| G1–G8 | NOT VERIFIED / NOT RUN | No qualifying robot test evidence is in this repository. |
| Hardware/OS/model selection | Pending | No exact platform combination is claimed compatible. |
| Runtime software and firmware | Not implemented here | Module directories contain integration instructions only. |
| Experiment helper | Scaffold utility | Creates records; does not execute or verify robot tests. |
| Project license | Pending maintainer decision | No project license has been selected by this scaffold. |

## Immediate learning plan

Stage 1: select a mature complete kit, restore its supported environment, check stop controls,
reproduce tutorials and make one reversible change. Stage 2: investigate RK3588 after the
baseline and a documented motivation. See [TWO_STAGE_PLAN](TWO_STAGE_PLAN.md).
No kit, learning outcome or migration is claimed completed by this plan update.

Immediate open items: Harry's GitHub handle, role acceptance, availability, Stage 1 budget,
kit selection and first non-motion setup. T06's formal 20-trial plan is deferred until after T08.

## Later blockers to formal G0 completion

1. Record Harry's GitHub handle, confirm team availability, and document available equipment and budget. Harry is Frank's classmate; his identity is recorded in [TEAM](TEAM.md).
2. Obtain actual protocol, watchdog, and electrical stop-path evidence from candidate suppliers.
3. Resolve the selected kit's OS/ROS 2/driver compatibility; RKNN compatibility is later RK3588 work.
4. Complete hardware-specific limits and measurement methods in G1/G2 specifications.
5. Record a team/mentor review of the architecture and test plan.

Next work: [T01–T04 preparation](BACKLOG.md), then T05 before T08 motion; T07 accompanies learning.
Keep no more than one active implementation task per person. Formal G0–G8 verdicts remain unchanged.
