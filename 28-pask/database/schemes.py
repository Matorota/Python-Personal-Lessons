from pydantic import  BaseModel

class HumasShortInfo(BaseModel):
    first_name: str
    last_name: str