from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, StringConstraints

Title = Annotated[str, StringConstraints(min_length=1, max_length=100)]


class ListItemBase(BaseModel):
    title: Title | None = None
    description: str | None = None


class ListItemCreate(ListItemBase):
    title: Title


class ListItemUpdate(ListItemBase):
    done: bool | None = False


class ListItem(ListItemBase):
    id: int
    done: bool
    list_id: int
    created_at: datetime
    updated_at: datetime


class EmptyTodoList(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    title: Title | None = None


class TodoList(EmptyTodoList):
    items: list[ListItem]
