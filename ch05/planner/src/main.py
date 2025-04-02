from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from src.routes.users import user_router
from src.routes.events import event_router

import uvicorn
from typing import Annotated


app = FastAPI(
    title="Event Planner API",
    description="FastAPI를 이용한 이벤트 플래너 API",
    version="1.0.0",
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
root_router = APIRouter()
app.include_router(root_router)
app.include_router(user_router)
app.include_router(event_router)


@root_router.get("/", response_class=RedirectResponse, status_code=308)
async def home() -> RedirectResponse:
    return RedirectResponse(url="/events/")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        workers=1,
        log_level="info"
    )