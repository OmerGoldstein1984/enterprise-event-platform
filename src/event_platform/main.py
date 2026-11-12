from fastapi import FastAPI

app = FastAPI(title="Enterprise Event Platform", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ready")
def ready() -> dict[str, str]:
    # TODO(M0): verify database and broker connectivity before returning ready.
    return {"status": "not_implemented"}
