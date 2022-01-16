from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, selectinload
from repository import user_repository as repo
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/users',
    tags=['Users']
)


@router.get('', response_model=List[schemas.UserInfo])
def all(db: Session = Depends(get_db)):
    return repo.get_all(db)


@router.post('/create')
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return repo.create(request, db)


@router.put('/update/{id}')
def update(id: int, request: schemas.UserInfo, db: Session = Depends(get_db)):
    return repo.update(id, request, db)


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete(id, db)
