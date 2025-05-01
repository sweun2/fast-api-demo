from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Users(Base):
    __tablename__ = "users"

    id       = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email    = Column(String(120), unique=True, index=True, nullable=False)
    hashed_pw= Column(String(128), nullable=False)