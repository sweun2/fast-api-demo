from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.v1.routers import api_router

app = FastAPI(
    title="My FastAPI Project",
    description="API documentation",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")


# 마이그레이션 툴 도입 x
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)