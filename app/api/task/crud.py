from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.api.task.models import Task
from app.api.task.schemas import TaskCreate, TaskUpdate


async def get_tasks(session: AsyncSession) -> list[Task]:
    stmt = select(Task).order_by(Task.id)
    result: Result = await session.execute(stmt)
    tasks = result.scalars().all()
    return list(tasks)


async def get_task_by_id(session: AsyncSession, task_id: int) -> Task | None:
    return await session.get(Task, task_id)


async def create_task(session: AsyncSession, task_in: TaskCreate) -> Task | None:
    task = Task(**task_in.model_dump())
    session.add(task)
    await session.commit()

    return task


async def update_task(
    session: AsyncSession, task: Task, task_update: TaskUpdate
) -> Task | None:
    for key, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    await session.commit()
    return task


async def delete_task(session: AsyncSession, task: Task) -> None:
    await session.delete(task)
    await session.commit()
