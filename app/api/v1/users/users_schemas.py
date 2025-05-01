from pydantic import BaseModel, Field
from app.core.models import Users as UsersModel

class UserCreateDTO(BaseModel):
    username: str = Field(..., min_length=1, max_length=50, description="유저 이름")
    email: str = Field(..., min_length=1, max_length=128, description="유저 이메일")
    password: str = Field(..., min_length=8, max_length=128, description="유저 비밀번호")

class UserReadDTO(BaseModel):
    id: int = Field(..., gt=0,description="유저 ID")
    username: str = Field(..., min_length=1, max_length=50, description="유저 이름")
    email: str = Field(..., min_length=1, max_length=128, description="유저 이메일")

    @classmethod
    def of(cls, user: UsersModel) -> "UserReadDTO":
        return cls(
            id=user.id,
            username=user.username,
            email=user.email,
        )
