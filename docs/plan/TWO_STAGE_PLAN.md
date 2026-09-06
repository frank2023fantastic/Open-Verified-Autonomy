# Two-stage learning and platform plan

Planning direction updated 2026-09-06 following the project sponsor's proposal:
**learn on a mature complete robot first; retain RK3588 as a longer-term platform direction.**
No kit has been selected, purchased or tested by this update.

## Stage 1: reproduce, understand, modify

Frank and Harry begin with an assembled robot and the vendor-supported computer, image,
controller and sensors. Prefer a complete ROS 2 learning path, readable source/protocols,
recoverable software and responsive support. Differential drive remains preferred for the
v0.1 mission; document any different geometry as a learning-platform tradeoff.
Buy finished hardware. Custom PCBs, motor drivers and power supplies are outside this stage.

Follow the vendor sequence: non-motion setup and sensors, supervised manual control,
mapping/navigation, and available vision examples. Retain the supplied working configuration
and record exact versions before changing anything. A visual-following demo may be unavailable
or fail; record this instead of treating advertised functionality as achieved.

### Before tutorial motion

These are bounded learning exercises, not qualifying G0/G1 experiments.
T02/T05 must establish the chosen kit's real stop controls, command-loss behavior and
startup/rearm behavior. Record the operator and observer, chosen low-speed setting,
clear test area and accessible physical drive stop. Check initial behavior with the base
secured as its documentation requires, then review readiness before floor motion.
A wireless handset alone is not proof of an independent stop.
If behavior is unknown or inadequate, keep learning with motion disabled and ask the supplier.

Review the additional stop/sensor requirements before each autonomous tutorial.
Do not bypass protections to run an example. Wheels-lifted observations cannot establish floor
stopping distance, and vendor procedures are not a safety certification.

### Learning records

For an exercise, record its goal, tutorial/version, configuration, commands, expected result,
observed result, evidence link, failure and next action. Use a short Issue note or Markdown log.
Identify physical, simulation and replay observations accurately. A dry run is record-format
practice, not a name for an actual moving robot. Preserve unsuccessful attempts.

The full seven-file evidence workflow and frozen acceptance specifications remain required
for qualifying verification work. Practice the format when useful; it need not block the
first non-motion learning exercise.

### Stage 1 exit review

- Both teammates can restart and operate the baseline from their own notes.
- They can explain sensor-to-computer-to-controller data and command flow.
- They have recorded the basic tutorial outcomes and any unsupported capabilities.
- They have made one reversible change with a diff, rollback and before/after observation.
- They have investigated one real failure and documented a repeat check.
- They can state what the platform does, what remains unverified and what to work on next.

A demo video alone is not sufficient. Missing outcomes lead to another learning task, not an
automatic platform replacement. No fixed eight-week deadline applies to this learning stage.

## Stage 2: RK3588 investigation and migration

Start when Stage 1 understanding is established and the team records a concrete reason:
for example a measured latency limit, a deployment constraint, a cost target or an explicit
edge-computing learning objective. The RK3588 direction is retained; purchase and migration
timing depend on this review, available time and budget.

1. Preserve the original kit as the reference and rollback configuration.
2. Select an RK3588 board/image and check power, cooling, interfaces and drivers on the desk.
3. Reproduce camera/recorded-data inference and LiDAR/telemetry handling without motor authority.
4. Compare equivalent inputs and settings: accuracy, end-to-end latency, dropped frames,
   sustained temperature and power where measurable. Pin versions and record measurement limits.
5. Review compatibility and the stop path before connecting motor control; revalidate affected
   motion and fault behavior. Do not assume the old platform's results transfer.

Reuse the chassis, MCU, sensors, maps, logs and interface knowledge where compatibility permits.
If migration offers insufficient benefit or is blocked, retain the working kit and record why.

## Relationship to G0–G8

Learning stages schedule work. G0–G8 describe evidence needed for verified capability claims.
Neither a tutorial nor an RK3588 migration completes a gate.

After the baseline, formal verification may proceed on the mature kit without waiting for RK3588.
Before qualifying G1 work, review actual G0 evidence, complete the required seven-file dry run,
resolve the G1 specification and freeze it with independent review. T06 prepares the formal
20-trial G2 protocol after practical navigation experience; it does not block first manual motion.

The existing G0–G8 YAML criteria remain DRAFT and unchanged by this planning update.
Where a draft still describes RK3588-specific measurements, review and version it for the exact
backend before freezing; never silently reuse a mismatched acceptance record.
The Autonomy / Safety / Verification boundaries and the enrolled-target v0.1 mission remain.

See [BACKLOG](BACKLOG.md) for the rescheduled Issues and [ROADMAP](ROADMAP.md) for formal gates.

## Optional application exploration: pet play

[The pet-robot process archive](../../media/concepts/2026-09-06-pet-robot/README.md) preserves the
need signal from Harry's mother, Koala's ball-shape hypothesis and alternative designs.
Use it as discussion input to T08 after kit/stop readiness. The team-reported L150 Pro four-wheel
candidate still needs its exact complete-package support confirmed in T03.
A ball-versus-base interaction comparison may use suitable purchased devices; it does not require
custom spherical mechanics, fixed-room cameras or RK3588 work now. Record a separate scope
and test decision before treating pet interaction as a formal project capability.
