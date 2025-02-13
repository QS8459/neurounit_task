from pydantic import BaseModel
from uuid import UUID


class BaseFileSchema(BaseModel):
    id: UUID
    title: str
    path: str
