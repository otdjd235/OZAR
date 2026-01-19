from fastapi import FastAPI

from app.core.database import engine
from app.routers.church import routers as church_router
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.roles import router as roles_router
from app.routers.themes import router as themes_router
from app.routers.songs import router as songs_router


app = FastAPI(title="OZAR API")


app.include_router(church_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(themes_router)
app.include_router(songs_router)



@app.get("/")
def root():
    return {"status": "ok", "service": "OZAR API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with engine.connect():
        pass
    return {"db": "connected"}
