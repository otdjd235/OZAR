from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from app.core.permissions import require_role

from app.core.deps import get_db
from app.core.permissions import requireRole

from app.core.models.church import Church
from app.schemas.church import ChurchCreate, ChurchOut
from app.core.models.church import Church
from app.core.models.user import User # User pas obligatoire ici, mais OK
from app.core.permissions import requireAnyRole
 


# from app.schemas import church

routers = APIRouter(prefix="/churches", tags=["churches"])

# @routers.post("/", response_model=ChurchOut)
# def create_church(payload: ChurchCreate, db: Session = Depends(get_db)):
#     existing = db.query(Church).filter(Church.name == payload.name).first()
#     if existing:
#         raise HTTPException(status_code=400, detail="Church already exists")

#     church = Church(name=payload.name)
#     db.add(church)
#     db.commit()
#     db.refresh(church)
#     return church

@routers.post("/", response_model=ChurchOut)
def create_church( 
    payload: ChurchCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(requireRole("ADMIN")),
):
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

@routers.get("/{church_id}/invite-code")
def get_invite_code(
    church_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(requireAnyRole(["ADMIN", "DIRECTOR"])),
):
    church = db.query(Church).filter(Church.id == church_id).first()
    if not church:
        raise HTTPException(status_code=404, detail="Church not found")

    # ✅ ADMIN: peut accéder à toutes les churches
    is_admin = any(r.name == "ADMIN" for r in current_user.roles)
    if not is_admin and church.id != current_user.church_id:
        raise HTTPException(status_code=403, detail="Cross-church forbidden")

    return {"church_id": church.id, "invite_code": church.invite_code}
