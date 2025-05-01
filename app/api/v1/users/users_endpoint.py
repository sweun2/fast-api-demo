from fastapi import APIRouter, Depends
from app.api.v1.users import users_schemas
from app.api.v1.users.users_service import UsersService
from app.core.dependecy import get_users_service


router = APIRouter()
@router.get("/{id}", response_model=users_schemas.UserReadDTO)
async def read_user(id: int, usersService: UsersService = Depends(get_users_service)):
    return users_schemas.UserReadDTO.of(usersService.get_user_by_id(id))

@router.post("/", response_model=users_schemas.UserReadDTO)
async def create_user(user_create_dto: users_schemas.UserCreateDTO, 
                      usersService: UsersService = Depends(get_users_service)):
    return users_schemas.UserReadDTO.of(usersService.create_user(user_create_dto))

@router.delete("/", response_model=None)
async def delete_user(user_create_dto: users_schemas.UserCreateDTO, 
                      usersService: UsersService = Depends(get_users_service)):
    return usersService.delete_user(user_create_dto)