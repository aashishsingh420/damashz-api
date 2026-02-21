from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Damashz API"
    app_version: str = "0.1.0"

    database_url: str = "postgresql://user:password@localhost:5432/damashz"

    keycloak_url: str = "http://localhost:8080"
    keycloak_realm: str = "damashz"
    keycloak_client_id: str = "damashz-api"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()