from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    link = Column(String(500), nullable=True)      
    lyrics = Column(Text, nullable=True)
    tonality = Column(String(20), nullable=True)

    themes = relationship(
        "Theme",
        secondary="theme_songs",
        back_populates="songs",
    )
