from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import db
from app.api.subtasks import crud

from app.api.subtasks.schemas import SubTask, SubTaskCreate, SubTaskUpdate
from app.api.subtasks.dependencies import subtask_by_id

router = APIRouter(prefix="/subtasks/{subtask_id}", tags=["subtasks"])


@router.get("/", response_model=SubTask)
async def get_subtask(subtask: SubTask = Depends(subtask_by_id)):
    return subtask


@router.patch("/", response_model=SubTask)
async def update_subtask(
    subtask_update: SubTaskUpdate,
    subtask: SubTask = Depends(subtask_by_id),
    session: AsyncSession = Depends(db.session_dependency),
):
    return await crud.update_subtask(session, subtask, subtask_update)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_subtask(
    subtask: SubTask = Depends(subtask_by_id),
    session: AsyncSession = Depends(db.session_dependency),
) -> None:
    await crud.delete_subtask(session, subtask)
