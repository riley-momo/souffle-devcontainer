from __future__ import annotations

from subprocess import CalledProcessError, run as subprocess_run


def run(*args: str) -> str:
    command = ["souffle", *args]
    try:
        completed = subprocess_run(
            command,
            text=True,
            capture_output=True,
            check=True,
        )
    except CalledProcessError as exc:
        return exc.stderr or exc.stdout or ""
    return completed.stdout
