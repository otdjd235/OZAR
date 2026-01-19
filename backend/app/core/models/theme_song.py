from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base

class ThemeSong(Base):
    __tablename__ = "theme_songs"

    theme_id = Column(Integer, ForeignKey("themes.id"), primary_key=True)
    song_id = Column(Integer, ForeignKey("songs.id"), primary_key=True)
