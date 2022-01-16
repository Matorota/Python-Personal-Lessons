from fastapi import status, HTTPException
from sqlalchemy.orm import Session, selectinload
import models
import schemas


def get_all(db: Session):
    return db.query(models.Settings).all()


def create(request: schemas.SettingsCreate, db: Session):
    global id
    new_settings = models.Settings(
        consumption=request.consumption,
        odometer=request.odometer,
        user_id=request.user_id
    )

    db.add(new_settings)
    db.commit()
    db.refresh(new_settings)
    return new_settings


def update(id: int, request: schemas.SettingsInfo, db: Session):
    settings = db.query(models.Settings).filter(models.Settings.id == id)

    if not settings.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Settings with id {id} not found"
        )

    settings.update(request.dict())
    db.commit()

    return settings.first()


def delete(id: int, db: Session):
    settings = db.query(models.Settings).filter(models.Settings.id == id)

    if not settings.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Settings with id {id} not found"
        )
    settings.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}

