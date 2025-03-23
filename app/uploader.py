import cloudinary.uploader
import os

def upload_to_cloudinary(file_path: str) -> str:
    """Uploads a video to Cloudinary and returns the public URL."""
    response = cloudinary.uploader.upload_large(
        file_path,
        resource_type="video",
        folder="youtube_videos/",
        timeout=600  # Set a timeout to prevent long uploads
    )
    return response.get("secure_url"), response.get("public_id")
