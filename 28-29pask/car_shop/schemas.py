from pydantic import BaseModel

class CarShortInfo(BaseModel):
    brand: str
    year: str
    price: str

    class Config:
        orm_mode = True


class CarPost(BaseModel):
    brand: str
    year: str
    price: str
    horsePower: str
    informacion: str
