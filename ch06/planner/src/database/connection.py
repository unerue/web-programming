from typing import Any, List, Optional

from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import ConfigDict, BaseModel
from pydantic_settings import BaseSettings

# 모델들을 먼저 import
from src.models.events import Event
from src.models.users import User

# 모델 리스트 정의
document_models = [Event, User]

class Settings(BaseSettings):
    DATABASE_URL: str | None = None

    async def initialize_database(self):
        if not self.DATABASE_URL:
            raise ValueError("데이터베이스 URL이 설정되지 않았습니다. .env 파일을 확인해주세요.")

        try:
            client = AsyncIOMotorClient(self.DATABASE_URL)
            await init_beanie(
                database=client.get_default_database(),
                document_models=[Event, User]
            )
            print("데이터베이스 연결 성공!")
        except Exception as e:
            print(f"데이터베이스 연결 실패: {str(e)}")
            print("MongoDB 서버가 실행 중인지 확인해주세요.")
            raise

    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=False
    )


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> list[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()

        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
