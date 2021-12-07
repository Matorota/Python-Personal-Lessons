from fastapi import APIRouter

from repository import repository as repo

router = APIRouter(
    prefix='/api/scrap',
    tags=['Scrapper']
)

@router.get('')
def hello():
    return repo.hello()
