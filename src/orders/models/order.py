from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.orders.models.base import BaseModel
from src.orders.schemas.status_enums import OrderStatusEnum

class Orders(BaseModel):
    __tablename__ = "orders"

    order_name: Mapped[str] = mapped_column(Text, nullable=False)
    order_items = relationship("OrderItem", back_populates="order", lazy="dynamic")
    order_status : Mapped[str] = mapped_column(Text , default=OrderStatusEnum.PENDING.value)

    def __repr__(self) -> str:
        return self.order_name
