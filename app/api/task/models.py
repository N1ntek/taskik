from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base import Base


class Task(Base):
    title: Mapped[str] = mapped_column(String(20))
    body: Mapped[str] = mapped_column(String(150))
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
