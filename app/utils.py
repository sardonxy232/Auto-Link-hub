import os
from fastapi import UploadFile
from uuid import uuid4

MEDIA_DIR = "media"
os.makedirs(MEDIA_DIR, exist_ok=True)  # ensure directory exists

def save_upload_file(upload_file: UploadFile) -> str:
    """Save uploaded file safely and return its relative path"""
    ext = upload_file.filename.split(".")[-1]
    unique_name = f"{uuid4()}.{ext}"
    file_path = os.path.join(MEDIA_DIR, unique_name)

    with open(file_path, "wb") as buffer:
        while chunk := upload_file.file.read(1024 * 1024):  # write in chunks
            buffer.write(chunk)

    return f"/{MEDIA_DIR}/{unique_name}"  # return relative URL path
