# Pet interaction: requirements and design hypotheses

Status: EXPLORATORY. These are discussion requirements and hypotheses, not a frozen product spec.
Read [the discussion record](DISCUSSION.md) for attribution and [sources](SOURCES.md) for evidence limits.

## The needs to distinguish

| Perspective | Need / question | What is not yet known |
| --- | --- | --- |
| Owner | Offer play or engagement when busy or away. | How common the need is, existing alternatives, acceptable setup/maintenance and willingness to pay. |
| Cat | Be able to approach, play, pause or leave. | Interest, avoidance, repeat interest and the effect of noise, speed, shape and size for each cat. |
| Learners | Understand robotics and make reproducible changes. | Which complete kit best matches their time, budget and support needs. |
| Future unattended product | Operate within a defined household envelope without frequent rescue. | Jam recovery, falls, damage, runtime, cleaning, charging and reliable stopping in that environment. |

Recognition means detecting/locating an animal. Tracking means maintaining its estimated trajectory.
Neither proves enjoyment or reliably identifies emotion. A cat pursuing a toy and a robot pursuing
a cat are different control objectives.

## Form-factor comparison

| Candidate | Potential value | Concrete questions |
| --- | --- | --- |
| Purchased four-wheel learning base | Supported controls, sensors and ROS examples; useful for learning. | Does the exact kit include the working computer/software? What is exposed to paws/fur? How often does it need intervention? |
| Rounded covered wheeled product concept | Room for stable camera viewpoint and accessible stop control. | Weight, stability, wheel openings, entanglement, cleaning and noise. |
| Complete rolling sphere | No fixed wheels-up chassis orientation; internal mechanism can be enclosed. | Can the drive regain motion after a push? Can it stop on the intended floor? Does it jam under furniture or struggle on carpet? |

A rounded cover on a conventional car is not the same mechanism as a rolling spherical shell.
“No fixed upside-down state” is not proof of self-recovery from every contact or obstacle.
Ball size, mass, shell material and speed remain open; the illustrations are not dimensioned designs.

## Spherical mechanism concept

The cutaway proposes an internal weighted carriage, low-mounted battery, controller and
small drive rollers acting on the shell. It is an artist's interpretation, not a mechanical model.
Traction, torque reaction, turning, mass distribution, tolerances, heat and service access
must be engineered or supplied by a mature module vendor before implementation.
No exact motor, battery, board, material, shell thickness or charging mechanism has been selected.

A camera attached to a rolling shell rotates with it. Stable onboard viewing would need its own
mechanical/optical solution. Do not assume ordinary wheeled-robot camera mounting transfers directly.

## Optional architecture: fixed observation plus a simple ball

| Part | Proposed responsibility | Boundary / unresolved item |
| --- | --- | --- |
| Fixed room camera | Observe the cat and ball within its actual view. | Furniture occlusion, blind zones, calibration and lighting. |
| Stationary computer | Explore perception, logging and bounded interaction decisions. | Initially use available supported compute; RK3588 is a possible later backend. |
| Ball controller | Execute bounded motion and monitor local motion/fault state. | Actual sensors, speed limiting, jam detection, timeout and rearm need design and tests. |
| Human operator | Start/stop supervised experiments and interpret observed responses. | Immediate intervention and defined space required for early trials. |
| Evidence review | Compare requirements with recorded observations. | Cannot issue motor commands or turn generated images into test evidence. |

“Connection lost → ball stops” is a proposed requirement, not an observed result.
Distinguish motor disable from physical stopping: a sphere may coast or roll on a slope.
Cloud/AI availability must not be required for local protective behavior.
If perception freezes while communications continue, data freshness needs checking separately.

## Candidate requirement checklist

- [ ] Define intended floor types, boundaries and furniture clearances.
- [ ] Compare voluntary approach and withdrawal with different motion patterns.
- [ ] Choose size/mass and assess noise, impact, enclosure integrity and cleanability.
- [ ] Establish local stopping, command expiry, startup and explicit restart behavior.
- [ ] Identify possible fur/paw entanglement, shell gaps and detachable-part hazards.
- [ ] Observe jams and rescue needs; do not promise autonomous recovery.
- [ ] Resolve battery enclosure, charging method and fault behavior with actual parts.
- [ ] Determine how to handle camera blind spots and stale observations.
- [ ] Keep owner-away operation outside early supervised demonstrations.
- [ ] Record which findings support a product direction and which remain unknown.

Do not put dangling strings, lasers or feeding attachments into the initial concept by default.
They were not required to test the proposed moving-toy interaction.

## Next design decision

First determine whether cats voluntarily engage and whether a ball reduces manual intervention
relative to the available base. Reuse finished modules for this comparison. A custom spherical
robot and a fixed-camera system are optional future routes, not simultaneous new build obligations.
The [two-stage plan](../../../docs/plan/TWO_STAGE_PLAN.md) remains the execution baseline.
