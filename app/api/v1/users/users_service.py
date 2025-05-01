from app.core.models import Users as UsersModel
from app.api.v1.users.users_crud import UsersCrud
from app.api.v1.users.users_schemas import UserCreateDTO
from sqlalchemy.orm import Session

class UsersService:
    def __init__(self, db: Session):
        self.crud = UsersCrud(db)
        
    def get_user_by_id(self,user_id: int) -> UsersModel | None:
        return self.crud.find_user_by_id(user_id)
    
    def get_user_by_email(self,user_email: str) -> UsersModel | None:
        return self.crud.find_user_by_email(user_email)
    
    def create_user(self,user_create_dto:UserCreateDTO) -> UsersModel | None:
        user_email= user_create_dto.email
        
        if self.crud.find_user_by_email(user_email) != None:
            raise ValueError("이미 존재하는 유저입니다")
        
        user = UsersModel(
        username = user_create_dto.username,
        email = user_create_dto.email,
        hashed_pw = user_create_dto.password
        )
        return self.crud.save_user(user)
    
    
    def delete_user(self,user_create_dto:UserCreateDTO):
        email = user_create_dto.email
        pw = user_create_dto.password
        
        user: UsersModel | None = self.crud.find_user_by_email(email)
        if user == None:
            raise ValueError("해당하는 email의 유저가 없습니다")
        if user.hashed_pw != pw:
            raise ValueError("비밀번호가 틀렸습니다")
        
        self.crud.delete_user(user)