from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    church_id = Column(Integer, ForeignKey("churches.id"), nullable=False)
