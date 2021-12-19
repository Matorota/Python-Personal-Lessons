# from fastapi import status, HTTPException
# from sqlalchemy.orm import Session
# import models
# import schemas
#
# def get_blog_short_info(db: Session):
#     return db.query(models.Blog).all()
#
#
# def get_blog_single_short_info(id: int, db: Session):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#
#     if not blog:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Blog with {id} not found"
#         )
#
#     return blog
#
# def create_blog(request: schemas.BlogPost, db: Session):
#     new_blog = models.Blog(
#         title=request.title,
#         text=request.text,
#         comments=request.comments
#     )
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#
#     return new_blog