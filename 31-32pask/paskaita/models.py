from database import Base
from sqlalchemy import  Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    blogs = relationship("Blog", back_populates="owner")


class PostSettings(Base):
    __tablename__ = "postsettings"

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=False)

    blog = relationship('Blog', back_populates='settings', uselist=False) # uselist using one to onje


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="blogs") # class ir 13 eil

    setting_id = Column(Integer, ForeignKey('postsettings.id'))
    settings = relationship('PostSettings', back_populates='blog') # eil 21
