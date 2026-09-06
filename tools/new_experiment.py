#!/usr/bin/env python3
"""Create an unexecuted experiment record. This tool never verifies a capability."""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-id', required=True, help='Unique ID: letters, digits, hyphens, underscores.')
    parser.add_argument('--gate', required=True, choices=[f'G{i}' for i in range(9)])
    parser.add_argument('--mode', required=True, choices=['dry_run', 'simulation', 'replay', 'physical', 'review'])
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,79}', args.run_id):
        parser.error('run ID must be 1–80 letters/digits/hyphens/underscores and start with a letter or digit')

    root = Path(__file__).resolve().parents[1]
    experiments = root / 'experiments'
    template = experiments / '_template'
    destination = experiments / args.run_id
    if destination.exists():
        parser.error(f'run already exists; choose a new ID: {destination}')
    names = ['run.yaml', 'acceptance.yaml', 'events.csv', 'metrics.json',
             'evidence_index.md', 'verifier_report.md', 'decision.md']
    missing = [name for name in names if not (template / name).is_file()]
    if missing:
        parser.error('missing experiment templates: ' + ', '.join(missing))

    replacements = {
        '__RUN_ID__': args.run_id,
        '__GATE__': args.gate,
        '__MODE__': args.mode,
        '__CREATED_AT__': datetime.now(timezone.utc).isoformat(),
    }
    # Prepare the complete bundle before creating the final directory. mkdir is the
    # collision guard: a concurrent invocation cannot overwrite an existing run.
    with tempfile.TemporaryDirectory(prefix='ova-run-') as staging_dir:
        staging = Path(staging_dir)
        for name in names:
            text = (template / name).read_text(encoding='utf-8')
            for old, new in replacements.items():
                # JSON string literals are valid YAML scalars. Keep IDs such as
                # "123", "true", or "null" as strings in the generated YAML.
                replacement = json.dumps(new) if name.endswith('.yaml') else new
                text = text.replace(old, replacement)
            (staging / name).write_text(text, encoding='utf-8')
        try:
            destination.mkdir()
        except FileExistsError:
            parser.error(f'run already exists; choose a new ID: {destination}')
        # If copying fails, leave the incomplete new record visible for diagnosis.
        # Never remove or overwrite an existing experiment.
        for name in names:
            with (staging / name).open('rb') as src, (destination / name).open('xb') as dst:
                shutil.copyfileobj(src, dst)

    print(f'Created {destination}')
    print('Status: NOT_RUN / NOT_REVIEWED. No test was executed and no verdict was issued.')


if __name__ == '__main__':
    main()
