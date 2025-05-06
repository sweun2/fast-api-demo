from sqlalchemy.orm import Session
from app.core.models import Orders as OrdersModel

class OrdersCrud:
    def __init__(self, db: Session):
        self.db = db
        
    def find_order_by_id(self, order_id: int) -> OrdersModel | None:
        return self.db.query(OrdersModel).filter(OrdersModel.id == order_id).first()
    
    """
    주문 저장 메서드
    Args:
        order (OrdersModel): 주문 모델
    Returns:
        OrdersModel | None: 생성된 주문 모델
    Commit: True
    """
    def save_order(self, order: OrdersModel) -> OrdersModel:
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order
    """
    주문 삭제 메서드
    Args:
        order (OrdersModel): 주문 모델
    Returns:
        None
    Commit: True
    """
    def delete_order(self, order: OrdersModel) -> None:
        self.db.delete(order)
        self.db.commit()