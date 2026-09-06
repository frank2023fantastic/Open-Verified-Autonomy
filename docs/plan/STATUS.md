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

## Current blockers to G0 completion

1. Record partner identity, available equipment, and budget.
2. Obtain actual protocol, watchdog, and electrical stop-path evidence from candidate suppliers.
3. Resolve OS/ROS 2/driver/RKNN compatibility for the chosen components.
4. Complete hardware-specific limits and measurement methods in G1/G2 specifications.
5. Record a team/mentor review of the architecture and test plan.

Next work: [T01–T04](BACKLOG.md), with no more than one active implementation task per person.
