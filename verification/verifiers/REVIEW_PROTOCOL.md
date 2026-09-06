# Independent review protocol

Status: manual review procedure; future automated tooling must implement and test explicit rules.
The verifier is given the frozen specification, raw evidence index, code/configuration/model versions,
metric calculation methods, and actual run records. It does not receive authority to command motion.

## Review in this order

1. Confirm the run is real for its declared mode and identify the tested capability and operating envelope.
2. Confirm the acceptance revision was frozen before the qualifying run and required fields were resolved.
3. Check run identity, commit, firmware/config/model versions and hashes against the raw evidence.
4. Check raw files are retrievable and hashes match. Inspect time alignment and measurement uncertainty.
5. Recompute or independently check each mandatory metric. Read source observations when automated summaries disagree.
6. Check repetition counts, failures, interventions, exclusions, and fault-injection coverage.
7. Separate commanded behavior from measured physical behavior, especially stopping.
8. Record criterion-by-criterion PASS / FAIL / NOT_RUN / INCONCLUSIVE and evidence locations.
9. Record a gate verdict and limitations; identify a human reviewer and the subsequent gate decision.

## Verdict rules

| Condition | Result |
| --- | --- |
| Every mandatory criterion passes with sufficient independent evidence | VERIFIED for that exact capability/configuration/envelope. |
| A mandatory criterion fails, or evidence is fundamentally missing/inconsistent | NOT VERIFIED. |
| A meaningful subset is supported but required coverage remains unresolved | PARTIAL; the gate remains incomplete. |
| No review performed | NOT_REVIEWED; no gate verdict yet. |

An AI verifier may propose findings. A named independent person checks the result and owns the review.
The feature author supplies explanations but does not independently certify their own change.
Fixes belong to a new builder change/run, not silent alterations to an existing evidence bundle.

## Test the verifier itself

Before relying on automation, challenge it with: missing raw logs; wrong commit/spec hash; insufficient
trials; fabricated or duplicated run IDs; invalid clock alignment; stop command without stopping telemetry;
a DRAFT specification; simulation substituted for physical evidence; and a failing mandatory result hidden
behind a good aggregate score. None may produce VERIFIED. Record the negative checks as verifier tests,
distinct from robot capability tests. No such tests are claimed executed by this scaffold.
