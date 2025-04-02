from beanie import Document
from pydantic import BaseModel, ConfigDict


class Event(Document):
    title: str
    image: str
    description: str
    tags: list[str]
    location: str

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "title": "FastAPI BookLaunch",
    #             "image": "https://linktomyimage.com/image.png",
    #             "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
    #             "tags": ["python", "fastapi", "book", "launch"],
    #             "location": "Google Meet"
    #         }
    #     }
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "FastAPI BookLaunch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
    )

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: str | None = None
    image: str | None = None
    description: str | None = None
    tags: list[str] | None = None
    location: str | None = None

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI BookLaunch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
