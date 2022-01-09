from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from repository import user_repository as repo

router = APIRouter(
    prefix='/api/user',
    tags=['Users']
)