from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.core.models.theme import Theme
from app.core.models.user import User
from app.core.permissions import requireAnyRole
from app.schemas.theme import ThemeCreate
from app.schemas.theme import ThemeOut

router = APIRouter(prefix="/themes", tags=["themes"])

@router.post("/", response_model=ThemeOut)
def create_theme(
    payload: ThemeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(requireAnyRole(["ADMIN", "DIRECTOR", "LEAD"])),
):
    existing = db.query(Theme).filter(Theme.title == payload.title).first()
    if existing:
        raise HTTPException(status_code=400, detail="Theme already exists")

    theme = Theme(
        title=payload.title.strip(),
        exhortation_video_url=payload.exhortation_video_url,
    )
    db.add(theme)
    db.commit()
    db.refresh(theme)
    return theme

@router.get("/", response_model=list[ThemeOut])
def list_themes(db: Session = Depends(get_db)):
    return db.query(Theme).order_by(Theme.title.asc()).all()
