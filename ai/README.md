# AI and edge inference

Status: no model selected, converted, or benchmarked for this robot.
Lead: Frank. Use [the model record](model-record.template.yaml) for every candidate.

Start with a compact detection model and a reproducible CPU/offline baseline. Record conversion and
quantization choices before RK3588 measurements. Separate model-only inference time from camera-to-decision
latency; record dropped frames, measurement conditions, temperature, and sustained runtime.

Detection does not establish target identity. G4 needs enrollment, identity matching, track continuity,
confidence/range validity, and a defined stop/recovery policy. Record failures on distractors and occlusion.
Keep model binaries outside normal Git and record source/license and hashes in the metadata.
