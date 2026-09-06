# G1 bench bringup checklist

This is the formal qualifying-test procedure. Initial vendor learning exercises use the bounded
[Stage 1 motion-readiness checks](../docs/plan/TWO_STAGE_PLAN.md) and do not claim G1 completion.

Status: planned procedure, not an executed record. Use it with the chosen hardware documentation and
a completed, frozen [G1 specification](../verification/specs/G1-manual-robot.yaml).
Resolve hardware-specific setup details with the mentor before the qualifying physical test.

1. Record hardware/firmware versions, wiring, supply limits, wheel geometry and encoder scale.
2. Check the physical stop path and startup/disarmed behavior before requesting movement.
3. With the base secured and wheels clear as appropriate for the hardware, verify motor direction,
   encoder sign, range limits, and command timeout using the defined low test setpoint.
4. Test physical stop, lost commands, high-level process termination, and reconnect/rearm behavior.
5. Move to the defined clear test area only after bench observations match the specification.
6. Measure teleoperation, encoder response, actual stopping time and distance under the declared load.
7. Preserve raw data, interventions and failures; obtain cross-review before a gate decision.

Do not infer a safe stopping distance from a wheels-lifted test. Do not treat a zero command, motor-inhibit
signal, or vendor demo as proof of physical stopping. Record how the chosen base coasts or brakes.
