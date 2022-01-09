from typing import List
from fastapi import FastAPI
from database import engine
from router import user_router
from router import car_router
import models

app = FastAPI()
app.include_router(user_router.router)
app.include_router(car_router.router)

models.Base.metadata.create_all(engine)
