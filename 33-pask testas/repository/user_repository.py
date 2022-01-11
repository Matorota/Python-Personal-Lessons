from fastapi import status, HTTPException
from sqlalchemy.orm import Session, selectinload
import models
import schemas


def get_all_users(db: Session):
    return db.query(models.User).all()


def create_users(request: schemas.UserCreate, db: Session):
    new_user = models.User(
        email=request.email,
        password=request.password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def create_user_settings(request:schemas.SettingsUserInfo, db: Session):
    new_user_settings = models.UserSettings(
        consumption_km=request.consumption_km,
        consumption_mp=request.consumption_mp,
        mel_km=request.mel_km,
        mel_mp=request.mel_mp,
        rida=request.rida,
    )
    db.add(new_user_settings)
    db.commit()
    db.refresh(new_user_settings)
    return new_user_settings

