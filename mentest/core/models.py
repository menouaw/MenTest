"""Core data models module."""
from uuid import UUID
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
import uuid
from enum import Enum


class TestStatus(str, Enum):
    """Enumeration for test execution statuses."""
    PASSED = "passed"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"


class Project(BaseModel):
    """Represents a testing project."""

    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    start_url: HttpUrl


class TestScenario(BaseModel):
    """Represents a Gherkin test scenario."""

    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    project_id: str
    title: str
    gherkin: str


class ExecutionResult(BaseModel):
    """Represents the result of a test execution."""

    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    scenario_id: str
    status: TestStatus
    allure_report_path: Optional[str] = None
