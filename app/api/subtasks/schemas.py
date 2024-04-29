from pydantic import BaseModel
from datetime import datetime


class SubTask(BaseModel):
    id: int
    title: str
    body: str
    completed: bool
    created_at: datetime
    task_id: int


class SubTaskCreate(BaseModel):
    title: str
    body: str


class SubTaskUpdate(BaseModel):
    title: str | None = None
    body: str | None = None
    completed: bool | None = None
