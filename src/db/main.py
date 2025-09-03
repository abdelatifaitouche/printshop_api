from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = 'postgresql://dbmanager:dbpassword@localhost:5432/testdb'

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(bind=engine , autoflush=False , autocommit=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try : 
        yield db
    finally : 
        db.close()