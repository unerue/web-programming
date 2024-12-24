from typing import List, Optional

from fastapi import Form
from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: int | None = Field(default=None, example=1)
    item: str = Field(..., example="Example schema!")

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)


class TodoItem(BaseModel):
    item: str = Field(..., example="Read the next chapter of the book")


class TodoItems(BaseModel):
    todos: List[TodoItem] = Field(
        ...,
        example=[{"item": "Example schema 1!"}, {"item": "Example schema 2!"}],
    )
