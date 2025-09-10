from fastapi import FastAPI
from src.orders.routes import orders_routes
from src.db.main import Base , engine
from src.auth.routes import auth_routes



api_version = 'v1'

app = FastAPI(
    version=api_version
)


Base.metadata.create_all(bind=engine)



app.include_router(prefix=f"/api/{api_version}/orders" , router=orders_routes)
app.include_router(prefix=f"/api/{api_version}/auth" , router=auth_routes)

