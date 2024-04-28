from datetime import datetime

from pydantic import BaseModel

from app.api.subtasks.schemas import SubTask


class Task(BaseModel):
    id: int
    title: str
    body: str
    completed: bool
    created_at: datetime


class TaskWithSubtasks(Task):
    subtasks: list[SubTask] = []


class TaskCreate(BaseModel):
    title: str
    body: str


class TaskUpdate(BaseModel):
    title: str | None = None
    body: str | None = None
    completed: bool | None = None
