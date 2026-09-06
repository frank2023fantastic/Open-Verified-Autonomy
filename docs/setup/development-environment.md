# Development environment record

Status: DRAFT. No OS image, ROS 2 distribution, sensor driver, or RKNN version is pinned yet.
Stage 1 starts with the selected kit's vendor-supported combination and recovery procedure.
Pin upstream sources and record actual setup observations. RK3588/RKNN rows are deferred Stage 2 work.

| Item | Candidate / exact version | Source link | Observed result | Owner |
| --- | --- | --- | --- | --- |
| Existing development computer and OS | TBD | TBD | NOT TESTED | Frank |
| ROS 2 distribution and install method | TBD | TBD | NOT TESTED | Partner |
| Simulator and robot description | TBD | TBD | NOT TESTED | Partner |
| Vendor kit computer, supplied image, kernel and recovery method | TBD | TBD | NOT TESTED | Frank + Harry |
| RK3588 board, OS image, kernel (Stage 2) | DEFERRED | TBD | NOT TESTED | Frank |
| RK3588 NPU driver, runtime and conversion tool (Stage 2) | DEFERRED | TBD | NOT TESTED | Frank |
| Camera and LiDAR drivers | TBD | TBD | NOT TESTED | Partner |
| MCU transport and firmware revision | TBD | TBD | NOT TESTED | Partner |

## First reproducible setup record

Record exact commands, source revisions, package versions, architecture, and error output.
Capture a minimal publish/subscribe or sensor-recording demonstration and label its environment.
Then add a tested setup procedure here. Do not copy a vendor's successful screenshot as your own result.

Keep PC-only simulation, CPU inference, and RK3588 NPU benchmarks separately labeled.
The record-creation helper needs Python 3.9+ and uses only the Python standard library.
It does not install a ROS workspace or board dependencies.
