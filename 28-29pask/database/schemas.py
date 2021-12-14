from pydantic import BaseModel

class HumanShortInfo(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class HumanPost(BaseModel):
    first_name: str
    last_name: str
    email: str
