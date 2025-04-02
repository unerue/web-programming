import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.database.connection import Settings
from src.routes.events import event_router
from src.routes.users import user_router

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작 시 데이터베이스 초기화
    await settings.initialize_database()
    yield
    # 종료 시 정리 작업 (필요한 경우)

app = FastAPI(
    title="Event Planner API",
    description="FastAPI를 이용한 이벤트 플래너 API",
    version="1.0.0",
    lifespan=lifespan
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우트 등록
app.include_router(user_router)
app.include_router(event_router)

@app.get("/", response_class=RedirectResponse, status_code=308)
async def home() -> RedirectResponse:
    return RedirectResponse(url="/events/")

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
