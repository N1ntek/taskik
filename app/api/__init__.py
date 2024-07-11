from fastapi import APIRouter

from app.api.tasks.router import router as task_router


from app.api.users.router import router as users_router
from app.api.auth.router import router as auth_router

router = APIRouter(prefix="/api")
router.include_router(task_router)
router.include_router(users_router)
router.include_router(auth_router)
