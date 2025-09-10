from sqlalchemy.orm import mapped_column , Mapped
from src.db.main import Base
from sqlalchemy import DateTime , Text
import sqlalchemy.dialects.postgresql as pg
import uuid
from typing import List 
from datetime import datetime
from .roles import Roles





class User(Base):
    __tablename__="users"

    id : Mapped[uuid.UUID] = mapped_column(pg.UUID , nullable=False , default=uuid.uuid4, primary_key=True, index=True)
    username : Mapped[str] = mapped_column(Text , nullable=False)
    email : Mapped[str] = mapped_column(Text, nullable=False)
    password_hash : Mapped[str] = mapped_column(Text , nullable=False)
    role : Mapped[str]  = mapped_column(Text , nullable=False , server_default=Roles.CLIENT)


    created_at : Mapped[DateTime] = mapped_column(DateTime , default=datetime.now())
    updated_at : Mapped[DateTime] = mapped_column(DateTime , default=datetime.now())


    def __repr__(self):
        return f"User : {self.username} --> Role {self.role}"