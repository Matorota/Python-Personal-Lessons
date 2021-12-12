from database_alchemy import Base
from sqlalchemy import Column, Integer, String



class Human(Base):
    __tablename__ = "humans"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

