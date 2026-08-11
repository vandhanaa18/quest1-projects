"""Application settings configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings with strict validation."""

    app_name: str = "FastAPI Clean Code Example"
    debug_mode: bool = True  # Set to False in production
    
    database_url: str = "sqlite:///./demo.db"
    
    api_root_path: str = "/api/v1"


settings = Settings()
