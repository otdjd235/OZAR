from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Church(Base):
    __tablename__ = "churches"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, unique=True)
