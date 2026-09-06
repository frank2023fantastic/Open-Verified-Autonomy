# ROS 2 workspace source area

Status: no ROS packages exist here yet; no `colcon build` or robot launch is claimed working.
Lead: robotics/test partner. Frank cross-reviews recorded telemetry and interface behavior.

Stage 1 reuses the vendor's packages and launch procedures; record their exact source/version.
Do not create replacement packages solely to match this planned directory structure.

Expected module responsibilities: bringup and robot description; chassis bridge; state estimation;
LiDAR/SLAM/Nav2 configuration; perception; enrolled-target tracking/following; deterministic supervisor;
experiment recording. Create packages only when their first implementation task begins.

Start with the pinned environment in [development setup](../../docs/setup/development-environment.md).
Record motor/encoder signs, TF, timestamps, and command expiry before integration.
Use actual upstream interfaces and keep all drive requests on the defined protected command path.
