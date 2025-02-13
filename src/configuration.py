from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine, async_sessionmaker
from src.settings import settings


engine: AsyncEngine = create_async_engine(str(settings.PG_URI))
async_session_maker: async_sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
