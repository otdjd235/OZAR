from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Theme(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False, unique=True)


    # ✅ vidéo d’exhortation (URL)
    exhortation_video_url = Column(String(500), nullable=True)

    songs = relationship(
        "Song",
        secondary="theme_songs",
        back_populates="themes",
    )
