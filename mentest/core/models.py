"""Core data models module."""
from uuid import UUID
from pydantic import BaseModel, HttpUrl

class Project(BaseModel):
    """Project model."""
    id: UUID
    name: str
    url: HttpUrl

    model_config = {"from_attributes": True}
