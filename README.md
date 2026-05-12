# souffle python wrapper

This repository contains a minimal Docker/devcontainer setup that installs:

- the Souffle CLI
- a tiny Python package named `souffle`

Inside the built image, you can do:

```python
import souffle
output = souffle.run("--version")
print(output)
```

Where the "--version" can be altered to incorporate any command-line arguments. 

The wrapper is intentionally small:

- input: command args (`*args`) that come after `souffle`
- output: one output string

```python
output = souffle.run("--help")
```

## end-to-end example

See:

- [examples/family/ancestor.dl](examples/family/ancestor.dl)
- [examples/run_example.py](examples/run_example.py)

Inside the container, run:

```python
python3 examples/run_example.py
```

That script:

1. calls the installed `souffle` Python wrapper
2. uses a hardcoded path for the example Datalog file, which includes inline facts using simple Parent and Ancestor relations.
3. sets `--output-dir -` so Souffle writes relation output to stdout
4. prints the output string returned by the wrapper
