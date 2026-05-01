import cloudinary
import cloudinary.uploader 

from app.config.config import settings
from fastapi import UploadFile

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET
)

# reusable upload function
async def upload_image(file: UploadFile, folder: str = "vendors"):
    
    result = cloudinary.uploader.upload(
        file.file,   # ✅ THIS IS IMPORTANT
        folder=folder,
        resource_type="image"
    )

    return result["secure_url"]