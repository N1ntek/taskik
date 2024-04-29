from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import db
from app.api.subtasks import crud

from app.api.subtasks.schemas import SubTask, SubTaskCreate, SubTaskUpdate

router = APIRouter(prefix="/subtasks/{subtask_id}", tags=["subtasks"])


@router.get("/")
async def get_subtask(
    subtask_id: int,
    session: AsyncSession = Depends(db.session_dependency),
):
    return await crud.get_subtask(session, subtask_id)


@router.patch("/")
async def update_subtask(
    subtask_id: int,
    subtask_in: SubTaskUpdate,
    session: AsyncSession = Depends(db.session_dependency),
):
    return await crud.update_subtask(subtask_id, subtask_in, session=session)


@router.delete("/")
async def delete_subtask(
    subtask_id: int,
    session: AsyncSession = Depends(db.session_dependency),
): ...
