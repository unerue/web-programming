from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: int = Field(..., example=1)
    item: str = Field(..., example="Example Schema!")


class TodoItem(BaseModel):
    item: str = Field(..., example="Read the next chapter of the book")
