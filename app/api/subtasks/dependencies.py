from typing import Annotated
from uuid import UUID

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.subtasks import crud
from app.core.models import SubTask
from app.core.database import db


async def subtask_by_id(
    subtask_id: Annotated[UUID, Path],
    session: AsyncSession = Depends(db.session_dependency),
) -> SubTask:
    subtask = await crud.get_subtask(session, subtask_id)

    if subtask:
        return subtask

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Subtask {subtask_id} not found",
    )
