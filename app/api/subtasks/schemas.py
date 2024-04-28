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
