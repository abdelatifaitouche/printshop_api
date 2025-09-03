from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class OrderBase(BaseModel):
    id : UUID
    order_name : str
    created_at : datetime

    class Config : 
        orm_mode : True


class CreateOrder(OrderBase):
    class Config : 
        orm_mode : True 