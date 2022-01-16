from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def get_all(db: Session):
    return db.query(models.Brand).all()


def create(request: schemas.BrandCreate, db: Session):
    new_brand = models.Brand(
        brand_name=request.brand_name
    )

    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    return new_brand


def update(id: int, request: schemas.BrandCreate, db: Session):
    brand = db.query(models.Brand).filter(models.Brand.id == id)

    if not brand.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Brand with id {id} not found"
        )

    brand.update(request.dict())
    db.commit()
    return brand.first()


def delete(id: int, db: Session):
    brand = db.query(models.Brand).filter(models.Brand.id == id)

    if not brand.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Brand with id {id} not found"
        )
    brand.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}