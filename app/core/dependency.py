from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.v1.users.users_service import UsersService
from app.api.v1.orders.orders_service import OrdersService

def get_service_factory(service_cls):
    def _get_service(db: Session = Depends(get_db)):
        return service_cls(db)
    return _get_service

get_user_service = get_service_factory(UsersService)
get_order_service = get_service_factory(OrdersService)