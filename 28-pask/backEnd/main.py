from fastapi import  FastAPI

from router import backEnd_router


app = FastAPI()
app.include_router(backEnd_router.router)
