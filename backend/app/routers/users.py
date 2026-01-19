from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.core.models.user import User
from app.core.models.role import Role
from app.core.permissions import requireAnyRole
from app.schemas.user_role import AssignRoleIn

router = APIRouter(prefix="/users", tags=["users"])

ALLOWED_ASSIGN_ROLES = {"CHANTRE", "INSTRUMENTIST", "DIRECTOR", "ADMIN"}

@router.post("/{user_id}/roles", status_code=204)
def assign_role(
    user_id: int,
    payload: AssignRoleIn,
    db: Session = Depends(get_db),
    current_user: User = Depends(requireAnyRole(["ADMIN", "DIRECTOR"])),
):
    role_name = payload.role.strip().upper()

    if role_name not in ALLOWED_ASSIGN_ROLES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid role. Allowed: {sorted(ALLOWED_ASSIGN_ROLES)}",
        )

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 🔒 option OZAR: tu ne modifies que les users de ta church
    if user.church_id != current_user.church_id:
        raise HTTPException(status_code=403, detail="Cross-church operation forbidden")

    role = db.query(Role).filter(Role.name == role_name).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found in DB (seed roles)")

    if role in user.roles:
        return  # déjà assigné → 204

    user.roles.append(role)
    db.commit()
    return

@router.get("/", response_model=list[dict])
def list_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(requireAnyRole(["ADMIN", "DIRECTOR"])),
):
    users = (
        db.query(User)
        .filter(User.church_id == current_user.church_id)
        .all()
    )
    return [
    {
        "id": u.id,
        "email": u.email,
        "church_id": u.church_id,
        "roles": [r.name for r in u.roles],
    }
    for u in users
]
