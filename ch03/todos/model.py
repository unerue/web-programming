from typing import List

from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: int = Field(..., example=1)
    item: str = Field(..., example="Example schema!")


class TodoItem(BaseModel):
    item: str = Field(..., example="Read the next chapter of the book")


class TodoItems(BaseModel):
    todos: List[TodoItem] = Field(
        ...,
        example=[{"item": "Example schema 1!"}, {"item": "Example schema 2!"}],
    )
