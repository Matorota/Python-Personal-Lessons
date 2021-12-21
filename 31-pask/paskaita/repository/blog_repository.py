from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas



def get_all_blog(db: Session):
    return db.query(models.Blog).options(selectinload(models.Blog.owner)).all()


def create_blog(request: schemas.BlogCreate, db: Session, user_id: int):
    new_post = models.Blog(
        title=request.title,
        body=request.body,
        owner_id=user_id, # relashions
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
