from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Users(Base):
    __tablename__ = "users"

    id       = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_pw= Column(String(128), nullable=False)
    hashed_pw= Column(String(128), nullable=False)
    
    orders    = relationship("Orders", back_populates="user")
    

class Items(Base):
    __tablename__ = "items"
    
    id       = Column(Integer, primary_key=True, index=True)
    itemname = Column(String(50), unique=True, index=True, nullable=False)
    price    = Column(Integer, nullable=False)
    
    orders    = relationship("Orders", back_populates="item")

class Orders(Base):
    __tablename__ = "orders"

    id       = Column(Integer, primary_key=True, index=True)
    item_id  = Column(Integer, ForeignKey("items.id"), nullable=False, index=True)
    user_id  = Column(Integer, ForeignKey("users.id"), nullable=False, index=True, unique=True)
    quantity = Column(Integer, nullable=False)
    user = relationship("Users", back_populates="orders")
    item = relationship("Items", back_populates="orders")
    