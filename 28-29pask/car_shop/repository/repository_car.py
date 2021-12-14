from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas

def get_cars_short_info(db: Session):
    return db.query(models.Cars).all()


def get_car_single_short_info(id: int, db: Session):
    car = db.query(models.Cars).filter(models.Cars.id == id).first()

    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with {id} not found"
        )

    return car


def create_car(request: schemas.CarPost, db: Session):
    new_car = models.Cars(
        brand=request.brand,
        year=request.year,
        price=request.price,
        horsePower=request.horsePower,
        informacion=request.informacion

    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return new_car
