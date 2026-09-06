# Team and working agreement

Harry is Frank's classmate and project collaborator, confirmed on 2026-09-06.
These are proposed working responsibilities based on the project direction. Confirm role acceptance and availability in T01.

| Role | Primary work | Cross-review |
| --- | --- | --- |
| Frank — Product and AI lead | Scope, repository, perception, target identity, model benchmarks, English build logs | Reproduce navigation/telemetry checks written by the partner. |
| Harry — Robotics and test partner | Chassis, MCU protocol, odometry, LiDAR/SLAM/Nav2, physical setup, fault injection | Replay and challenge Frank's perception/identity results. |
| Mentor | System boundaries, hardware/stop-path review, major tradeoffs, gate decisions | Check that evidence supports claims and that the scope remains manageable. |
| AI builder | Draft code, configuration, documentation, and test tooling | Supplies changes and assumptions; cannot independently certify its own work. |
| Independent reviewer/verifier | Challenge criteria and inspect source evidence | Does not repair the implementation and then certify that same repair. |

## Fill in at kickoff

- Partner name: **Harry — Frank's classmate**
- Harry's GitHub handle: **TBD**
- Existing computer and equipment: **TBD**
- Time available per person: **TBD**
- Agreed hardware spending envelope: **TBD**
- Mentor/reviewer for the first physical test: **TBD**
- Project license decision owner: **Frank / maintainer; decision pending**

## Working rhythm

- Keep one active implementation task per person. Pair on interfaces and physical fault tests.
- At handoff: link the commit, describe the observation, name the remaining gap, and identify the next owner.
- At a weekly check-in: demonstrate one measured result, inspect one failure, and select the next ready task.
- Use task dependencies to choose work. Record blockers promptly instead of quietly expanding scope.
- A gate review is triggered by evidence readiness. Calendar dates are planning aids only.
