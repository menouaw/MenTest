import streamlit as st
import asyncio
from dotenv import load_dotenv
from mentest.main import run_browser_use_example  # Import the new function

load_dotenv()

st.set_page_config(layout="wide")
st.title("MenTest: Browser Use Example Executor")

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
