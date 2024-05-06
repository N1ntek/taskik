from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api import router as api_router


app = FastAPI()
app.include_router(api_router)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs", status_code=307)
