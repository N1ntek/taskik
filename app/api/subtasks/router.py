from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import db

router = APIRouter(prefix="/subtasks/{subtask_id}", tags=["subtasks"])


@router.get("/")
async def get_subtask(
    subtask_id: int,
    session: AsyncSession = Depends(db.session_dependency),
): ...


@router.patch("/")
async def update_subtask(
    subtask_id: int,
    session: AsyncSession = Depends(db.session_dependency),
): ...


@router.delete("/")
async def delete_subtask(
    subtask_id: int,
    session: AsyncSession = Depends(db.session_dependency),
): ...
