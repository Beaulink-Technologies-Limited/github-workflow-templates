from fastapi import FastAPI

app = FastAPI(title="REPLACE_ME Service")

@app.get("/healthz", tags=["meta"])
def health() -> dict[str, str]:
    return {"status": "ok"}
