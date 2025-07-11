from fastapi.testclient import TestClient
import pytest

# In-memory database from the endpoint file, to reset between tests
from mentest.api.endpoints.project import projects_db
from mentest.api.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def run_around_tests():
    """Fixture to execute before and after each test."""
    # Code that will run before each test
    projects_db.clear()
    yield
    # Code that will run after each test
    projects_db.clear()


def test_create_project_success():
    """
    Tests successful creation of a new project.
    """
    response = client.post(
        "/api/projects/",
        json={"name": "Test Project 1", "start_url": "https://example.com"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Project 1"
    assert data["start_url"] == "https://example.com/"
    assert "id" in data


def test_create_project_duplicate_id():
    """
    Tests that creating a project with a duplicate ID fails.
    """
    # First, create a project
    project_payload = {
        "id": "test-id-123",
        "name": "Original Project",
        "start_url": "https://original.com",
    }
    client.post("/api/projects/", json=project_payload)

    # Now, try to create another with the same ID
    duplicate_payload = {
        "id": "test-id-123",
        "name": "Duplicate Project",
        "start_url": "https://duplicate.com",
    }
    response = client.post("/api/projects/", json=duplicate_payload)

    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]


def test_get_project_not_found():
    """
    Tests that retrieving a non-existent project returns a 404 error.
    """
    response = client.get("/api/projects/non-existent-id")
    assert response.status_code == 404
    assert response.json() == {"detail": "Project not found"}


def test_get_project_success():
    """
    Tests retrieving a single, existing project.
    """
    # First, create a project to retrieve
    response = client.post(
        "/api/projects/",
        json={"name": "My Test App", "start_url": "https://test-app.com"},
    )
    project_id = response.json()["id"]

    # Now, retrieve it
    response = client.get(f"/api/projects/{project_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert data["name"] == "My Test App"


def test_get_all_projects():
    """
    Tests retrieving all projects.
    """
    # Initially, should be empty
    response = client.get("/api/projects/")
    assert response.status_code == 200
    assert response.json() == []

    # Add two projects
    client.post(
        "/api/projects/",
        json={"name": "Project A", "start_url": "https://a.com"},
    )
    client.post(
        "/api/projects/",
        json={"name": "Project B", "start_url": "https://b.com"},
    )

    # Retrieve all
    response = client.get("/api/projects/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Project A"
    assert data[1]["name"] == "Project B" 