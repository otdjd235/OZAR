from pydantic import BaseModel, EmailStr
from typing import List

class UserOut(BaseModel):
    id: int
    email: EmailStr
    church_id: int
    status: str
    roles: List[str]

class UserStatusUpdate(BaseModel):
    status: str
