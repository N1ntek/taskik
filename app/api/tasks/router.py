from fastapi import APIRouter
from starlette import status

from app.api.auth.dependencies import CurrentUser
from app.core.database import SessionDep

from app.api.tasks import crud
from app.api.tasks.dependencies import TaskByIdDep
from app.api.tasks.schemas import (
    Task,
    SubTask,
    TaskCreate,
    TaskUpdate,
    TaskWithSubtasks,
)


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/",
    response_model=list[Task],
)
async def get_tasks(
    session: SessionDep,
    current_user: CurrentUser,
):
    """
    Get all task
    """
    return await crud.get_tasks(session, current_user)


@router.post(
    "/",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    session: SessionDep,
    current_user: CurrentUser,
    task_in: TaskCreate,
):
    """
    Create a new task
    """
    return await crud.create_task(session, current_user, task_in)


@router.post(
    "/{task_id}/subtask/",
    response_model=SubTask,
    status_code=status.HTTP_201_CREATED,
)
async def create_subtask(
    session: SessionDep,
    parent_task: TaskByIdDep,
    subtask_in: TaskCreate,
):
    """
    Crete a subtask
    """
    current_user = parent_task.user
    return await crud.create_task(
        session,
        current_user,
        subtask_in,
        parent_task,
    )


@router.get(
    "/{task_id}",
    response_model=TaskWithSubtasks,
)
async def get_task(task: TaskByIdDep):
    """
    Get a task by id
    """
    return task


@router.patch(
    "/{task_id}",
    response_model=Task,
)
async def update_task(
    session: SessionDep,
    task_update: TaskUpdate,
    task: TaskByIdDep,
):
    """
    Update a task
    """
    return await crud.update_task(session, task, task_update)


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_task(
    session: SessionDep,
    task: TaskByIdDep,
) -> None:
    """
    Delete a task
    """
    return await crud.delete_task(session, task)


@router.get(
    "/{task_id}/subtasks",
    response_model=list[Task],
)
async def get_subtasks(task: TaskByIdDep):
    """
    Get all subtasks of a task
    """
    return await crud.get_subtasks(task)
