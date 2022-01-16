from pydantic import BaseModel


class UserInfo(BaseModel):
    id: int
    gmail: str
    kategorija: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    gmail: str
    kategorija: str

    class Config:
        orm_mode = True


class BrandCreate(BaseModel):
    brand_name: str


class BrandInfo(BaseModel):
    id: int
    brand_name: str

    class Config:
        orm_mode = True


class ModelCreate(BaseModel):
    model_name: str


class ModelInfo(BaseModel):
    id: int
    model_name: str

    class Config:
        orm_mode = True


class SettingsCreate(BaseModel):
    consumption: str
    odometer: str
    user_id: int


class SettingsInfo(BaseModel):
    id: int
    consumption: str
    odometer: str

    class Config:
        orm_mode = True


class CarCreate(BaseModel):
    year: int
    more_info: str
    price: str
    more_info: str
    brand_id: int
    model_id: int
    users_id: int


class CarInfo(BaseModel):
    year: int
    more_info: str
    price: str

    class Config:
        orm_mode = True


class MileageInfo(BaseModel):
    id: int
    mileage_record: int
    time: str


    class Config:
        orm_mode = True


class MileageCreate(BaseModel):
    mileage_record: int
    time: str
    car_id: int






