from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base import Base


class Task(Base):
    title: Mapped[str] = mapped_column(String(20))
    body: Mapped[str] = mapped_column(String(150))
