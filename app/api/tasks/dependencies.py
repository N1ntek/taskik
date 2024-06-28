from typing import Annotated
from uuid import UUID

from fastapi import Path, HTTPException, status, Depends

from app.api.auth.dependencies import CurrentUser
from app.api.tasks import crud
from app.core.models import Task
from app.core.database import SessionDep


async def task_by_id(
    session: SessionDep,
    current_user: CurrentUser,
    task_id: Annotated[UUID, Path],
) -> Task:
    task = await crud.get_task_by_id(
        session,
        current_user=current_user,
        task_id=task_id,
    )
    if task:
        return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found",
    )


TaskByIdDep = Annotated[Task, Depends(task_by_id)]
