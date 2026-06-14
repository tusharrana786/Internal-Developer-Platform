from sqlalchemy.orm import Session

from app.models.service import Service
from app.schemas.service import CreateServiceRequest


def create_service(
    db: Session,
    payload: CreateServiceRequest,
):
    service = Service(
        name=payload.name,
        runtime=payload.runtime,
    )

    db.add(service)
    db.commit()
    db.refresh(service)

    return service