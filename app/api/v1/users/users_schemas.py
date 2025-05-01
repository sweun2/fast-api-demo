from pydantic import BaseModel, EmailStr
from app.core.models import Users as UsersModel

class UserCreateDTO(BaseModel):
    username: str
    email: str
    password: str

class UserReadDTO(BaseModel):
    id: int
    username: str
    email: str

    @classmethod
    def of(cls, user: UsersModel) -> "UserReadDTO":
        return cls(
            id=user.id,
            username=user.username,
            email=user.email,
        )
