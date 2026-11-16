from fastapi import FastAPI

app = FastAPI(title="mitsuami-unit-python")


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}
