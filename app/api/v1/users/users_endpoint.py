from fastapi import APIRouter, Depends, Path, Body
from app.api.v1.users import users_schemas
from app.api.v1.users.users_service import UsersService
from app.core.dependecy import get_users_service

router = APIRouter()

@router.get("/{id}",
    response_model=users_schemas.UserReadDTO,
    summary="유저 조회 API",
    description="유저를 조회하는 API입니다.",
    response_description="유저 조회 데이터")
async def read_user(id: int = Path(
    description="유저 ID", example=1), usersService: UsersService = Depends(get_users_service)):
    return users_schemas.UserReadDTO.of(usersService.get_user_by_id(id))

@router.post("/",
    response_model=users_schemas.UserReadDTO,
    summary="유저 생성 API",
    description="유저를 생성하는 API입니다.",
    response_description="유저 생성 데이터")
async def create_user(user_create_dto: users_schemas.UserCreateDTO, 
                      usersService: UsersService = Depends(get_users_service)):
    return users_schemas.UserReadDTO.of(usersService.create_user(user_create_dto))

@router.delete("/",
    response_model=None,
    summary="유저 삭제 API",
    description="유저를 삭제하는 API입니다.",
    response_description="None")
async def delete_user(user_create_dto: users_schemas.UserCreateDTO, 
                      usersService: UsersService = Depends(get_users_service)):
    return usersService.delete_user(user_create_dto)