from celery import Celery
from src.settings import settings


celery_app = Celery(
    "worker",
    broker= settings.CELERY_BROKER_URL,
)


celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    task_ignore_result=True,
    timezone="UTC",
    enable_utc=True
)

celery_app.conf.beat_schedule = {
    "run-every-10-seconds": {
        "task": "worker.tasks.scheduled_task",
        "schedule": 10.0,
        "args": (),
    }
}