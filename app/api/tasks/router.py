from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.core.database import db

from app.api.tasks import crud
from app.api.tasks.dependencies import task_by_id
from app.api.tasks.schemas import Task, TaskCreate, TaskUpdate

from app.api.subtasks.schemas import SubTask, SubTaskCreate


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=list[Task])
async def get_tasks(session: AsyncSession = Depends(db.session_dependency)):
    """
    Get all task
    """
    return await crud.get_tasks(session)


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(
    task: TaskCreate,
    session: AsyncSession = Depends(db.session_dependency),
):
    """
    Create a new task
    """
    return await crud.create_task(session, task)


@router.get("/{task_id}", response_model=Task)
async def get_task(task: Task = Depends(task_by_id)):
    """
    Get a task by id
    """
    return task


@router.patch("/{task_id}", response_model=Task)
async def update_task(
    task_update: TaskUpdate,
    task: Task = Depends(task_by_id),
    session: AsyncSession = Depends(db.session_dependency),
):
    """
    Update a task
    """
    return await crud.update_task(session, task, task_update)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task: Task = Depends(task_by_id),
    session: AsyncSession = Depends(db.session_dependency),
) -> None:
    """
    Delete a task
    """
    return await crud.delete_task(session, task)


@router.get("/{task_id}/subtasks", response_model=list[SubTask])
async def get_subtasks(task: Task = Depends(task_by_id)):
    """
    Get all subtasks of a task
    """
    return await crud.get_subtasks(task)


@router.post("/{task_id}/subtasks/", response_model=SubTask, status_code=status.HTTP_201_CREATED)
async def create_subtask(
    subtask_in: SubTaskCreate,
    task: Task = Depends(task_by_id),
    session: AsyncSession = Depends(db.session_dependency),
):
    """
    Crete a subtask
    """
    return await crud.create_subtask(session, task, subtask_in)
