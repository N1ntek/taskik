from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api.task.models import Task
from app.core.models.base import Base


class SubTask(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    body: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    task_id: Mapped[int] = mapped_column(ForeignKey('tasks.id'))
    task: Mapped[Task] = relationship(back_populates='subtasks')
