from fastapi import APIRouter

from .task.router import router as task_router
from .subtasks.router import router as subtasks_router

router = APIRouter(prefix="/api")
router.include_router(task_router)
router.include_router(subtasks_router)
