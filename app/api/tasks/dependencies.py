from typing import Annotated
from uuid import UUID

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.tasks import crud
from app.core.models import Task
from app.core.database import db


async def task_by_id(
    task_id: Annotated[UUID, Path],
    session: AsyncSession = Depends(db.session_dependency),
) -> Task:
    task = await crud.get_task_by_id(session, task_id)
    if task:
        return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found",
    )
