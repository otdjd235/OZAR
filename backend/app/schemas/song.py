from pydantic import BaseModel
from typing import Optional, List

class SongCreate(BaseModel):
    title: str
    link: Optional[str] = None
    lyrics: Optional[str] = None
    tonality: Optional[str] = None
    theme_ids: Optional[List[int]] = []   # ✅ permet d’attacher le chant à plusieurs thèmes

class SongOut(BaseModel):
    id: int
    title: str
    link: Optional[str] = None
    lyrics: Optional[str] = None
    tonality: Optional[str] = None
    themes: list[dict] = []

    class Config:
        from_attributes = True
