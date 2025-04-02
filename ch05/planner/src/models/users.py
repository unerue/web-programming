from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict
from src.models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: list[Event] | None = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }
    )


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }
    )