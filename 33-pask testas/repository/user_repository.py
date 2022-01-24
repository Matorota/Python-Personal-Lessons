from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas


def get_all(db: Session):
    return db.query(models.User).all()


def create(request: schemas.UserCreate, db: Session):
    new_user = models.User(
        gmail=request.gmail,
        kategorija=request.kategorija,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def update(id: int, request: schemas.UserInfo, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    user.update(request.dict())
    db.commit()

    return user.first()


def delete(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    user.delete(synchronize_session=False)
    db.commit()

    return {"details": "Success"}