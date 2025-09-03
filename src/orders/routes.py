from fastapi import APIRouter



orders_routes = APIRouter()



@orders_routes.get('/')
async def get_orders():
    return "Getting the orders"


