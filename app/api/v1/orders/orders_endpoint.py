from fastapi import APIRouter, Depends, Path, Body
from app.api.v1.orders import orders_schemas
from app.api.v1.orders.orders_service import OrdersService
from app.core.dependency import get_order_service

router = APIRouter()

@router.get("/{id}",
    response_model=orders_schemas.OrderReadDTO,
    summary="주문 조회 API",
    description="주문을 조회하는 API입니다.",
    response_description="주문 조회 데이터")
def read_order(id: int = Path(
    description="주문 ID", example=1), ordersService: OrdersService = Depends(get_order_service)):
    return orders_schemas.OrderReadDTO.of(ordersService.get_order_by_id(id))

@router.post("/",
    response_model=orders_schemas.OrderReadDTO,
    summary="주문 생성 API",
    description="주문를 생성하는 API입니다.",
    response_description="주문 생성 데이터")
def create_order(order_create_dto: orders_schemas.OrderCreateDTO, 
                      ordersService: OrdersService = Depends(get_order_service)):
    return orders_schemas.OrderReadDTO.of(ordersService.create_order(order_create_dto))

@router.delete("/",
    response_model=None,
    summary="주문 삭제 API",
    description="주문를 삭제하는 API입니다.",
    response_description="None")
async def delete_order(order_create_dto: orders_schemas.OrderCreateDTO, 
                      ordersService: OrdersService = Depends(get_order_service)):
    return ordersService.delete_order(order_create_dto)