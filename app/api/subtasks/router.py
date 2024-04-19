from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import db

router = APIRouter(prefix="/tasks/{task_id}/subtasks", tags=["subtasks"])


@router.get("/")
async def get_subtasks(
    task_id: int, session: AsyncSession = Depends(db.session_dependency)
): ...


@router.post("/")
async def create_subtask(
    task_id: int,
    session: AsyncSession = Depends(db.session_dependency),
): ...


@router.get("/{subtask_id}")
async def get_subtask(
    task_id: int,
    subtask_id: int,
    session: AsyncSession = Depends(db.session_dependency),
): ...


@router.patch("/{subtask_id}")
async def update_subtask(
    task_id: int,
    subtask_id: int,
    session: AsyncSession = Depends(db.session_dependency),
): ...


@router.delete("/{subtask_id}")
async def delete_subtask(
    task_id: int,
    subtask_id: int,
    session: AsyncSession = Depends(db.session_dependency),
): ...
