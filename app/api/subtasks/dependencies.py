from typing import Annotated

from fastapi import Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.subtasks import crud
from app.api.subtasks.models import SubTask
from app.core.database import db


async def subtask_by_id(
    subtask_id: Annotated[int, Path],
    session: AsyncSession = Depends(db.session_dependency),
) -> SubTask:
    await crud.get_subtask(session, subtask_id)


    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found",
    )

