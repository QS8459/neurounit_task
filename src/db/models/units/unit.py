from src.db.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, String, DECIMAL, TIMESTAMP
from datetime import datetime


class Units(Base):

    __tablename__ = "units"
    __table_arg__ = {"schema": "public"}

    date: Mapped[datetime] = mapped_column(TIMESTAMP,default=datetime.utcnow())
    xml_id: Mapped[INTEGER] = mapped_column(INTEGER)
    name: Mapped[String] = mapped_column(String(100))
    quantity: Mapped[INTEGER] = mapped_column(INTEGER, default=0)
    price: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2), default=0.0)
    category: Mapped[String] = mapped_column(String(100))


__all__ = ("units")
