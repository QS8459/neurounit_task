from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.services.base import BaseService
from src.db.models.units.unit import Units
from src.db.engine import get_async_session


class UnitService(BaseService):

    def __init__(self, session: AsyncSession):
        super().__init__(session, Units)


def unit_service(session=Depends(get_async_session)) -> UnitService:
    return UnitService(session)
