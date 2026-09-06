# Start here: learn on a mature robot

Frank and Harry's first outcome is a reproducible vendor baseline and practical understanding.
Use the [two-stage plan](plan/TWO_STAGE_PLAN.md): mature complete kit now, RK3588 later.
No robot capabilities or evidence gates have been completed.

## 1. Agree and select

Start [T01 / Issue #1](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/1):
confirm Harry's GitHub handle, available equipment, weekly time, roles and Stage 1 budget.
Frank is proposed to lead software/perception; Harry chassis integration/navigation.
Both should operate the kit and review each other's changes.

In T03 compare three complete learning kits, prioritizing tutorials, recoverable supplied software,
source/protocol access, stop behavior and included hardware. Use [supplier questions](../hardware/supplier-checklist.md).
Use the selected kit's supported computer; RK3588 compatibility is a later question.

## 2. Get a reproducible baseline

T04 records the actual PC and vendor image, sources, versions and backup/recovery procedure.
Start with non-motion examples: camera viewing, sensor readings and telemetry.
Have the other teammate repeat the startup from notes.
T02 maps the actual data/control flow and identifies stop controls and unknowns.

## 3. Run bounded tutorials

Complete T05's motion-readiness checks under the [two-stage plan](plan/TWO_STAGE_PLAN.md)
before supervised manual movement. Resolve unclear stopping behavior with the supplier.
Proceed through vendor sensor, mapping/navigation and available vision tutorials in T08,
reviewing requirements before each new motion mode.
The formal 20-trial navigation protocol is later work, not a prerequisite for this first manual run.

## 4. Understand and change one thing

Keep T07's short learning log from the beginning: goal, version, commands, observation, failure,
evidence and next action. Make a reversible change such as logging measured wheel speed or
lowering a speed cap, preserve rollback, and have the teammate repeat the result.
Investigate a real failure; do not invent one to complete a checklist.

## Next decision

Review T08's learning outcomes. Continue learning where understanding is missing.
Formal verification on the kit and a motivated RK3588 desktop comparison are possible next steps;
neither requires replacing working hardware immediately.

G0–G8 remain uncompleted. Full frozen acceptance and evidence records apply before qualifying
tests; vendor tutorial outcomes are learning observations. See [ROADMAP](plan/ROADMAP.md),
[BACKLOG](plan/BACKLOG.md) and [STATUS](plan/STATUS.md).
