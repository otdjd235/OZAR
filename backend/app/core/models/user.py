from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    church_id = Column(Integer, ForeignKey("churches.id"), nullable=False)
   
    status = Column(String(20), nullable=False, default="ACTIVE")

    # relations
    church = relationship("Church", back_populates="users")
    roles = relationship("Role", secondary="user_roles", back_populates="users")
