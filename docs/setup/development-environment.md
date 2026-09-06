# Development environment record

Status: DRAFT. No OS image, ROS 2 distribution, sensor driver, or RKNN version is pinned yet.
Select a compatible combination using upstream documentation and direct setup experiments.

| Item | Candidate / exact version | Source link | Observed result | Owner |
| --- | --- | --- | --- | --- |
| Existing development computer and OS | TBD | TBD | NOT TESTED | Frank |
| ROS 2 distribution and install method | TBD | TBD | NOT TESTED | Partner |
| Simulator and robot description | TBD | TBD | NOT TESTED | Partner |
| RK3588 board, OS image, kernel | TBD | TBD | NOT TESTED | Frank |
| Board NPU driver, runtime, and conversion tool | TBD | TBD | NOT TESTED | Frank |
| Camera and LiDAR drivers | TBD | TBD | NOT TESTED | Partner |
| MCU transport and firmware revision | TBD | TBD | NOT TESTED | Partner |

## First reproducible setup record

Record exact commands, source revisions, package versions, architecture, and error output.
Capture a minimal publish/subscribe or sensor-recording demonstration and label its environment.
Then add a tested setup procedure here. Do not copy a vendor's successful screenshot as your own result.

Keep PC-only simulation, CPU inference, and RK3588 NPU benchmarks separately labeled.
The record-creation helper needs Python 3.9+ and uses only the Python standard library.
It does not install a ROS workspace or board dependencies.
