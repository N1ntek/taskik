from datetime import datetime, UTC
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.base import Base


if TYPE_CHECKING:
    from app.core.models import Task


class SubTask(Base):
    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=text("gen_random_uuid()"))
    title: Mapped[str]
    body: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now(UTC).replace(tzinfo=None))
    task_id: Mapped[UUID] = mapped_column(ForeignKey("tasks.id", ondelete="CASCADE"))  # проверить это
    task: Mapped["Task"] = relationship(back_populates="subtasks")
