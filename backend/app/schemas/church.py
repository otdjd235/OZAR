from pydantic import BaseModel

class ChurchCreate(BaseModel):
    name: str

class ChurchOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
