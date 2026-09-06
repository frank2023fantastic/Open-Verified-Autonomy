# Interface contract v0.1

Status: DRAFT. Logical interfaces below define responsibilities. ROS topic names, message types,
QoS, rates, and vendor packet bytes must be confirmed during T02/T04; this is not a ready driver API.

| Interface | Producer → consumer | Required information | Failure contract |
| --- | --- | --- | --- |
| Sensor observation | Driver → perception/navigation/monitor | Sensor ID, source and receive timestamps, sequence, frame, units, validity | Stale, absent, or invalid required data triggers the specified stop policy. |
| Target state | Enrollment/tracker → following policy | Enrolled target ID, track ID, observation time, confidence, range estimate and validity | Unknown identity/range cannot authorize blind following. |
| Motion request | Planner/manual control → safety supervisor | Source, linear/angular request, timestamp, mode | Requests outside limits or from an inactive mode are rejected or bounded as specified. |
| Permitted command | Supervisor → MCU | Sequence, linear/angular or wheel targets, units, bounded values, expiry/heartbeat semantics | Invalid/stale/out-of-sequence command must not renew motion permission. |
| Wheel/MCU telemetry | MCU → state estimation/monitor/recorder | Measured wheel speeds/counts, time, enable/fault state, firmware revision | Implausible/missing data triggers a named fault; define response before testing. |
| Fault event | Supervisor/MCU → recorder/operator | Event ID, source, detection time, state transition, cause, stop action | Log failures remain visible; missing records cannot support a passed test. |
| Experiment metadata | Test runner → verifier | Run ID, spec hash, code/config/model versions, environment, evidence locations | Version disagreement or missing evidence makes the result unresolved. |

## Units, frames, and clocks

Use SI units in the project-facing interface: meters, seconds, radians, meters/second, radians/second.
Document wheel radius, track width, encoder scale/sign, and motor sign before motion testing.
Record the map/odom/base/sensor frame relationships and the exact TF names in the implemented robot description.

Preserve sensor time and host receive time where available. Record clock sources, offsets, and uncertainty.
Fault-to-stop calculations need a common timeline or an explicitly measured alignment; subtracting
unrelated clocks is not a valid latency measurement. Video alignment and wheel-speed resolution are part of the test setup.

## MCU transport decision checklist

Record serial/CAN/other choice, electrical levels, connector pinout, packet length/framing, checksum,
rate, range, sequence behavior, timeout, startup defaults, and reconnect/rearm rules.
The actual vendor protocol is evidence to read, not an API to invent. A heartbeat that continues while
perception is stuck must not conceal stale observations from the supervisor.

## One command authority

Define a single active source for drive requests and a single route through the supervisor to the MCU.
Manual and autonomous modes share protective limits. The physical stop acts directly on the drive hardware.
The verifier has no drive command interface in v0.1.
