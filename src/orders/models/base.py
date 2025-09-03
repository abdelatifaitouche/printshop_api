from src.db.main import Base
from sqlalchemy import Column ,DateTime
import uuid
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from sqlalchemy.orm import Mapped , mapped_column


class BaseModel(Base):

    """

    This is the baseModel that all the model will inherit from 

    to avoid the id, created, updated , and user duplication written on every model

    """

    __abstract__ = True


    id : Mapped[uuid.UUID] = mapped_column(pg.UUID , primary_key=True , nullable=False , default=uuid.uuid4)
    created_at : Mapped[datetime] = mapped_column(DateTime , default=datetime.now())
    updated_at : Mapped[datetime] = mapped_column(DateTime , default=datetime.now())

    