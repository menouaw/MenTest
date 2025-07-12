import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import sys
import os
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
import asyncio
from dotenv import load_dotenv
from mentest.main import run_browser_use_example

load_dotenv()

st.set_page_config(layout="wide")
st.title("MenTest: Browser Use Example Executor")

# Install Playwright browsers if not already installed
if "playwright_installed" not in st.session_state:
    with st.spinner("Installing Playwright browsers... This may take a moment."):
        try:
            result = subprocess.run(
                [sys.executable, "-m", "playwright", "install"],
                capture_output=True,
                text=True,
                check=True,
            )
            st.success("Playwright browsers installed successfully!")
            st.code(result.stdout)
            st.session_state.playwright_installed = True
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to install Playwright browsers: {e}")
            st.code(e.stderr)
        except FileNotFoundError:
            st.error(
                "Playwright command not found. Make sure it's installed in your environment."
            )

# Streamlit UI

if st.button("Run Browser Use Example", key="run_example_button"):
    with st.spinner("Running Browser Use example... This may take a moment."):
        result = asyncio.run(run_browser_use_example())
        if result:
            st.success("Execution Complete!")
            st.write("Result:")
            st.code(result, language="text")
        else:
            st.error("An error occurred or no result was returned.")
