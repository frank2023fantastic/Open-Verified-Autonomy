# Firmware and MCU integration

Status: no project firmware implementation yet. Initial integration can use a suitable vendor MCU
with a documented open protocol and independently tested timeout/stop behavior.

First deliverables: exact firmware version/source/license; packet and electrical interface; encoder
scale/sign; independent command expiry; startup and explicit rearm behavior; physical-stop interaction.
Follow [the interface contract](../docs/architecture/interfaces-v0.1.md) and G1 acceptance.
Do not choose a new MCU or write custom motor-control firmware before the base integration need is clear.
