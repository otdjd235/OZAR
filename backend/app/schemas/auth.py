from pydantic import BaseModel, EmailStr

class RegisterPayload(BaseModel):
    email: EmailStr
    password: str
    church_id: int

class LoginPayload(BaseModel):
    email: EmailStr
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
