# from beanie import Document
from sqlmodel import SQLModel

from pydantic import BaseModel, EmailStr


class User(SQLModel, table=True):
    email: EmailStr
    password: str

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {"email": "fastapi@packt.com", "password": "strong!!!"}
        }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
