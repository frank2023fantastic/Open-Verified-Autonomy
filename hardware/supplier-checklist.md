# Supplier comparison

Compare at least three chassis suppliers before choosing. Record vendor, date, exact model/revision,
answer, and a link/document for each answer. A sales claim remains unverified until checked.

| Question | Evidence to request |
| --- | --- |
| Can we buy mechanics plus MCU without the main computer? | Itemized quote and contents. |
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
