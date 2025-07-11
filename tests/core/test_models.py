"""Tests for core data models."""

import pytest
from uuid import uuid4, UUID
from pydantic import ValidationError
from mentest.core.models import Project


def test_project_creation_successful():
    """
    Tests that a Project instance can be created successfully with valid data.
    """
    project_id = uuid4()
    project = Project(id=project_id, name="Test Project", start_url="http://example.com")
    assert project.id == project_id
    assert project.name == "Test Project"
    assert str(project.start_url) == "http://example.com/"


def test_project_creation_fails_with_missing_fields():
    """
    Tests that creating a Project instance fails when required fields are missing.
    """
    with pytest.raises(ValidationError):
        Project(name="Incomplete Project")  # Missing start_url


def test_project_creation_fails_with_invalid_url():
    """
    Tests that creating a Project instance fails with an invalid URL.
    """
    with pytest.raises(ValidationError):
        Project(id=uuid4(), name="Invalid URL Project", start_url="not-a-valid-url")


def test_project_creation_fails_with_invalid_id():
    """
    Tests that creating a Project instance fails with an invalid UUID.
    """
    with pytest.raises(ValidationError):
        Project(
            id="not-a-uuid",
            name="Invalid ID Project",
            start_url="http://example.com",
        )
