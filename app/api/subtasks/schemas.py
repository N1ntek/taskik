from uuid import UUID

from pydantic import BaseModel
from datetime import datetime


class SubTask(BaseModel):
    id: UUID
    title: str
    body: str
    completed: bool
    created_at: datetime
    user_id: UUID
    task_id: UUID


class SubTaskCreate(BaseModel):
    title: str
    body: str


class SubTaskUpdate(BaseModel):
    title: str | None = None
    body: str | None = None
    completed: bool | None = None
