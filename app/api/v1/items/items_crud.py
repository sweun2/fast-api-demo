from sqlalchemy.orm import Session
from app.core.models import Items as ItemsModel

class ItemsCrud:
    def __init__(self, db: Session):
        self.db = db
        
    def find
    
    def find_user_by_id(self, user_id: int) -> UsersModel | None:
        return self.db.query(UsersModel).filter(UsersModel.id == user_id).first()
    """
    유저 이메일로 유저 찾기 메서드
    Args:
        user_email (str): 유저 이메일
    Returns:
        UsersModel | None: 유저 모델
    """
    def find_user_by_email(self, user_email: str) -> UsersModel | None:
        return self.db.query(UsersModel).filter(UsersModel.email == user_email).first()
    """
    유저 생성 메서드
    Args:
        user (UsersModel): 유저 모델
    Returns:
        UsersModel | None: 생성된 유저 모델
    Commit: True
    """
    def save_user(self,user: UsersModel) -> UsersModel:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    """
    유저 삭제 메서드
    Args:
        user (UsersModel): 유저 모델
    Returns:
        None
    Commit: True
    """
    def delete_user(self,user: UsersModel) -> None:
        self.db.delete(user)
        self.db.commit()