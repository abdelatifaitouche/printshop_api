from pydantic import BaseModel
from uuid import UUID
from .status_enums import ItemStatusEnum


class OrderItemBase(BaseModel):
    id : UUID
    item_name : str
    item_status : ItemStatusEnum

class OrderItemCreate(BaseModel):
    item_name : str 




