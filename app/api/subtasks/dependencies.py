from typing import Annotated
from uuid import UUID

from fastapi import Path, HTTPException, status, Depends

from app.api.auth.dependencies import CurrentUser
from app.api.subtasks import crud
from app.core.models import SubTask
from app.core.database import SessionDep


async def subtask_by_id(
    session: SessionDep,
    current_user: CurrentUser,
    subtask_id: Annotated[UUID, Path],
) -> SubTask:
    subtask = await crud.get_subtask(
        session,
        current_user=current_user,
        subtask_id=subtask_id,
    )
    if subtask:
        return subtask

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Subtask {subtask_id} not found",
    )


SubtaskByIdDep = Annotated[SubTask, Depends(subtask_by_id)]
