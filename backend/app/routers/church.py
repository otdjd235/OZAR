from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.core.models.church import Church
from app.schemas.church import ChurchCreate, ChurchOut
# from app.schemas import church

routers = APIRouter(prefix="/churches", tags=["churches"])

@routers.post("/", response_model=ChurchOut)
def create_church(payload: ChurchCreate, db: Session = Depends(get_db)):
    existing = db.query(Church).filter(Church.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Church already exists")

    church = Church(name=payload.name)
    db.add(church)
    db.commit()
    db.refresh(church)
    return church

@routers.get("/", response_model=list[ChurchOut])
def list_churches(db: Session = Depends(get_db)):
    return db.query(Church).all()