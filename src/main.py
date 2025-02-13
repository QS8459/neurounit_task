from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.worker.tasks import process_task
from src.core.middleware import logger_mddle
from src.api import api

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.configuration import engine

    "In this lifespan function we will initiate db connection"
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.on_event('startup')
async def add_middleware():
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[],
        allow_methods=["*"],
        allow_headers=["*"]
    )
app.middleware("http")(logger_mddle)

@app.get('/', status_code = 200)
async def home(data:str, bg_tasks: BackgroundTasks):
    bg_tasks.add_task(process_task,data)
    return JSONResponse(
        content={"detail": "Welcome to FastAPI"},
        status_code=200

    )

app.include_router(api)
