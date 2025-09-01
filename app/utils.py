import os
from fastapi import UploadFile
from uuid import uuid4

MEDIA_DIR = "media"

def save_upload_file(upload_file: UploadFile) -> str:
    """Save uploaded file and return its relative path"""
    ext = upload_file.filename.split(".")[-1]
    unique_name = f"{uuid4()}.{ext}"
    file_path = os.path.join(MEDIA_DIR, unique_name)

    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())

    return file_path
