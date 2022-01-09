from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from repository import car_repository as repo


router = APIRouter(
    prefix='/api/Car',
    tags=['Car']
)
