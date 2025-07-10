"""Core configuration module."""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Main settings class."""
    OPENAI_API_KEY: str

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379 

    class Config:
        """Settings configuration."""
        env_file = ".env"

def get_settings():
    """Get the settings instance."""
    return Settings()
