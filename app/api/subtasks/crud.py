from sqlalchemy.ext.asyncio import AsyncSession

from app.api.subtasks.models import SubTask


async def get_subtask(session: AsyncSession, subtask_id: int) -> SubTask: ...


async def update_subtask(session: AsyncSession, subtask_id: int) -> SubTask: ...


async def delete_subtask(session: AsyncSession, subtask_id: int) -> None: ...
