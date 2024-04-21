from sqlalchemy.ext.asyncio import AsyncSession

from app.api.task.models import Task


async def create_subtask(session: AsyncSession, task_id: int, subtask_in: SubTaskCreate) -> Task:
    ...