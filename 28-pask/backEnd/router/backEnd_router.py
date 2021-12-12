from fastapi import APIRouter

from repository import backEnd_repository as repo

router = APIRouter(
    prefix='/api/scrap',
    tags=['Scrapper']
)

@router.get('')
def work():
    return repo.work()
