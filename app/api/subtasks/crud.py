from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import SubTask
from app.api.subtasks.schemas import SubTaskUpdate


async def get_subtask(
    session: AsyncSession,
    subtask_id: UUID,
) -> SubTask | None:
    """
    Get a subtask by id
    """
    return await session.get(SubTask, subtask_id)


async def update_subtask(
    session: AsyncSession,
    subtask: SubTask,
    subtask_update: SubTaskUpdate,
) -> SubTask:
    """
    Update a subtask
    """
    for key, value in subtask_update.model_dump(exclude_unset=True).items():
        setattr(subtask, key, value)
    await session.commit()
    return subtask


async def delete_subtask(
    session: AsyncSession,
    subtask: SubTask,
) -> None:
    """
    Delete a subtask
    """
    await session.delete(subtask)
    await session.commit()
