from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def get_all(db: Session):
    return db.query(models.Model).all()


def create(request: schemas.ModelCreate, db: Session):
    new_model = models.Model(
        model_name=request.model_name
    )

    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model


def update(id: int, request: schemas.ModelInfo, db: Session):
    model = db.query(models.Model).filter(models.Model.id == id)

    if not model.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Model with id {id} not found"
        )
    model.update(request.dict())
    db.commit()

    return model.first()


def delete(id: int, db: Session):
    model = db.query(models.Model).filter(models.Model.id == id)

    if not model.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Model with id {id} not found"
        )
    model.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}
