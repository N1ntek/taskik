from fastapi import APIRouter, status

from app.core.database import SessionDep
from app.api.subtasks import crud

from app.api.subtasks.schemas import SubTask, SubTaskUpdate
from app.api.subtasks.dependencies import SubtaskByIdDep

router = APIRouter(prefix="/subtasks/{subtask_id}", tags=["subtasks"])


@router.get("/", response_model=SubTask)
async def get_subtask(subtask: SubtaskByIdDep):
    return subtask


@router.patch("/", response_model=SubTask)
async def update_subtask(
    session: SessionDep,
    subtask: SubtaskByIdDep,
    subtask_update: SubTaskUpdate,
):
    return await crud.update_subtask(session, subtask, subtask_update)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_subtask(
    session: SessionDep,
    subtask: SubtaskByIdDep,
) -> None:
    await crud.delete_subtask(session, subtask)
