from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from repository import repository_car as repo
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/cars',
    tags=['Cars']
)

@router.get('', response_model=List[schemas.CarShortInfo])
def all(db: Session = Depends(get_db)):
    return repo.get_cars_short_info(db)


@router.get('/{id}', response_model=schemas.CarShortInfo)
def get_singe(id: int, db: Session = Depends(get_db)):
    return repo.get_car_single_short_info(id, db)

@router.post('', response_model=schemas.CarShortInfo)
def create(request: schemas.CarShortInfo, db: Session = Depends(get_db)):
    return repo.create_car(request, db)

