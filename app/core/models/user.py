from datetime import datetime, UTC
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import String, text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.core.models import Base

if TYPE_CHECKING:
    from app.core.models import Task


class User(Base):
    id: Mapped[UUID] = mapped_column(
        primary_key=True, server_default=text("gen_random_uuid()")
    )
    username: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    hashed_password: Mapped[bytes] = mapped_column(nullable=False)
    active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(UTC).replace(tzinfo=None)
    )
    tasks: Mapped[list["Task"]] = relationship(
        back_populates="user", cascade="all, delete"
    )
