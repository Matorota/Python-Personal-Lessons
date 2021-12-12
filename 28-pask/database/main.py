from fastapi import FastAPI
from database_alchemy import engine
from routers import routers_data
import models


app = FastAPI()
app.include_router(routers_data.router)

models.Base.metadata.create_all(engine)
