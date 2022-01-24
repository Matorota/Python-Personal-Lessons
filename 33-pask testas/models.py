from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    gmail = Column(Integer)
    kategorija = Column(Integer)

    setting = relationship("Settings", back_populates="user", uselist=False)
    car = relationship("Car", back_populates="user")


class Brand(Base):

    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String)

    car = relationship("Car", back_populates="brand")


class Model(Base):

    __tablename__ = 'models'

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String)

    car = relationship("Car", back_populates="model")


class Settings(Base):

    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True, index=True)
    consumption = Column(String)
    odometer = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="setting")




class Car(Base):

    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    price = Column(String)
    more_info = Column(String)

    users_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='car')

    brand_id = Column(Integer, ForeignKey('brands.id'))
    brand = relationship('Brand', back_populates='car')

    model_id = Column(Integer, ForeignKey('models.id'))
    model = relationship('Model', back_populates='car')

    mileage = relationship("Mileage", back_populates="car")


class Mileage(Base):

    __tablename__ = 'mileage'

    id = Column(Integer, primary_key=True, index=True)
    mileage_record = Column(Integer)
    time = Column(Date)

    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship('Car', back_populates='mileage')

