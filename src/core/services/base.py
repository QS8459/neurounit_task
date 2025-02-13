from typing import Generic, TypeVar, Type
from abc import ABC
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from src.core.logger import logger

T = TypeVar('T')


class BaseService(ABC, Generic[T]):
    def __init__(self, session: AsyncSession, model: Type[T] = None):
        self.session = session
        self.model = model

    async def __handle_session(self, call_back, refresh=True, *args, **kwargs):
        try:
            result = await call_back(*args, **kwargs)
            await self.session.commit()
            if refresh:
                await self.session.refresh(result)
            return result
        except SQLAlchemyError as e:
            logger.error(f'SQLAlchemyError {e}')
            raise
        except IntegrityError as e:
            logger.error(f"IntegrityError {e}")

    async def _exec_in_session(self, call_back, refresh=False, fetch_one =True, *args, **kwargs):
        if refresh:
            return await self.__handle_session(call_back, *args, **kwargs)
        else:
            result = await self.__handle_session(call_back, refresh=False, *args, **kwargs)

            if fetch_one:
                return result.scalars().first()
            else:
                return result.scalars().all()

    async def add(self, *args, **kwargs):
        async def _add(*in_args, **in_kwargs):
            instance = self.model(**in_kwargs)
            self.session.add(instance)
            return instance
        result = await self._exec_in_session(_add, refresh=True, *args, **kwargs)
        return result

