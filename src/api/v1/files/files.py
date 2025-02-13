from fastapi import APIRouter, Depends, UploadFile
from fastapi.responses import FileResponse
from src.api.v1.files.utils import save_file
from src.core.schema.file.file import BaseFileSchema
from src.core.services.files.files import get_file_service
file_api = APIRouter(prefix='/file', tags=['files'])


@file_api.post("/upload/", response_model=BaseFileSchema)
async def upload_file(file: UploadFile, file_service=Depends(get_file_service)):
    save_file(file)
    result = await file_service.add(title=file.filename, path=f'/app/uploaded/{file.filename}')
    return result


@file_api.post('/download/')
async def download_file(file_name: str, file_service=Depends(get_file_service)):
    result = await file_service.get_by_name(file_name)
    return FileResponse(result.path, media_type='application/octet-stream', filename=result.title)
