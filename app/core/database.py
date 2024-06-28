from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from app.core.config import settings


class Database:
    def __init__(
        self,
        url: str,
        echo: bool,
        echo_pool: bool = False,
        pool_size: int = 5,
        max_overflow: int = 10,
    ):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session
            await session.close()


db = Database(
    url=str(settings.db.url),
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)

SessionDep = Annotated[AsyncSession, Depends(db.session_dependency)]
