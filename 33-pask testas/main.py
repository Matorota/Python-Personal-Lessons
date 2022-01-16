from typing import List
from fastapi import Depends, FastAPI
from database import engine
from fastapi.security import OAuth2PasswordBearer
from router import user_router, brand_router, model_router, settings_router, car_router, mileage_router
import models

app = FastAPI()
app.include_router(user_router.router)
app.include_router(brand_router.router)
app.include_router(model_router.router)
app.include_router(settings_router.router)
app.include_router(car_router.router)
app.include_router(mileage_router.router)

models.Base.metadata.create_all(engine)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
