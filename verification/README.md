# Verification plane

This directory holds draft criteria, scenario definitions, and the review method. It does not contain
an implemented automated verifier or completed robot results.

1. Select the gate in [the roadmap](../docs/plan/ROADMAP.md).
2. Complete its draft specification in `specs/`: resolve required nulls, methods, repetitions, and boundaries.
3. Have the criterion owner and independent reviewer record a version and freezing decision before a qualifying run.
4. Instantiate the applicable [scenario catalog](scenarios/catalog.yaml) and prepare the physical or simulated setup.
5. Create a record using [experiment instructions](../experiments/README.md), then execute the actual procedure.
6. Use [the review protocol](verifiers/REVIEW_PROTOCOL.md) to inspect evidence and record the human gate decision.

`DRAFT` means criteria are unfinished. `FROZEN` means criteria are fixed for a particular experiment;
it does not mean the system meets them. Changing a frozen criterion creates a new revision and new
qualifying runs where required. Keep the previous specification and evidence.

Test result: PASS / FAIL / NOT_RUN / INCONCLUSIVE. Review state: NOT_REVIEWED until review occurs.
Gate verdict: VERIFIED / NOT VERIFIED / PARTIAL. Only a complete, independently supported verdict can
support advancing a gate. A physical requirement cannot be satisfied solely by simulation or replay.
