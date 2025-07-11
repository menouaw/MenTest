import streamlit as st

st.set_page_config(
    page_title="Mentest Home",
    page_icon="✅",
    layout="wide",
)

st.title("Welcome to Mentest! ✅")

st.markdown(
    """
    Mentest is an AI-powered QA platform designed to automate the full testing
    lifecycle for your web applications.

    **👈 Select a page from the sidebar** to get started.

    ### Workflow
    1.  **Project Setup**: Configure your target application URL.
    2.  **Site Exploration**: Automatically discover pages and components.
    3.  **Test Generation**: Create test cases and Gherkin scenarios.
    4.  **Test Execution**: Run tests and generate automation scripts.
    5.  **Results Dashboard**: Visualize test outcomes in an Allure report.
"""
) 