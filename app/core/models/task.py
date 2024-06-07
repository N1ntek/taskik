from datetime import datetime, UTC
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.base import Base

if TYPE_CHECKING:
    from app.core.models import SubTask


class Task(Base):
    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=text("gen_random_uuid()"))
    title: Mapped[str]
    body: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC).replace(tzinfo=None))
    subtasks: Mapped[list["SubTask"]] = relationship(back_populates="task", cascade="all, delete")
