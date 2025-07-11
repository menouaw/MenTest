from fastapi import APIRouter, HTTPException
from typing import Dict, List, Optional
import uuid

from mentest.core.models import Project

router = APIRouter()

# In-memory database for demonstration
projects_db: Dict[str, Project] = {}


@router.post("/projects/", response_model=Project, status_code=201)
async def create_project(project: Project) -> Project:
    """
    Create a new project.

    If an ID is not provided, a new one will be generated.
    """
    if not project.id:
        project.id = str(uuid.uuid4())
    if project.id in projects_db:
        raise HTTPException(
            status_code=400, detail=f"Project with id '{project.id}' already exists."
        )
    projects_db[project.id] = project
    return project


@router.get("/projects/", response_model=List[Project])
async def get_projects() -> List[Project]:
    """
    Retrieve all projects.
    """
    return list(projects_db.values())


@router.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: str) -> Project:
    """
    Retrieve a project by its ID.
    """
    project = projects_db.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project 