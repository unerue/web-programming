import os

from sqlmodel import SQLModel, Session, create_engine
from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

from models.events import Event


class Settings(BaseSettings):
    DATABASE_URL: str
    SQLITE_DB: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        pyproject_toml_table_header=("tool", "poetry"),
        toml_file="pyproject.toml",
    )


settings = Settings(_env_file=".env")


# database_file = "planner.db"
# database_connection_string = f"sqlite:///{database_file}"

connect_args = {"check_same_thread": False}
engine_url = create_engine(
    settings.DATABASE_URL, echo=True, connect_args=connect_args
)


def conn():
    SQLModel.metadata.create_all(
        engine_url,
    )


def get_session():
    with Session(engine_url) as session:
        yield session
