from pydantic import BaseModel, EmailStr,Field

class RegisterPayload(BaseModel):
    email: EmailStr
    password: str= Field(min_length=8)
    invite_code: str

class LoginPayload(BaseModel):
    email: EmailStr
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
