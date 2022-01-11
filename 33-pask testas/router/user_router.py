from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from repository import user_repository as repo

router = APIRouter(
    prefix='/api/user',
    tags=['Users']
)


@router.get('', response_model=List[schemas.User])  # get users
def all(db: Session = Depends(get_db)):
    return repo.get_all_users(db)


@router.post('/create_user')
def create_users(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return  repo.create_users(request, db)

@router.post('/create_user_settings')
def create_users(request: schemas.SettingsUserInfo, db: Session = Depends(get_db)):
    return  repo.create_user_settings(request, db)
