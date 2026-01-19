from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.core.models.role import Role
from app.core.models.user import User
from app.core.permissions import requireAnyRole

router = APIRouter(prefix="/roles", tags=["roles"])

@router.get("/")
def list_roles(
    db: Session = Depends(get_db),
    current_user: User = Depends(requireAnyRole(["ADMIN", "DIRECTOR"])),
):
    roles = db.query(Role).order_by(Role.name.asc()).all()
    return [{"id": r.id, "name": r.name} for r in roles]
