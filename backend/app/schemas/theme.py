from pydantic import BaseModel, HttpUrl
from typing import Optional, List

class ThemeCreate(BaseModel):
    title: str
    exhortation_video_url: Optional[str] = None  # on reste string pour éviter blocage URL

class ThemeOut(BaseModel):
    id: int
    title: str
    exhortation_video_url: Optional[str] = None

    class Config:
        from_attributes = True

class ThemeWithSongsOut(ThemeOut):
    songs: List[dict] = []
