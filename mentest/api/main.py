from fastapi import FastAPI
from mentest.api.endpoints import project

app = FastAPI(title="Mentest API")

app.include_router(project.router, prefix="/api", tags=["Projects"])


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint for the API.
    """
    return {"message": "Welcome to the Mentest API"} 