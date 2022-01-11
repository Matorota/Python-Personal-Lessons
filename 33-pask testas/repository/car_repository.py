from fastapi import status, HTTPException
from sqlalchemy.orm import Session, selectinload
import models
import schemas


def get_all_cars(db: Session):
    return db.query(models.Car).all()


def create_car(request: schemas.CarCreate, db: Session, user_id: int):
    new_settings_user = models.UserSettings(
        is_active=request.settings.is_active
    )
    db.add(new_settings_user)
    db.commit()
    db.refresh(new_settings_user)

    new_settings_car = models.CarSettings(
        is_active=request.settings.is_active
    )
    db.add(new_settings_car)
    db.commit()
    db.refresh(new_settings_car)

    new_setting_brand = models.CarBrands(
        is_active=request.settings.is_active
    )
    db.add(new_setting_brand)
    db.commit()
    db.refresh(new_setting_brand)

    new_post = models.Car(
        years=request.years,
        owner_id=user_id,
        setting_id_user=new_settings_user.id,
        setting_id_car=new_settings_car.id,
        setting_id_brand=new_setting_brand.id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def create_brand(request: schemas.CarBrands, db: Session):
    new_brand = models.CarBrands(
        model=request.model,
    )

    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    return new_brand

def create_car_settings(request: schemas.CarSettingsCreate, db: Session):
    new_car_settings = models.UserSettings(
        mileage=request.consumption_km,
        time=request.consumption_mp,
    )
    db.add(new_car_settings)
    db.commit()
    db.refresh(new_car_settings)
    return new_car_settings

def update_car(id: int, request: schemas.Car, db: Session):
    car = db.query(models.car).filter(models.car.id == id)

    if not cars.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    car.update(request.dict())
    db.commit()

    return car.first()
