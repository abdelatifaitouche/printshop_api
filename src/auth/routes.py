from fastapi import APIRouter
from .schemas import CreateUser , UserLogin
from src.db.main import get_db
from fastapi import Depends
from sqlalchemy.orm.session import Session
from .models import User
from .service import AuthService

import logging


logs = logging.Logger(name="logs")



auth_routes = APIRouter()

auth_service =AuthService()


@auth_routes.post("/add_user" , response_model=CreateUser)
def create_user(user_data : CreateUser , db : Session = Depends(get_db)):

    new_user = auth_service.create_user(user_data , db)

    return new_user


@auth_routes.post("/login")
def login(user_data : UserLogin , db : Session = Depends(get_db)) -> str:
    return auth_service.login_user(user_data , db)




@auth_routes.get("/check_user")
def check_user(user_email : str , db : Session = Depends(get_db)):
    return auth_service.user_exists(user_email , db)