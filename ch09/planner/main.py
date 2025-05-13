from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from database.connection import Settings
from routes.users import user_router
from routes.events import event_router

import uvicorn

app = FastAPI()

settings = Settings()


# 출처 등록

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")
# 라우트 등록

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
async def init_db():
    await settings.initialize_database()


# @app.get("/")
# async def home():
#     return RedirectResponse(url="/event/")


@app.get("/", response_class=HTMLResponse)  # 응답 클래스를 HTMLResponse로 변경
async def home(request: Request):  # request 파라미터 추가
    # /event/ 라우트에서 모든 이벤트를 가져옵니다.
    # 실제 클라이언트에서는 JavaScript로 API를 호출하여 데이터를 가져오는 것이 일반적이지만,
    # 여기서는 초기 페이지 로드 시 서버에서 데이터를 전달하는 간단한 예시를 보여줍니다.
    # 좀 더 동적인 페이지를 원하시면 JavaScript fetch API를 사용해야 합니다.
    return templates.TemplateResponse("planner_view.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
