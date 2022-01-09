from database import Base
from sqlalchemy import  Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

    userCars = relationship("Car", back_populates="owner")



class UserSettings(Base):
    __tablename__ = "usersettings"

    id = Column(Integer, primary_key=True, index=True)

    consumption_km = Column(String)
    consumption_mp = Column(String)
    mel_km = Column(String)
    mel_mp = Column(String)
    rida = Column(Integer)

    is_active = Column(Boolean, default=False)

    settingsUsers = relationship('Car', back_populates='settings', uselist=False)


# class CarBrands(Base):
#     __tablename__ = "carbrands"
#
#     id = Column(Integer, primary_key=True, index=True)
#     brand = Column(String)
#
#     is_active = Column(Boolean, default=False)
#
#     carBrand = relationship("Car", back_populates="owner")


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    years = Column(Integer)
    model = Column(Integer)
    price = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="userCars") # class ir 13 eil

    setting_id_users = Column(Integer, ForeignKey('usersettings.id'))
    settings_users = relationship('UserSettings', back_populates='settingsUsers') # eil 21

    setting_id_users = Column(Integer, ForeignKey('carsettings.id'))
    settings_users = relationship('CarSettings', back_populates='settingsCars')

    # setting_id_brand = Column(Integer, ForeignKey('carsettings.id'))
    # settings_brand = relationship('CarBrands', back_populates='carBrand')


class CarSettings(Base):
    __tablename__ = "carsettings"

    id = Column(Integer, primary_key=True, index=True)
    mileage = Column(Integer)
    time = Column(Integer)
    is_active = Column(Boolean, default=False)

    settingsCars = relationship('Car', back_populates='settings', uselist=False)