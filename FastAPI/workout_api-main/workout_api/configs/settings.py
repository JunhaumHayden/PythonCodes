from pydantic import Field
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://workout:workout@localhost/workout')


settings = Settings()