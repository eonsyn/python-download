import yt_dlp
import os
import uuid

DOWNLOADS_DIR = "downloads/"

# Ensure the downloads directory exists
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

def download_video(youtube_url: str) -> str:
    """Downloads a YouTube video and returns the file path."""
    unique_id = str(uuid.uuid4())  # Generate a unique filename
    output_path = os.path.join(DOWNLOADS_DIR, f"{unique_id}.mp4")

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": output_path,
        "merge_output_format": "mp4"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    return output_path
