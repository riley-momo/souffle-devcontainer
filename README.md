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

## api usage

If this image is run as a `reasoner` service in Docker Compose, it can expose a small HTTP API with FastAPI.
Your other containers can then call the service over the Compose network using the service name, for example `http://reasoner:8000`.

Example from another Python container:

```python
import requests

response = requests.post(
	"http://reasoner:8000/run",
	json={"args": ["examples/family/ancestor.dl", "--output-dir", "-"]},
)
response.raise_for_status()

result = response.json()
print(result["output"])
```

The `/run` endpoint accepts a JSON body with an `args` list.
Those values are passed through to the Souffle CLI in the same way as `souffle.run(*args)`.
