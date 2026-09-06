# Supplier comparison

Stage 1: compare three mature complete-kit candidates using dated sources. Prioritize tutorial
quality, a recoverable vendor-supported image and source access over headline compute performance.
Obtain an itemized current quote for the preferred package. Record vendor, exact revision, answer
and evidence for each item; unknowns remain unknown. Formal G0 still requires its full supplier review.

| Question | Evidence to request |
| --- | --- |
| Does the complete package include a supported computer, sensors and working image? | Itemized quote, exact versions and package contents. |
| Can we recover the environment and reproduce core tutorials? | Image/recovery instructions, versioned quick start, source and support channel. |
| Can the computer be replaced later while reusing the base and sensors? | Protocol/pinout/source evidence; RK3588 need not be supported for Stage 1. |
| Is the command/encoder/IMU protocol public? | Complete protocol document and source link. |
| What happens if commands or the computer stop? | Exact timeout/rearm behavior and a reproducible test method. |
| How does physical emergency stop affect the drive? | Electrical diagram, enable/power/brake behavior, and startup defaults. |
| What ROS 2 support exists? | Exact OS/distribution, driver source, URDF/TF and launch examples. |
| What MCU/firmware version is supplied? | Firmware source/license, or full interface and documented behavior if closed. |
| What are the electrical limits and connections? | Supply range, peak demand, pinout, connector and logic levels. |
| What sensors are actually included? | Model/revision and official driver links. |
| What battery/charger/protection is included? | Specifications and compatibility information. |
| May code and documentation be redistributed? | Exact license/terms; identify closed components. |

Track evidence gaps in [selection](selection.md). The preferred starting base is differential drive;
extra movement axes or sensors must solve an explicit task before adding complexity.
