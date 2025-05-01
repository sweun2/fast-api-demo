from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.v1.users.users_service import UsersService

def get_users_service(
    db: Session = Depends(get_db)
) -> UsersService:
    return UsersService(db)