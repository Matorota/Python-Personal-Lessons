from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def get_all(db: Session):
    return db.query(models.Car).all()


def create(request: schemas.CarCreate, db: Session):
    new_car = models.Car(
        year=request.year,
        price=request.price,
        more_info=request.more_info,
        brand_id=request.brand_id,
        model_id=request.model_id,
        users_id=request.users_id
    )

    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car


def update(id: int, request: schemas.CarInfo, db: Session):
    car = db.query(models.Car).filter(models.Car.id == id)

    if not car.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {id} not found"
        )

    car.update(request.dict())
    db.commit()
    return car.first()


def delete(id: int, db: Session):
    car = db.query(models.Car).filter(models.Car.id == id)

    if not car.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with id {id} not found"
        )
    car.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}

