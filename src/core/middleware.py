from src.core.logger import logger

from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException


async def logger_mddle(request: Request, call_next):
    try:
        logger.info("Middleware was triggered")
        response = await call_next(request)
    except HTTPException as e:
        logger.error("Exception has happened in logger MIDDLEWARE")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail":"Something went wrong"}
        )
    return response
