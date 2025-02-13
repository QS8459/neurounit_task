from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import UUID4
from datetime import datetime
from uuid import uuid4


class Base(DeclarativeBase):

    id: Mapped[UUID4]=mapped_column(default=uuid4, primary_key=True)
    created_at: Mapped[datetime]=mapped_column(default=datetime.utcnow())

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id})"