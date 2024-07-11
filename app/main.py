import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api import router as api_router

app = FastAPI()
app.include_router(api_router)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs", status_code=307)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
