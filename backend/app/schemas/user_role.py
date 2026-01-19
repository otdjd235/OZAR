from pydantic import BaseModel, Field

class AssignRoleIn(BaseModel):
    role: str = Field(..., examples=["CHANTRE"])
