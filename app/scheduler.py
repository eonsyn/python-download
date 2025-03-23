from apscheduler.schedulers.background import BackgroundScheduler
import cloudinary.api

scheduler = BackgroundScheduler()
scheduler.start()

def schedule_deletion(public_id: str):
    """Schedules Cloudinary file deletion after 30 minutes."""
    scheduler.add_job(delete_cloudinary_file, "date", run_date=datetime.utcnow() + timedelta(minutes=30), args=[public_id])

def delete_cloudinary_file(public_id: str):
    """Deletes a file from Cloudinary."""
    try:
        cloudinary.api.delete_resources([public_id], resource_type="video")
        print(f"Deleted {public_id} from Cloudinary.")
    except Exception as e:
        print(f"Error deleting {public_id}: {e}")
