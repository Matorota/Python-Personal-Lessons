from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def get_humans_short_info(db: Session):
    return db.query(models.Human).all()


def get_human_single_short_info(id: int, db: Session):
    human = db.query(models.Human).filter(models.Human.id == id).first()

    if not human:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Human with {id} not found"
        )

    return human

def create_human(request: schemas.HumanPost, db: Session):
    new_human = models.Human(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email
    )
    db.add(new_human)
    db.commit()
    db.refresh(new_human)

    return new_human

def update_human(id: int, request: schemas.HumanPost, db: Session):
    human = db.query(models.Human).filter(models.Human.id == id)

    if not human.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Human with id {id} not found"
        )

    human.update(request.dict())
    db.commit()

    return human.first()

def delete_human(id: int, db: Session):
    human = db.query(models.Human).filter(models.Human.id == id)

    if not human.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Human with id {id} not found"
        )
    human.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}