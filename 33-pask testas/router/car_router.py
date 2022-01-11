from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from repository import car_repository as repo


router = APIRouter(
    prefix='/api/Car',
    tags=['Car']
)

@router.get('', response_model=List[schemas.Car])  # get users
def all(db: Session = Depends(get_db)):
    return repo.get_all_cars(db)


@router.post('/create_car/{user_id}')
def create(request: schemas.CarCreate, user_id: int, db: Session = Depends(get_db)):
    return repo.create_car(request, db, user_id)


@router.post('/create_car_settings')
def create_users(request: schemas.CarSettingsCreate, db: Session = Depends(get_db)):
    return repo.create_car_settings(request, db)


@router.post('/create_brand')
def create_users(request: schemas.CarBrands, db: Session = Depends(get_db)):
    return repo.create_brand(request, db)


