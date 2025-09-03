from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import List
from .order_item import OrderItemCreate , OrderItemBase
from .status_enums import OrderStatusEnum

class OrderBase(BaseModel):
    id : UUID
    order_name : str
    created_at : datetime
    updated_at : datetime
    order_items : List[OrderItemBase]
    order_status : OrderStatusEnum

    class Config : 
        orm_mode : True


class CreateOrder(BaseModel):
    order_name : str
    order_items : List[OrderItemCreate]
    class Config : 
        orm_mode : True 