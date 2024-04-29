from sqlalchemy.ext.asyncio import AsyncSession

from app.api.subtasks.models import SubTask


async def get_subtask(session: AsyncSession, subtask_id: int) -> SubTask | None:
    """
    Get a subtask by id
    """
    return await session.get(SubTask, subtask_id)


async def update_subtask(session: AsyncSession, subtask_id: int, subtask_in) -> SubTask: ...


async def delete_subtask(session: AsyncSession, subtask_id: int) -> None: ...
