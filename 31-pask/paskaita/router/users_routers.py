from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from  repository import users_repository as repo

router = APIRouter(
    prefix='/api/user',
    tags=['Users']
)


@router.get('', response_model=List[schemas.User])  # get users
def all(db: Session = Depends(get_db)):
    return repo.get_all_users(db)

# create

@router.post('/create')
def create_users(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return  repo.create_blog(request, db)