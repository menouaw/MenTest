"""Core data models module."""
from pydantic import BaseModel

class Project(BaseModel):
    """Project model."""
    id: str
    name: str
    url: str
