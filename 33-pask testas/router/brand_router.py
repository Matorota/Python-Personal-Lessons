from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository import brand_repository as repo
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/brands',
    tags=['Brands']
)


@router.get('', response_model=List[schemas.BrandInfo])
def all(db: Session = Depends(get_db)):
    return repo.get_all(db)


@router.post('/create')
def create_brand(request: schemas.BrandCreate, db: Session = Depends(get_db)):
    return repo.create(request, db)


@router.put('/update/{id}')
def update(id: int, request: schemas.BrandInfo, db: Session = Depends(get_db)):
    return repo.update(id, request, db)


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return repo.delete(id, db)
