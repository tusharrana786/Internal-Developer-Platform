from fastapi import FastAPI

from app.controllers.healthController import router as health_router
from app.controllers.serviceController import router as service_router
from app.core.config import settings
from app.db.database import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name
)



app.include_router(health_router)
app.include_router(service_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to User Service"
    }