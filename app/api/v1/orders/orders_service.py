from app.core.models import Orders as OrdersModel
from app.api.v1.orders.orders_crud import OrdersCrud
from app.api.v1.orders.orders_schemas import OrderCreateDTO
from sqlalchemy.orm import Session


class OrdersService:
    def __init__(self, db: Session):
        self.crud = OrdersCrud(db)
        
    def get_order_by_id(self, order_id: int) -> OrdersModel | None:
        return self.crud.find_order_by_id(order_id)
    
    """
    주문 생성 메서드
    Args:
        order_create_dto (OrderCreateDTO): 주문 생성 DTO
    Returns:
        OrdersModel | None: 생성된 주문 모델
    """
    def create_order(self, order_create_dto: OrderCreateDTO) -> OrdersModel | None:
        order = OrdersModel(
            item_id=order_create_dto.item_id,
            quantity=order_create_dto.quantity,
            user_id=order_create_dto.user_id,
        )
        return self.crud.save_order(order)