from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository import settings_repository as repo
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/settings',
    tags=['Settings']
)


@router.get('', response_model=List[schemas.SettingsInfo])
def all(db: Session = Depends(get_db)):
    return repo.get_all(db)


@router.post('/create')
def create_settings(request: schemas.SettingsCreate, db: Session = Depends(get_db)):
    return repo.create(request, db)


@router.put('/update/{id}')
def update(id: int, request: schemas.SettingsInfo, db: Session = Depends(get_db)):
    return repo.update(id, request, db)


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete(id, db)
