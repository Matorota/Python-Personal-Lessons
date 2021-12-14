from fastapi import FastAPI
from database import engine
from router import router_car
import models


app = FastAPI()
app.include_router(router_car.router)

models.Base.metadata.create_all(engine)
