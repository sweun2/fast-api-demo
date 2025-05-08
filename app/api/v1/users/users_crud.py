from sqlalchemy.orm import Session
from app.core.models import Users as UsersModel

class UsersCrud:
    def __init__(self, db: Session):
        self.db = db
    
    def find_user_by_id(self, user_id: int) -> UsersModel | None:
        return self.db.query(UsersModel).filter(UsersModel.id == user_id).first()
    
    def find_user_by_email(self, user_email: str) -> UsersModel | None:
        """
        유저 이메일로 유저 찾기 메서드
        Args:
            user_email (str): 유저 이메일
        Returns:
            UsersModel | None: 유저 모델
        """
        return self.db.query(UsersModel).filter(UsersModel.email == user_email).first()

    def save_user(self,user: UsersModel) -> UsersModel:
        """
        유저 생성 메서드
        Args:
            user (UsersModel): 유저 모델
        Returns:
            UsersModel | None: 생성된 유저 모델
        Commit: True
        """
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self,user: UsersModel) -> None:
        """
        유저 삭제 메서드
        Args:
            user (UsersModel): 유저 모델
        Returns:
            None
        Commit: True
        """
        self.db.delete(user)
        self.db.commit()