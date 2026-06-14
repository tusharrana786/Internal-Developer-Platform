from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Internal Development Platform"


settings = Settings()