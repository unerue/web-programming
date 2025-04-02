from fastapi import APIRouter, HTTPException, status
from src.database.connection import Database
from src.models.users import User, UserSignIn


user_router = APIRouter(prefix="/users", tags=["Users"])
user_database = Database(User)


@user_router.post(
    "/signup",
    response_model=dict[str, str],
    status_code=status.HTTP_201_CREATED,
    summary="새로운 사용자 등록",
    response_description="사용자 등록 성공 메시지"
)
async def sign_user_up(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)

    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already."
        )
    await user_database.save(user)
    return {
        "message": "User created successfully"
    }


@user_router.post(
    "/signin",
    response_model=dict[str, str],
    status_code=status.HTTP_200_OK,
    summary="사용자 로그인",
    response_description="로그인 성공 메시지"
)
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist."
        )
    if user_exist.password == user.password:
        return {
            "message": "User signed in successfully."
        }

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed."
    )
