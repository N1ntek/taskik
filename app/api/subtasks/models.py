from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base import Base


class SubTask(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    body: Mapped[str]
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
