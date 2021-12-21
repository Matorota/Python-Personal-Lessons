from typing import List
from fastapi import FastAPI
from database import engine
from router import users_routers
from router import blog_routers
import models

app = FastAPI()
app.include_router(users_routers.router)
app.include_router(blog_routers.router)

models.Base.metadata.create_all(engine)
