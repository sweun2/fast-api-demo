from fastapi import APIRouter
from app.api.v1.users import users_endpoint as users
from app.api.v1.orders import orders_endpoint as orders

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])