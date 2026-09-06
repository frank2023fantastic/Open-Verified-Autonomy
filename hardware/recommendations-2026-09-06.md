# T03 discussion: RK3588 and a purchased differential-drive base

Date: 2026-09-06  
Status: **SUPERSEDED FOR STAGE 1 PROCUREMENT — historical proposal, no purchase approval**

Update: the [two-stage plan](../docs/plan/TWO_STAGE_PLAN.md) now takes priority. Stage 1 selects
a mature complete kit with its vendor-supported computer; RK3588 and the L150/C30D combination
below are retained only as possible later integration references. This historical checklist is
not the current purchase instruction.  
Discussion: [Issue #3](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/3)

## Recommendation

Buy an assembled, configured differential-drive chassis with its motor controller, encoders,
battery, charger and finished wiring. Integrate purchased compute and sensors.
Custom chassis, PCB, motor-driver and power-supply design are outside this starting scope.

Keep RK3588 as the initial compute direction. The exact board and software image remain open.
For the pictured L150 family, investigate **the differential-drive mechanics with a
factory-configured C30D controller** first. Confirm that this combination is actually sold;
the screenshots do not establish an orderable SKU.

This proposal supports the existing supervised, low-speed indoor target-following mission.
It does not freeze the BOM or change the G0–G8 acceptance gates.

| Item | Proposed choice | Condition / fallback |
| --- | --- | --- |
| Chassis geometry | L150-family differential version: two driven wheels and front passive omnidirectional support wheels | Obtain exact SKU, assembled configuration and usable mounting dimensions. |
| Base controller | C30D, configured by the supplier for this differential base | If unavailable, evaluate the standard C10B differential package against the same protocol and stop requirements. Do not change geometry merely to obtain “Pro.” |
| Main computer | RK3588 board bought separately, with cooling and storage | Select the board together with its supported OS, ROS 2, kernel and RKNN versions. |
| Base accessories | Matching battery/charger, secured wiring, controller link adapter and manual-control handset | Quote the exact contents. A handset is not an independent emergency stop. |
| 2D LiDAR | N10P as a conditional supplier-bundle candidate | Require the exact variant, appropriate USB/serial adapter, mounting and an exercised driver on the chosen system. Reassess alternatives if this fails. |
| Camera | Keep USB UVC RGB as the existing baseline; discuss RGB-D if depth solves an explicit following requirement | Orbbec Gemini 335 is an optional RGB-D candidate, not a frozen selection or part of the pictured chassis package. |
| Initial extras | Fixed sensor mounts and necessary cables | Defer line-following modules, voice/LLM bundles and manipulator accessories. |

Prefer this differential layout for the current mission because it keeps the motion model and
integration scope small. Mecanum, three-wheel omni, Ackermann, tracked and four-wheel skid-steer
variants need a specific mission benefit to justify their additional motion or contact behavior.

## What the seller material does and does not establish

The user supplied L150/L150 Pro comparison, controller, contents and dimension screenshots.
Treat these as seller claims pending an exact listing, hardware revision and written response.

- C10B is advertised with STM32F103, two encoder-motor channels and no onboard IMU.
  C30D is advertised with STM32F407, four encoder-motor channels, ICM20948 and a CAN interface.
  These features alone do not establish a usable protocol, watchdog or ROS 2 integration.
- The Pro comparison table omits differential drive from its supported-base list, while the
  C30D description includes it; the differential drawing is labeled L150. Resolve this discrepancy
  before specifying “L150 Pro differential” in an order.
- The pictured differential base is advertised at about 232 × 188 mm, 1.4 kg and 3 kg payload.
  Bare-base and assembled-stack heights differ. Confirm actual space and loaded behavior.
- A 5 V / 5 A output label does not establish compatibility with every RK3588 board:
  voltage, negotiation, connector, peak demand and peripheral load still need checking.
- Advertised runtime is not a measurement with our compute and sensors. A motor-enable switch
  is not evidence of a verified emergency-stop path.

Screenshot provenance: supplied for this discussion on 2026-09-06; filenames
IMG_0344.jpeg, IMG_0354.jpeg, IMG_0345.jpeg and IMG_0356.jpeg–IMG_0362.jpeg.
Seller identity, listing URL and document revisions remain to be recorded.
Vendor images are not redistributed in this commit.

## Checklist for supplier responses and team review

Record each answer with vendor, date, exact model/revision and evidence link in
[selection.md](selection.md), using the existing [supplier checklist](supplier-checklist.md).
All items below are open.

- [ ] **D1 — Package:** Is the differential base available assembled and tuned with C30D,
  without a bundled main computer? Supply an itemized quote, firmware version, contents,
  sensor mounts and connectors. If not, quote the C10B fallback.
- [ ] **D2 — Protocol:** Obtain complete command and telemetry framing, units, signs, rates,
  error handling and a runnable example. Identify encoder feedback as measured counts/speed,
  not an echo of requested motion; document timing, update gaps and any derived odometry.
- [ ] **D3 — Link:** Specify UART voltage/pinout and the finished USB adapter/cable for RK3588.
  Identify which ports carry data versus power. CAN hardware alone does not establish a CAN protocol.
- [ ] **D4 — Timeout:** Document MCU behavior after command loss, computer crash, link loss,
  reboot and reconnection: timeout, braking/coasting, enable defaults and rearm policy.
  Ask for an observable demonstration with the supplied firmware.
- [ ] **D5 — Physical stop:** Obtain the actual electrical drive-inhibit/stop diagram and a
  finished supplier-supported stop solution. Determine whether drive power, enable or braking is
  affected and whether stopping is independent of Linux/ROS. Resolve this before powered floor tests.
- [ ] **D6 — Power and mechanics:** Check the chosen board's input requirements, total sustained
  and startup demand, USB peripherals, thermal load, battery protection and charging.
  Confirm sensor placement, clearance and loaded runtime; purchase finished compatible modules.
- [ ] **D7 — Drivers:** Record board, OS image, kernel, ROS 2 distribution, MCU firmware,
  sensor revision, driver commit and license. Demonstrate camera frames, LiDAR scans and
  measured wheel telemetry on that combination; marketing “ROS 2 support” is insufficient.
- [ ] **D8 — Cost and support:** Obtain dated comparable answers from at least three suppliers,
  as T03 requires. Include shipping, adapters, mounts, cooling, storage and stop hardware.
  No supplier contact, quote or three-supplier comparison is completed by this document.
- [ ] **D9 — Decision:** Confirm available equipment, budget, named owner and separate reviewer.
  Record acceptance/rejection reasons and unresolved items before approving a purchase.

Suggested response format: **D-number / answer / evidence URL and revision / owner / next action**.
Use “unknown” where evidence is missing.

## Adversarial questions and first evidence

Review these under [T02 / Issue #2](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/2)
and [T05 / Issue #5](https://github.com/frank2023fantastic/Open-Verified-Autonomy/issues/5).
They are proposed review/test items, not executed tests or new acceptance thresholds.

| Failure or misleading claim | Evidence to request or measure |
| --- | --- |
| Camera freezes while software continues sending commands | Source-data freshness and command-expiry checks; MCU heartbeat alone cannot detect this case. |
| Main process or controller link fails | Fault-to-stop time, physical stopping distance, residual motion and explicit rearm behavior. |
| Wheel odometry says “stopped,” but the chassis slides | External physical observations using a defined measurement method, not odometry alone. |
| “The AI verified the AI” | Separate builder/reviewer roles; independent observations, frozen criteria and preserved failed runs. |
| Sensors work individually but fail together | Concurrent sensing/inference/control under load, including supply and thermal observations. |
| Similar person or occlusion causes a target switch | Identity traces, annotated observations and the specified uncertainty/stop policy. |

Complete G0 review and hardware-specific G1 criteria, then follow the existing
[bringup checklist](bringup-checklist.md). Establish manual motion, telemetry and stop behavior
before autonomous motion. Static perception work can proceed separately.
Retain the existing gate sequence and label dry runs, replay, simulation and physical tests accurately.

## Public references and limits

Reviewed on 2026-09-06; pin exact revisions when selecting components.

- [Rockchip RKNN Model Zoo](https://github.com/airockchip/rknn_model_zoo):
  upstream deployment examples; not a performance result for our board or model.
- [LSLiDAR ROS 2 driver repository](https://github.com/Lslidar/Lslidar_ROS2_driver):
  starting point for the N10P driver investigation. Confirm the correct branch and target ROS 2
  version; the top-level instructions contain legacy Foxy guidance.
- [Orbbec ROS 2 wrapper](https://github.com/orbbec/OrbbecSDK_ROS2):
  starting point for evaluating the optional RGB-D camera. Confirm model-specific SDK,
  ARM64 dependencies, USB behavior and the actual board image.

Suggested division of discussion work: Frank on compute/perception requirements; Harry, Frank's
classmate and project collaborator, on supplier evidence and chassis integration; a separate
reviewer/mentor on stop behavior and measurement methods. Confirm role acceptance, Harry's GitHub
handle and the reviewer through T01. Decisions belong in
[selection.md](selection.md) and a [decision record](../docs/architecture/decisions/README.md);
this proposal remains a traceable input.
