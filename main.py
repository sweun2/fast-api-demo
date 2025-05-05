from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.v1.routers import api_router
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from app.core.database import Base, engine, SessionLocal
from app.core.models import Items



# 마이그레이션 툴 도입 x
def on_startup():
    Base.metadata.create_all(bind=engine)
    
def seed_default_items():
    session: Session = SessionLocal()
    try:
        # 이미 데이터가 있으면 삽입 생략
        if session.query(Items).count() == 0:
            defaults = [
                Items(itemname="item1", price=1000),
                Items(itemname="item2", price=2000),
                Items(itemname="item3", price=3000),
            ]
            session.add_all(defaults)
            session.commit()
    finally:
        session.close()
        
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    on_startup()
    seed_default_items()
    yield
    # Shutdown code    

app = FastAPI(
    title="My FastAPI Project",
    description="API documentation",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api/v1")      