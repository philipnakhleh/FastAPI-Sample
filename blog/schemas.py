from pydantic import BaseModel
from datetime import date


class Seller(BaseModel):
    first_name: str
    last_name: str
    birthday: date
    email: str
    phone: str
    organization_name: str
    organization_type: str
    organization_website: str
    country: str
    city: str
    postal_code: str
    need_fund: bool
    funding_amount: int
    offer: str
    Description: str
    pain_points: str
    country_code: str
    __verification_code: str = ""
    __verified: bool = False

    def set_verification(self, code: str):
        self.__verification_code = code
        return code


    class Config:
        orm_mode = True


class Buyer(BaseModel):
    first_name: str
    last_name: str
    birthday: date
    email: str
    phone: str
    organization_name: str
    organization_type: str
    organization_website: str
    country: str
    city: str
    postal_code: str
    order: str
    reason: str
    country_code: str
    __verification_code: str
    pain_points: str
    __verified: bool = False

    def set_verification(self, code: str):
        self.__verification_code = code
        return code

    class Config:
        orm_mode = True


class Investor(BaseModel):
    first_name: str
    last_name: str
    birthday: date
    email: str
    phone: str
    organization_name: str
    organization_type: str
    organization_website: str
    country: str
    city: str
    postal_code: str
    amount: int
    communication_time: str
    communication_type: str
    description: str
    pain_points: str
    country_code: str
    __verification_code: str = ""
    __verified: bool = False

    def set_verification(self, code: str):
        self.__verification_code = code
        return code

    class Config:
        orm_mode = True

class Subscribers(BaseModel):
    email: str
    class Config:
        orm_mode = True

class Messages(BaseModel):
    email: str
    content: str
    class Config:
        orm_mode = True

class BlogsPage(BaseModel):
    pagenum: int
    length: int