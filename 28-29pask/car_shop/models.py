from database import Base
from sqlalchemy import Column, Integer, String



class Cars(Base):
    __tablename__ = "Car"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    year = Column(Integer)
    price = Column(Integer)
    horsePower = Column(Integer)
    informacion = Column(String)
