# MenTest

Mentest is a comprehensive, user-friendly QA testing platform that automates the entire testing lifecycle for web applications.

## Getting Started

Follow these instructions to set up your local development environment.

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (a fast Python package installer and resolver)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/menouaw/mentest.git
    cd mentest
    ```

2.  **Create and activate the virtual environment:**

    This project uses `uv` to manage the virtual environment and dependencies.

    ```bash
    # Create the virtual environment using Python 3.11
    uv venv --python 3.11

    # Activate the virtual environment
    # On Windows (Bash):
    source .venv/Scripts/activate
    # On Windows (PowerShell):
    .venv\Scripts\Activate.ps1
    # On macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    uv pip install -r requirements.txt
    ```

4.  **Install the project in editable mode:**

    This makes the `mentest` package visible to Python, which is necessary for the application to run correctly.

    ```bash
    uv pip install -e .
    ```

5.  **Set up environment variables:**

    Copy the example environment file and fill in your details, such as your OpenAI API key.

    ```bash
    cp .env.example .env
    ```

    Now, open the `.env` file and add your credentials.

## Running the Application

To run the platform, you need to start both the backend API and the frontend UI in separate terminals.

### 1. Start the Backend (FastAPI)

In your first terminal, make sure your virtual environment is activated, then run:

```bash
uvicorn mentest.api.main:app --reload --port 8000
```

### 2. Start the Frontend (Streamlit)

In a second terminal, activate the virtual environment and run:

```bash
streamlit run mentest/app/Mentest.py
```

The application will be available at `http://localhost:8501`.
