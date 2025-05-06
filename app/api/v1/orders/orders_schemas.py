from pydantic import BaseModel, Field
from app.core.models import Orders as OrdersModel

class OrderCreateDTO(BaseModel):
    product_id: int = Field(..., gt=0, description="상품 ID")
    quantity: int = Field(..., gt=0, description="주문 수량")
    user_id: int = Field(..., gt=0, description="유저 ID")
    