from src.api.v1.files.files import file_api
from fastapi import APIRouter

v1 = APIRouter(prefix="/v1")

v1.include_router(file_api)