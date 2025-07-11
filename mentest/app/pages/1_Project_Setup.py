import streamlit as st
import requests
import json
import os

from pydantic import ValidationError
from mentest.core.models import Project

API_URL = os.getenv("MENTEST_API_URL", "http://localhost:8000/api")

st.title("📝 Project Setup")

st.markdown("Define a new project to begin testing.")

with st.form("project_form"):
    project_name = st.text_input("Project Name", 
                                 value="OrangeHRM",
                                 placeholder="e.g., My E-commerce Site")
    start_url = st.text_input("Start URL", 
                              value="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
                              placeholder="https://example.com")
    submitted = st.form_submit_button("Create Project")

if submitted:
    if not project_name or not start_url:
        st.error("Please provide both a project name and a start URL.")
    else:
        try:
            project_data = Project(name=project_name, start_url=start_url)
            response = requests.post(
                f"{API_URL}/projects/",
                data=project_data.model_dump_json(),
                headers={"Content-Type": "application/json"},
                timeout=10,
            )
            if response.status_code == 201:
                st.success(f"Project '{project_name}' created successfully!")
                st.json(response.json())
            else:
                st.error(f"Error creating project: {response.text}")
        except ValidationError:
            st.error("Invalid URL format. Please enter a full URL (e.g., 'https://example.com').")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to connect to the backend API: {e}")

st.divider()

st.header("Existing Projects")

try:
    response = requests.get(f"{API_URL}/projects/", timeout=10)
    if response.status_code == 200:
        projects = response.json()
        if projects:
            st.table(projects)
        else:
            st.info("No projects found. Create one above to get started.")
    else:
        st.error("Could not retrieve projects from the backend.")
except requests.exceptions.RequestException as e:
    st.warning(f"Backend API not available: {e}") 