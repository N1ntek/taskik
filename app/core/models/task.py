from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.base import Base

if TYPE_CHECKING:
    from app.core.models import SubTask


class Task(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    body: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    subtasks: Mapped[list["SubTask"]] = relationship(back_populates="task")
