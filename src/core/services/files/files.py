from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.services.base import BaseService
from src.db.engine import get_async_session
from src.db.models.file.file import File

from sqlalchemy.future import select


class FileService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(session, File)

    async def get_by_name(self, name):
        async def _get_by_name(_name):
            query = select(self.model).where(self.model.title == _name)
            return await self.session.execute(query)
        instance = await self._exec_in_session(_get_by_name, _name = name)

        if not instance:
            return None
        return instance


def get_file_service(session=Depends(get_async_session)) -> FileService:
    return FileService(session)
