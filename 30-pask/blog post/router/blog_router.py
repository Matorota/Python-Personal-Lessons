# from fastapi import APIRouter, Depends
# from typing import List
# from sqlalchemy.orm import Session
# from repository import blog_repository as repo
# import models
# import schemas
# from database import get_db
#
#
# router = APIRouter(
#     prefix='/api/blog',
#     tags=['Blog']
# )

# @router.get('', response_model=List[schemas.BlogShortInfo])
# def all(db: Session = Depends(get_db)):
#     return repo.get_blog_single_short_info(db)
#
#
# @router.get('/{id}', response_model=schemas.BlogShortInfo)
# def get_singe(id: int, db: Session = Depends(get_db)):
#     return repo.get_blog_single_short_info(id, db)
#
# @router.post('', response_model=schemas.BlogShortInfo)
# def create(request: schemas.BlogShortInfo, db: Session = Depends(get_db)):
#     return repo.create_blog(request, db)

