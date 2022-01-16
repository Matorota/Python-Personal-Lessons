from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, selectinload
from repository import car_repository as repo
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/cars',
    tags=['Cars']
)


@router.get('', response_model=List[schemas.CarInfo])
def all(db: Session = Depends(get_db)):
    return repo.get_all(db)


@router.post('/create')
def create_car(request: schemas.CarCreate, db: Session = Depends(get_db)):
    return repo.create(request, db)


@router.put('/update/{id}')
def update(id: int, request: schemas.CarInfo, db: Session = Depends(get_db)):
    return repo.update(id, request, db)


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete(id, db)