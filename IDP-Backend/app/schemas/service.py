from pydantic import BaseModel


class CreateServiceRequest(BaseModel):
    name: str
    runtime: str