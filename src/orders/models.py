from src.db.main import Base
from sqlalchemy import Column , Integer , Text
from uuid import UUID



class Commands(Base):
    __tablename__="Commands"
    id = Column(Integer , primary_key=True , nullable=False)
    title=Column(Text , nullable=False)


    def __repr__(self):
        return self.title