# Discussion record: from a learning robot to pet interaction

Date: 2026-09-06. Source: the project sponsor's conversation, supplied seller material,
and a shared chat screenshot. English summaries below are paraphrases, not a verbatim transcript.
No supplier response, purchase, physical experiment or demand validation was produced in this session.

## Contributions and evolution

| Step | Contributor / input | Substance | Resulting status |
| --- | --- | --- | --- |
| 1 | Project sponsor | Buy mature hardware and integrate it; do not design the initial chassis/electronics. RK3588 is of interest. | Hardware integration direction. |
| 2 | Earlier assistant proposal | Investigate L150 differential mechanics with a factory-configured C30D, subject to availability/protocol evidence. | Later superseded for initial procurement; historical proposal retained in the repository. |
| 3 | Project sponsor | Harry is Frank's classmate and collaborator. | Team identity recorded; role acceptance and GitHub handle remain open. |
| 4 | Project sponsor | First gain practical experience with a mature supported solution; RK3588 is a long-term plan. | Two-stage plan and Issues #1–#8 rescheduled. |
| 5 | Team choice reported by sponsor | Frank and Harry are considering the pictured L150 Pro four-wheel-drive package. | Candidate, not a documented complete ROS 2 kit or purchase. |
| 6 | Harry's mother, relayed by Frank | Pet owners who travel may want an automatic way to engage their cats. | One owner-originated need signal; prevalence and willingness to pay unknown. |
| 7 | Frank, discussing with Harry | Use recognition/tracking so a cat can chase or seek the robot. | Proposed interaction application. |
| 8 | Assistant assessment | Tracking the cat is different from pursuing it. First observe voluntary approach and supervised interaction. | Proposed experiment, not an approved animal-use protocol or tested feature. |
| 9 | Sponsor's wife Koala | Could a spherical shape avoid overturning and suit play while an owner is away? | Form-factor and unattended-use hypotheses. Koala is a person, not an animal mascot. |
| 10 | Assistant assessment | A complete rolling shell has no fixed wheels-up orientation, but can still jam, lose traction or fall. Internal drive recovery remains a design question. | Plausible benefit; engineering and animal suitability unverified. |
| 11 | Assistant design suggestion | Separate fixed-room observation and stationary compute from a simple rolling ball with local protection. | Optional architecture to investigate; not a selected implementation. |
| 12 | User requests | Produce two groups of four concept images, with English text, then archive the process assets on GitHub. | Eight generated original images and this process record. |

Harry's mother and Koala are distinct contributors. No full names, GitHub accounts or likenesses
are inferred for either of them. People and pets in the generated images are synthetic illustrations.

## Assessment of the L150 Pro four-wheel-drive candidate

The supplied image IMG_0367.jpeg advertises assembled/tuned shipment, four independently driven
motors and a suspension mechanism. Its contents list includes the STM32F407 controller,
battery, charger and accessories; N10P LiDAR and USB wireless controller are optional.
It does not establish an included Linux/ROS 2 computer, camera, recoverable image or complete
mapping/navigation software package.

The fixed-wheel arrangement appears to use differential/skid steering; that inference is not
confirmation of the supplied firmware. Four-wheel drive is not itself a rejection reason.
For Stage 1, the important question is whether this exact version has a supported complete
package and reproducible tutorials.

Ask the supplier for the itemized system: computer/image, controller/firmware, sensors, adapters,
software/source versions, stop behavior and tutorials for this geometry. A working STM32 base
is not automatically a ready ROS 2 learning robot. No quote or compatibility answer is invented here.

## What the conversation changed

- The immediate goal is hands-on learning on mature supported hardware.
- Pet interaction is a concrete application hypothesis to discuss and test.
- A ball is an alternative product form, not an instruction to start custom mechanics.
- RK3588 remains a later platform direction; a fixed hub could host it in one future architecture.
- Owner-away operation remains future work, not a capability established by a sphere or a demo.

The original v0.1 enrolled-person-following scope remains in the mission documents.
This archive adds a pet exploration track; adopting it as the formal v0.1 mission requires a
separate scope decision and corresponding specifications. No G0–G8 status changes here.

## Repository history

- [Original hardware proposal: b92d1cb](https://github.com/frank2023fantastic/Open-Verified-Autonomy/commit/b92d1cbc6cf94d0dbe34ce059f3264b2c1b1a9ac)
- [Harry team clarification: 9974137](https://github.com/frank2023fantastic/Open-Verified-Autonomy/commit/9974137581b152a774ae0b6fa5a5ed1704f1599b)
- [Two-stage plan and task rescheduling: 5df0cee](https://github.com/frank2023fantastic/Open-Verified-Autonomy/commit/5df0ceec619676ee3a53338c8cb7fded85a7f606)
- [Current hardware discussion / Issue #3](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/3)
- [Learning outcome / Issue #8](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/8)

The private chat screenshot IMG_0368.png is represented by the substantive paraphrases above,
not republished as chat UI with avatars. Seller reference images and generated concepts are
separately identified in [SOURCES](SOURCES.md).
