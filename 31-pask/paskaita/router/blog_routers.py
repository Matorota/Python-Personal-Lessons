from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from repository import blog_repository as repo


router = APIRouter(
    prefix='/api/blog',
    tags=['Blog']
)


@router.get('', response_model=List[schemas.Blog])  # get users
def all(db: Session = Depends(get_db)):
    return repo.get_all_blog(db)
    # return db.query(models.Blog).options(selectinload(models.Blog.owner)).all()



def all(db: Session = Depends(get_db)):
    return repo.get_all_users(db)

# create

@router.post('/create/{user_id}')
def create(request: schemas.BlogCreate, user_id: int, db: Session = Depends(get_db)):
    return  repo.create_blog(request, db)

