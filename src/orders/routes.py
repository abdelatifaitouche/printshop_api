from fastapi import APIRouter , Depends
from src.db.main import get_db
from sqlalchemy.orm.session import Session
from sqlalchemy import select
from src.orders.models import Orders
from src.orders.schemas import CreateOrder , OrderBase
from typing import List
from src.orders.service import OrderService
from uuid import UUID




orders_routes = APIRouter()
orders_service = OrderService()


@orders_routes.get("/order_id" , response_model=OrderBase)
def get_order(order_id : UUID , db : Session = Depends(get_db)):
    order = orders_service.get_order_by_id(order_id , db)
    return order





@orders_routes.get('/' , response_model=List[OrderBase])
def get_orders(db:Session = Depends(get_db)):
    orders : List[OrderBase] = orders_service.get_all_orders(db)
    return orders




@orders_routes.post('/create_order' , response_model=OrderBase)
def create_order(order_data : CreateOrder , db : Session = Depends(get_db)):
    new_order = orders_service.create_order(order_data , db)
    return new_order

