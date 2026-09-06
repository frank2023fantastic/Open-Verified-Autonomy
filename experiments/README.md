# Experiment records

Create one directory per attempt. Never overwrite a previous run, including a failed one.
Use a unique run ID such as `20260906-g1-timeout-001`. Raw files can be stored externally; keep their
retrievable locations and hashes in the record. Preserve all intended trials and explain exclusions.

From the repository root:

```bash
python3 tools/new_experiment.py --run-id practice-001 --gate G1 --mode dry_run
```

The helper needs Python 3.9+ and no third-party packages. It copies seven templates and sets only the
run ID, gate, declared mode, and record creation time. It does not run tests, freeze acceptance,
calculate metrics, collect evidence, or issue a verdict. It refuses to overwrite an existing run.

Modes: `dry_run` for template practice; `simulation`; `replay`; `physical`; `review` for document/evidence review.
Choosing `physical` does not make the record physical evidence; the actual experiment and raw observations are required.
Review mode can record G0/G7 work; it cannot satisfy a physical-test requirement.

## Before a qualifying run

Fill `run.yaml`: tested code commit (plus any diff/dirty state), firmware, configuration and model hashes,
hardware, environment, operator, reviewer, clock alignment, and actual start/end time.
For a non-applicable field, record that fact and a reason (for example, no perception model in a manual-control run).
Replace the placeholder `acceptance.yaml` with a byte-for-byte copy of the reviewed FROZEN specification;
record its path, revision and SHA-256 in `run.yaml`. The template is deliberately incomplete.

## During and after

- Add actual events to `events.csv`; specify clock reference and units. Preserve the raw sensor/command/wheel data.
- Calculate metrics using a recorded method/script revision; each result identifies its criterion and source evidence.
- Add raw artifact locations, size, SHA-256, and useful intervals to `evidence_index.md`.
- A different person completes `verifier_report.md`; the human gate owner records `decision.md` afterward.
- Keep unfinished records `NOT_RUN`, `INCONCLUSIVE`, or `NOT_REVIEWED` as appropriate. An empty metrics file is not a pass.

Do not edit an old frozen run to make it agree with a later implementation. Publish a new run and link the comparison.
