from app.core.models import Orders as OrdersModel
from app.api.v1.orders.orders_crud import OrdersCrud
from app.api.v1.items.items_crud import ItemsCrud
from app.api.v1.orders.orders_schemas import OrderCreateDTO
from sqlalchemy.orm import Session


class OrdersService:
    def __init__(self, db: Session):
        self.db = db
        self.order_curd = OrdersCrud(db)
        self.item_curd = ItemsCrud(db)
        
    def get_order_by_id(self, order_id: int) -> OrdersModel | None:
        return self.order_curd.find_order_by_id(order_id)
    
    """
    주문 생성 메서드
    Args:
        order_create_dto (OrderCreateDTO): 주문 생성 DTO
    Returns:
        OrdersModel | None: 생성된 주문 모델
    Description:
        주문 생성 시 해당 개수만큼 아이템 차감
    """
    def create_order(self, order_create_dto: OrderCreateDTO) -> OrdersModel | None:
        order = OrdersModel(
            item_id=order_create_dto.item_id,
            quantity=order_create_dto.quantity,
            user_id=order_create_dto.user_id,
        )
        item = self.item_curd.find_item_by_id_with_for_update(order_create_dto.item_id)
        if item is None:
            raise ValueError("해당하는 아이템이 없습니다")
        if item.quantity < order_create_dto.quantity:
            raise ValueError("아이템 수량이 부족합니다")
        item.quantity -= order_create_dto.quantity
        item = self.item_curd.save_item_without_commit(item)
        order = self.order_curd.save_order_without_commit(order)
        self.db.commit()
        return order
    
    """
    주문 삭제 메서드
    Args:
        order_id (int): 주문 ID
    Returns:
        None
    """
    def delete_order(self, order_id: int) -> None:
        order: OrdersModel | None = self.order_curd.find_order_by_id(order_id)
        if order is None:
            raise ValueError("해당하는 주문이 없습니다")
        
        self.order_curd.delete_order(order)
    