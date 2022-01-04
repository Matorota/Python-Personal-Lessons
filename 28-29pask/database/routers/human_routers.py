from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from repository import human_repository as repo
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/human',
    tags=['Humans']
)


@router.get('', response_model=List[schemas.HumanShortInfo])
def all(db: Session = Depends(get_db)):
    return repo.get_humans_short_info(db)


@router.get('/{id}', response_model=schemas.HumanShortInfo)
def get_singe(id: int, db: Session = Depends(get_db)):
    return repo.get_human_single_short_info(id, db)


@router.post('', response_model=schemas.HumanShortInfo)
def create(request: schemas.HumanShortInfo, db: Session = Depends(get_db)):
    return repo.create_human(request, db)


@router.put('/update/{id}')
def update(id: int, request:schemas.HumanPost, db: Session = Depends(get_db)):
    return repo.update_human(id, request, db)


@router.delete('/delete/{id}')
def delete(id: int, db:Session = Depends(get_db)):
    return repo.delete_human(id, db)