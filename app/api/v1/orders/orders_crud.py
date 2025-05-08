from sqlalchemy.orm import Session
from app.core.models import Orders as OrdersModel

class OrdersCrud:
    def __init__(self, db: Session):
        self.db = db
        
    def find_order_by_id(self, order_id: int) -> OrdersModel | None:
        return self.db.query(OrdersModel).filter(OrdersModel.id == order_id).first()
    

    def save_order(self, order: OrdersModel) -> OrdersModel:
        """
        주문 저장 메서드
        Args:
            order (OrdersModel): 주문 모델
        Returns:
            OrdersModel | None: 생성된 주문 모델
        Commit: True
        """
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order
    
    def save_order_without_commit(self, order: OrdersModel) -> OrdersModel:
        """
        주문 저장 메서드 (커밋 없이 저장)
        Args:
            order (OrdersModel): 주문 모델
        Returns:
            OrdersModel | None: 생성된 주문 모델
        Commit: False
        """
        
        self.db.add(order)
        self.db.flush()
        return order


    def delete_order(self, order: OrdersModel) -> None:
        """
        주문 삭제 메서드
        Args:
            order (OrdersModel): 주문 모델
        Returns:
            None
        Commit: True
        """
        self.db.delete(order)
        self.db.commit()