from fastapi import APIRouter, HTTPException, status
from src.models.users import User, UserSignIn


user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# 타입 힌팅 추가
users: dict[str, User] = {}


@user_router.post(
    "/signup", 
    response_model=dict[str, str],
    status_code=status.HTTP_201_CREATED,
    summary="새로운 사용자 등록",
    response_description="사용자 등록 성공 메시지"
)
async def sign_new_user(user: User) -> dict[str, str]:
    if user.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email already exists"
        )
    users[user.email] = user
    return {
        "message": "User successfully registered!"
    }


@user_router.post(
    "/signin",
    response_model=dict[str, str],
    status_code=status.HTTP_200_OK,
    summary="사용자 로그인",
    response_description="로그인 성공 메시지"
)
async def sign_user_in(credentials: UserSignIn) -> dict[str, str]:
    if credentials.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    stored_user = users[credentials.email]
    if stored_user.password != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials"
        )
    
    return {
        "message": "User signed in successfully"
    }