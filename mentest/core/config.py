"""Core configuration module."""
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class Settings(BaseSettings):
    """Main settings class."""
    OPENAI_API_KEY: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = int(load_dotenv().get("REDIS_PORT"))

    class Config:
        """Settings configuration."""
        env_file = ".env"

def get_settings():
    """Get the settings instance."""
    return Settings()
