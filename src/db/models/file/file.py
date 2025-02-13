from src.db.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class File(Base):
    __tablename__ = "file"
    __table_arg__ = {"schema": "public"}

    title: Mapped[String] = mapped_column(String(250), nullable=False)
    path: Mapped[String] = mapped_column(String(350), nullable=False)
