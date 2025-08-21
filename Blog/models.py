from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Blog(Base):
    __tablename__ = "blogs"

    creator = relationship("User", back_populates="blogs")
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)  
    user_id = Column(Integer,ForeignKey('users.id')) # Foreign key to link to User table

class User(Base):
    __tablename__ = "users"
    blogs = relationship("Blog", back_populates="creator")
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)  # In a real application, ensure to hash passwords       