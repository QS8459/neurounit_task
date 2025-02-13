from src.core.celery_config import celery_app
from src.core.logger import logger

@celery_app.task
def process_task(data=None):
    from time import sleep
    sleep(10)
    logger.info("Message from process_task Celery")
    return 0

@celery_app.task
def scheduled_task():
    logger.info("Scheduled task that runs every 10 seconds")