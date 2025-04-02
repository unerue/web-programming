from beanie import Document
from pydantic import EmailStr, BaseModel, ConfigDict
from src.models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: list[Event] | None = None

    class Settings:
        name = "users"

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "email": "unerue@example.com",
                "password": "strong!!!",
            }
        }
    )


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "unerue@example.com",
                "password": "strong!!!",
            }
        }