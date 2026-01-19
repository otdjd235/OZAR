from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Church(Base):
    __tablename__ = "churches"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    invite_code = Column(String(50), nullable=False, unique=True)

    users = relationship("User", back_populates="church")
    