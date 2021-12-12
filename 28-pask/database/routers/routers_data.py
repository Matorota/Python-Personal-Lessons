from fastapi import APIRouter, Depends
from typing import  List
from sqlalchemy.orm import  Session
import models
import schemes
from database_alchemy import  get_db

router = APIRouter(
    prefix='/api/human',
    tags=['Humans']
)

@router.get('')
def all(db: Session = Depends(get_db)):
    humans = db.query(models.Human).all() # selectina visus
    return humans

@router.post('')
def create(request: schemes.HumasShortInfo, db: Session = Depends(get_db)):
    new_human = models.Human(first_name= request.first_name, last_name= request.last_name, email= 'wa@se.com')
    db.add(new_human)
    db.commit()
    db.refresh(new_human)

    return new_human
    print(request)

