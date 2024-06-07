from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.api.subtasks.schemas import SubTaskCreate
from app.api.tasks.schemas import TaskCreate, TaskUpdate
from app.core.models import Task
from app.core.models import SubTask


async def get_tasks(session: AsyncSession) -> list[Task]:
    stmt = select(Task).order_by(Task.id)
    result = await session.execute(stmt)
    tasks = result.scalars().all()
    return list(tasks)


async def get_task_by_id(session: AsyncSession, task_id: UUID) -> Task | None:
    stmt = select(Task).options(selectinload(Task.subtasks)).where(Task.id == task_id)
    result = await session.execute(stmt)
    task = result.scalar_one_or_none()
    return task


async def create_task(session: AsyncSession, task_in: TaskCreate) -> Task | None:
    task = Task(**task_in.model_dump())
    session.add(task)
    await session.commit()
    return task


async def update_task(
    session: AsyncSession,
    task: Task,
    task_update: TaskUpdate,
) -> Task | None:
    for key, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    await session.commit()
    return task


async def delete_task(session: AsyncSession, task: Task) -> None:
    await session.delete(task)
    await session.commit()


async def get_subtasks(task: Task) -> list[SubTask]:
    return task.subtasks


async def create_subtask(
    session: AsyncSession, task: Task, subtask_in: SubTaskCreate
) -> SubTask:
    subtask = SubTask(**subtask_in.model_dump(), task=task)
    session.add(subtask)
    await session.commit()
    return subtask
