from sqlalchemy.orm import Session
from app.core.models import Users as UsersModel

class UsersCrud:
    def __init__(self, db: Session):
        self.db = db
        
    def find_user_by_id(self, user_id: int) -> UsersModel | None:
        return self.db.query(UsersModel).filter(UsersModel.id == user_id).first()

    def find_user_by_email(self, user_email: str) -> UsersModel | None:
        return self.db.query(UsersModel).filter(UsersModel.email == user_email).first()

    def save_user(self,user: UsersModel) -> UsersModel:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self,user: UsersModel) -> None:
        self.db.delete(user)
        self.db.commit()