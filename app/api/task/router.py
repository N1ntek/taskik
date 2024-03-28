from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from . import crud
from .schemas import Task, TaskCreate
from app.core.database import db

router = APIRouter(prefix="/tasks", tags=["task"])


@router.get("/", response_model=list[Task])
async def get_tasks(
    session: AsyncSession = Depends(db.session_dependency),
):
    """
    Get all tasks ordered by id
    """
    return await crud.get_tasks(session)


@router.post("/task", response_model=Task)
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
    task_id: int,
    session: AsyncSession = Depends(db.session_dependency),
):
    """
    Get a task by id
    """
    task = crud.get_task_by_id(session, task_id)
    if task:
        return await task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task {task_id} not found",
    )
