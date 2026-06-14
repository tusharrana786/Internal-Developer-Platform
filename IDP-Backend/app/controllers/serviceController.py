from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.service import CreateServiceRequest
from app.services.service import create_service

router = APIRouter()


@router.post("/services")
def create_service_endpoint(
    payload: CreateServiceRequest,
    db: Session = Depends(get_db),
):
    return create_service(
        db=db,
        payload=payload,
    )