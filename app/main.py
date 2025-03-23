from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.downloader import download_video
from app.uploader import upload_to_cloudinary
from app.scheduler import schedule_deletion
import os

app = FastAPI()

# Define a Pydantic model for request body validation
class VideoRequest(BaseModel):
    youtube_url: str

@app.get("/")
def home():
    return {"message": "Welcome to YouTube Video Downloader API!"}

@app.post("/download/")
def download_and_upload(video: VideoRequest):
    try:
        # Step 1: Download video
        video_path = download_video(video.youtube_url)

        # Step 2: Upload to Cloudinary
        cloudinary_url, public_id = upload_to_cloudinary(video_path)

        # Step 3: Schedule deletion after 30 minutes
        schedule_deletion(public_id)

        # Step 4: Remove local file
        os.remove(video_path)

        return {"video_url": cloudinary_url, "message": "Video uploaded successfully. It will be deleted after 30 minutes."}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
