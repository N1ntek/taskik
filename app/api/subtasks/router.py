from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import db
from app.api.subtasks import crud

from app.api.subtasks.schemas import SubTask, SubTaskCreate, SubTaskUpdate
from app.api.subtasks.dependencies import subtask_by_id

router = APIRouter(prefix="/subtasks/{subtask_id}", tags=["subtasks"])


@router.get("/", response_model=SubTask)
async def get_subtask(subtask: SubTask = Depends(subtask_by_id)):
    return subtask


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
