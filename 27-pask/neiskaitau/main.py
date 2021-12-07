from fastapi import  FastAPI

from router import scrapper_url


app = FastAPI()
app.include_router(scrapper_url.router)
