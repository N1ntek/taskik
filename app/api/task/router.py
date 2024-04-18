from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import db
from . import crud
from .dependencies import task_by_id
from .schemas import Task, TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=list[Task])
async def get_tasks(
        session: AsyncSession = Depends(db.session_dependency),
):
    """
    Get all tasks ordered by id
    """
    return await crud.get_tasks(session)


@router.post("/create", response_model=Task)
async def create_task(
        task: TaskCreate,
        session: AsyncSession = Depends(db.session_dependency),
):
    """
    Create a new task
    """
    return await crud.create_task(session, task)


@router.get("/{task_id}", response_model=Task)
async def get_task_by_id(
        task: Task = Depends(task_by_id),
):
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
