from src.db.main import Base
from sqlalchemy import Column , Integer , Text , DateTime
import uuid
import sqlalchemy.dialects.postgresql as pg
from typing import List
from datetime import datetime


class Orders(Base):
    __tablename__="orders"
    id : uuid.UUID = Column(pg.UUID , primary_key=True , nullable=False , default=uuid.uuid4())
    order_name : str =Column(Text , nullable=False)
    created_at : datetime = Column(DateTime , default=datetime.now())

    def __repr__(self):
        return self.order_name