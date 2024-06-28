from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.api.subtasks.schemas import SubTask


class Task(BaseModel):
    id: UUID
    title: str
    body: str
    completed: bool
    created_at: datetime
    user_id: UUID


class TaskWithSubtasks(Task):
    subtasks: list[SubTask] = []


class TaskCreate(BaseModel):
    title: str
    body: str


class TaskUpdate(BaseModel):
    title: str | None = None
    body: str | None = None
    completed: bool | None = None
