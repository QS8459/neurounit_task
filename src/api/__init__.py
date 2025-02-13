from src.api.v1 import v1
from fastapi import APIRouter

api = APIRouter(prefix="/api")

api.include_router(v1)