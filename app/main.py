from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import db
from app.core.models.base import Base

from app.api import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
