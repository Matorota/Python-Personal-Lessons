from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas

def get_all_users(db: Session):
        return db.query(models.User).all()


def create_users(request: schemas.UserCreate, db: Session):
    new_user = models.User(
        email=request.email,
        password=request.password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return  new_user