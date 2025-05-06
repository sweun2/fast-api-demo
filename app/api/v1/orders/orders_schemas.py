from pydantic import BaseModel, Field
from app.core.models import Orders as OrdersModel

class OrderReadDTO(BaseModel):
    id: int = Field(..., gt=0, description="주문 ID")
    item_id: int = Field(..., gt=0, description="상품 ID")
    quantity: int = Field(..., gt=0, description="주문 수량")
    user_id: int = Field(..., gt=0, description="유저 ID")

    @classmethod
    def of(cls, order: OrdersModel) -> "OrderReadDTO":
        return cls(
            id=order.id,
            item_id=order.item_id,
            quantity=order.quantity,
            user_id=order.user_id,
        )

class OrderCreateDTO(BaseModel):
    item_id: int = Field(..., gt=0, description="상품 ID")
    quantity: int = Field(..., gt=0, description="주문 수량")
    user_id: int = Field(..., gt=0, description="유저 ID")

