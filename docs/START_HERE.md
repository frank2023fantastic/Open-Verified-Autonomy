# Start here: the first 72 hours

The first outcome is a shared, testable G0 plan and a reproducible development baseline.
The repository scaffold is ready; no hardware or autonomy gate has passed.
Times below are suggested working sessions, not deadlines that override evidence.

## Session 1: agree on the work (about 2 hours)

Both teammates read the README and [three-plane architecture](architecture/three-plane-v0.1.md).
Each explains the goal, stop authority, and what could make a demo misleading.

- Frank owns product scope, perception/identity, GitHub organization, and English build logs.
- Harry, Frank's classmate and robotics/test partner, is proposed to lead chassis integration, navigation, and test setup; confirm the working agreement in T01.
- Record Harry's GitHub handle, available equipment, available time, and one owner per task in [TEAM](plan/TEAM.md).
- Start T01 and T02 from [BACKLOG](plan/BACKLOG.md). Add questions to the task; do not guess hardware facts.

Output: a short shared scope statement, named task owners, and an annotated interface draft.

## Session 2: select a compatible starting platform

Harry compares at least three chassis suppliers using [the supplier checklist](../hardware/supplier-checklist.md).
Frank records the existing development computer and candidate board software combinations using
[the development setup record](setup/development-environment.md).

Check open command/encoder protocols, MCU command timeout, the actual electrical stop path,
ROS 2 documentation, and whether the main computer can be omitted from the chassis order.
Record dated quotes and evidence in the BOM and selection record. Unknown answers stay unknown.
The first implementation target can be an available computer and simulation while selection continues.

Output: supplier comparison and one candidate system with unresolved compatibility items.

## Session 3: make G1 and G2 measurable

Together review [G1](../verification/specs/G1-manual-robot.yaml) and
[G2](../verification/specs/G2-navigation.yaml).
Choose the test area, measured limits, repetition counts, instruments, and stop criteria.
Define both fault-to-stop time and physical stopping distance. Record who reviewed the criteria.
Do not turn a null threshold into a made-up value just to complete the file.

Output: versioned acceptance drafts ready for hardware-specific review. Freeze only after required
fields and measurement methods are resolved, before the corresponding qualifying experiment.

## Session 4: rehearse the evidence workflow

From the repository root, with Python 3.9 or newer:

```bash
python3 tools/new_experiment.py --run-id practice-001 --gate G1 --mode dry_run
```

This creates `experiments/practice-001/` with seven record templates. It does not run the robot or a test.
The folder is a practice record; keep `NOT_RUN` / `NOT_REVIEWED` and do not put invented measurements in it.
Walk through how real timestamps, wheel speed, video, hashes, metrics, and a second person's review will connect.
Use a fresh run ID for the later real experiment.

Output: one clearly labeled practice record and a list of logging gaps. See [experiment instructions](../experiments/README.md).

## Next: G0 review, then G1

Use [G0 acceptance](../verification/specs/G0-architecture.yaml) to review scope, interfaces,
hardware compatibility, and the test plan. Completing the scaffold alone does not satisfy G0.
After G0 and the G1 specification are ready, follow [the bench bringup checklist](../hardware/bringup-checklist.md).

Each person records one finding, one unresolved question, and one next action. The first short build log
should explain the goal and the most likely failure modes. Use [the roadmap](plan/ROADMAP.md) to see what follows.
