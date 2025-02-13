from fastapi import UploadFile
from src.core.logger import logger
import shutil


def save_file(file: UploadFile):
    try:
        with open(f'/app/uploaded/{file.filename}', 'wb') as f_writer:
            shutil.copyfileobj(file.file, f_writer)

    except (shutil.Error, shutil.ExecError) as e:
        logger.error("Having issue with saving file")

