from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.orders.models.base import BaseModel
import uuid
import sqlalchemy.dialects.postgresql as pg
from src.orders.schemas.status_enums import ItemStatusEnum

class OrderItem(BaseModel):
    __tablename__ = "order_items"

    item_name: Mapped[str] = mapped_column(Text, nullable=False)
    order_id: Mapped[uuid.UUID] = mapped_column(pg.UUID, ForeignKey("orders.id"), nullable=False)
    order = relationship("Orders", back_populates="order_items")
    item_status : Mapped[str] = mapped_column(Text , default=ItemStatusEnum.PENDING.value)

    def __repr__(self) -> str:
        return self.item_name
