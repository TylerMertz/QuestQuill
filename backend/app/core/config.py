from pydantic_settings import BaseSettings
from pydantic import Field
import os

BASE_PATH = os.path.abspath(os.path.dirname(__name__))

class Settings(BaseSettings):
    env: str = Field(..., env="ENV")
    debug: bool = Field(..., env="DEBUG")

    pg_host: str = Field(..., env="PG_HOST")
    pg_port: int = Field(..., env="PG_PORT")
    pg_db: str = Field(..., env="PG_DB")
    pg_username: str = Field(..., env="PG_USERNAME")
    pg_password: str = Field(..., env="PG_PASSWORD")

    class Config:
        env_file = ".env"

settings = Settings()
print(settings)
