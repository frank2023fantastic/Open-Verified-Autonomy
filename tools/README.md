# Repository tools

`new_experiment.py` creates an empty, explicitly unreviewed experiment record from the template.
It needs Python 3.9+ and only the standard library. Run it from any working directory; the destination
is this repository's `experiments/` directory. See [experiment instructions](../experiments/README.md).

There is no automated robot test runner or capability verifier yet. Those will be implemented from the
specifications once the first real inputs and measurement methods exist.
