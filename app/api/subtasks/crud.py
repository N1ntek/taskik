from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.users.schemas import User
from app.core.models import SubTask
from app.api.subtasks.schemas import SubTaskUpdate


async def get_subtask(
    session: AsyncSession,
    current_user: User,
    subtask_id: UUID,
) -> SubTask | None:
    """
    Get a subtask by id
    """
    stmt = select(SubTask).where(
        (SubTask.user_id == current_user.id) & (SubTask.id == subtask_id)
    )
    result = await session.execute(stmt)
    subtask = result.scalar_one_or_none()
    return subtask


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
