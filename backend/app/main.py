from fastapi import FastAPI

from app.core.database import engine
from app.routers.church import routers as church_router

app = FastAPI(title="OZAR API")

# app= FastAPI()
app.include_router(church_router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with engine.connect():
        pass
    return {"db": "connected"}



