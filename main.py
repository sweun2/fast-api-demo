from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.v1.routers import api_router
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from app.core.database import Base, engine, SessionLocal
from app.core.models import Items, Users
from app.core.middleware import LoggingMiddleware
from fastapi.middleware.cors import CORSMiddleware
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

# 마이그레이션 툴 도입 x
def on_startup():
    
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    
def seed_default_items():
    session: Session = SessionLocal()
    try:
        if session.query(Items).count() == 0:
            defaults = [
                Items(itemname="item1", price=1000, quantity=1000),
                Items(itemname="item2", price=2000, quantity=1000),
                Items(itemname="item3", price=3000, quantity=1000),
            ]
            session.add_all(defaults)
            session.commit()
        if session.query(Users).count() == 0:
            defaults = [
                Users(username="user1", email="test@gmail.com", hashed_pw="1234"),
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
app.add_middleware(LoggingMiddleware)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api/v1")      