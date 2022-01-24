from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from datetime import datetime


def get_all(db: Session):
    return db.query(models.Mileage).all()


def create(request: schemas.MileageCreate, db: Session):
    now = datetime.now()
    new_mileage = models.Mileage(
        mileage_record=request.mileage_record,
        time=now,
        car_id=request.car_id
    )

    db.add(new_mileage)
    db.commit()
    db.refresh(new_mileage)
    return new_mileage


def update(id: int, request: schemas.MileageInfo, db: Session):
    mileage = db.query(models.Mileage).filter(models.Mileage.id == id)

    if not mileage.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mileage with id {id} not found"
        )

    mileage.update(request.dict())
    db.commit()

    return mileage.first()


def delete( id: int, db: Session):
    mileage = db.query(models.Mileage).filter(models.Mileage.id == id)

    if not mileage.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mileage with id {id} not found"
        )
    mileage.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}
