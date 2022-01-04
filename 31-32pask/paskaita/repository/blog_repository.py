from fastapi import status, HTTPException
from sqlalchemy.orm import Session, selectinload
import models
import schemas



def get_all_blog(active : int, db: Session):
    if active < 0 or active > 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Wrong active state passed"
        )
        return db.query(models.Blog)\
            .join(models.PostSettings)\
            .options(selectinload(models.Blog.owner))\
            .options(selectinload(models.Blog.settings))\
            .filter(models.PostSettings.is_active == active).all()


def create_blog(request: schemas.BlogCreate, db: Session, user_id: int):
    new_settings = models.PostSettings(
        is_active=request.settings.is_active
    )
    db.add(new_settings)
    db.commit()
    db.refresh(new_settings)

    new_post = models.Blog(
        title=request.title,
        body=request.body,
        owner_id=user_id, # relashions
        setting_id=new_settings.id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def update_blog(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.blog).filter(models.blog.id == id)

    if not human.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog.update(request.dict())
    db.commit()

    return blog.first()
