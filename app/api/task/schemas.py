from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    body: str


class Task(TaskBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class TaskCreate(TaskBase):
    pass
