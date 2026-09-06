# Roadmap to v0.1

**Current capability status: no gate completed.** See [STATUS](STATUS.md) for the latest planning snapshot
and [BACKLOG](BACKLOG.md) for task ownership and dependencies.

The original eight-week outline is a pacing hypothesis. Start its clock when the team and compatible
hardware are ready; supplier delays and failed tests change the plan. Do not compress testing to keep a date.

| Gate | Suggested window | Lead | Entry dependency | Exit evidence |
| --- | --- | --- | --- | --- |
| G0 Architecture | Kickoff / first 72 hours | Both + mentor | Shared goal | Reviewed scope, interfaces, compatible BOM direction, stop-path design, and test drafts. |
| G1 Manual robot | Week 1 | Partner | G0; frozen G1 spec | Teleop, encoder, emergency-stop and command-timeout measurements on the chosen base. |
| G2 Navigation | Weeks 2–3 | Partner; Frank reviews | G1 | Defined 20-run SLAM/Nav2 protocol, raw outcomes, interventions, and acceptance verdict. |
| G3 Edge AI | Week 4 | Frank; partner reviews | G2 for gate completion | Model record and measured latency/FPS/accuracy/temperature on RK3588. |
| G4 Target identity | Week 5 | Frank | G3 | Enrollment, distractor and occlusion results; identity-switch and confidence evidence. |
| G5 Following | Week 6 | Both | G4 | Integrated S01–S09 reports within the declared operating envelope. |
| G6 Fault injection | Week 7 | Partner | G5 | S10–S12 plus stale data, MCU link loss, and other required fault results. |
| G7 Independent verification | Week 7 | Independent reviewer + mentor | G6 | All mandatory criteria resolved; evidence-linked release verdict. |
| G8 External reproduction | Week 8 or later | A contributor outside the feature authors | G7 | Reproduction from a pinned revision, complete setup notes, and independent results. |

Software setup, offline learning, and experiment-template practice may run in parallel with hardware
selection. Completing an offline exercise does not advance a gate or authorize an integrated moving test.
G1 already includes protective behavior; G6 expands fault coverage in the integrated following system.

## Learning tied to outputs

| Learn | Use it to produce |
| --- | --- |
| Git, Python, terminal basics | A reproducible change and evidence record another teammate can inspect. |
| Frames, units, timing, odometry | An interface contract and measured motion/calibration results. |
| ROS 2, SLAM, navigation | A repeatable 20-run navigation experiment. |
| Edge AI, quantization, tracking | Measured inference behavior and target-identity failure analysis. |
| Experimental design and statistics | Predeclared criteria, raw outcomes, distributions, and limitations. |
| AI-assisted engineering | A change whose correctness is established independently of its author. |

## After v0.1

After G8, test a following load-carrying prototype with real users. Choose a product direction from those
observations. Delivery, luggage, custom control boards, imitation learning, and multi-robot work remain
future decisions with their own requirements.
