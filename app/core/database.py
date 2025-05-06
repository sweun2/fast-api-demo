from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

engine = create_engine(
    settings.db_url,
    pool_pre_ping=True,
    pool_recycle=1800,  # 커넥션 재활성화 주기(초)
    pool_size=20,        # 기본 5 → 20으로 증가
    max_overflow=30,    # 기본 10 → 30으로 증가
    pool_timeout=30,    # 대기 시간(초)
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        raise
    finally:
        db.close()