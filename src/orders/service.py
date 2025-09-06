from sqlalchemy import select
from src.orders.models.order import Orders
from src.orders.schemas.order import CreateOrder , OrderBase
from uuid import UUID
from sqlalchemy.orm.session import Session
from sqlalchemy import select
from src.orders.models import Orders , OrderItem
from fastapi.exceptions import HTTPException
from fastapi import status
from typing import List


class OrderService : 

    def get_all_orders(self , db : Session) -> List[OrderBase] : 
        statement = select(Orders)
        orders = db.execute(statement).scalars().all()
        return orders


    def get_order_by_id(self , order_id : UUID , db : Session) -> OrderBase:
        """
            Returns an order based on the provided ID,

            raise an exception if not found
        """
        statement = select(Orders).where(Orders.id == order_id)
        order = db.execute(statement).scalars().first()

        if order is None : 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , detail='No Order found')

        return order
    

    def create_order(self , order_data : CreateOrder , db : Session) -> OrderBase:
        """
            Creates an Order, and Order Itrems related

            Since every order can contains mutliple items to process

        """

        order = Orders(order_name = order_data.order_name)
        
        for order_item in order_data.order_items :
            item = OrderItem(item_name=order_item.item_name)
            order.order_items.append(item)

        db.add(order)
        db.commit()
        db.refresh(order)
        return order
    
    
    def update_order():
        return
    

    def delete_order(self , order_id : UUID , db : Session) -> None:
        order = self.get_order_by_id(order_id , db)
        db.delete(order)
        db.commit()
        
    


    def get_order_item_by_id():
        return