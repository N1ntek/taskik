from datetime import datetime, UTC
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.base import Base

if TYPE_CHECKING:
    from app.core.models import User


class Task(Base):
    id: Mapped[UUID] = mapped_column(
        primary_key=True, server_default=text("gen_random_uuid()")
    )
    title: Mapped[str]
    body: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(UTC).replace(tzinfo=None)
    )
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="tasks")

    parent_id: Mapped[UUID] = mapped_column(ForeignKey("tasks.id"), nullable=True)

    parent_task: Mapped["Task"] = relationship(
        remote_side=id, back_populates="subtasks"
    )

    subtasks: Mapped[list["Task"]] = relationship(
        back_populates="parent_task", cascade="all, delete-orphan"
    )
