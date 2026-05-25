from fastapi import FastAPI
from ._api import run as souffle_run

app = FastAPI(title="Souffle API")


@app.post("/run")
async def run_souffle(args: list[str]):
    """Run souffle with the given arguments"""
    try:
        output = souffle_run(*args)
        return {"success": True, "output": output}
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.get("/health")
async def health():
    return {"status": "ok"}
