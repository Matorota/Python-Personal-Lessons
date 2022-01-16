from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, selectinload
from repository import mileage_repository as repo
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/mileage',
    tags=['Mileage']
)


@router.get('', response_model=List[schemas.MileageInfo])
def all(db: Session = Depends(get_db)):
    return repo.get_all(db)


@router.post('/create')
def create_car(request: schemas.MileageCreate, db: Session = Depends(get_db)):
    return repo.create(request, db)


@router.put('/update/{id}')
def update(id: int, request: schemas.MileageInfo, db: Session = Depends(get_db)):
    return repo.update(id, request, db)


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete(id, db)
