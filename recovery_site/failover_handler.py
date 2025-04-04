import os
import logging
import boto3

# Define the recovery log directory
RECOVERY_REPORTS_FOLDER = r"E:\Saved Games\disaster-recovery-system\reports\recovery_reports"

# Ensure the recovery log directory exists
os.makedirs(RECOVERY_REPORTS_FOLDER, exist_ok=True)

# Define the log file path
recovery_log_path = os.path.join(RECOVERY_REPORTS_FOLDER, "failover.log")

# Setup logging
logging.basicConfig(
    filename=recovery_log_path,  # Save logs in recovery_reports/failover.log
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# AWS S3 Configuration
AWS_ACCESS_KEY_ID = "AKIAU6GD24HFHAA2LME5"
AWS_SECRET_ACCESS_KEY = "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"
AWS_REGION = "ap-south-1"
BUCKET_NAME = "itm-disaster"
OBJECT_KEY = "local_backup.zip"
LOCAL_BACKUP_PATH = "local_backup.zip"

def check_local_backup():
    """Check if local backup exists."""
    return os.path.exists(LOCAL_BACKUP_PATH)

def download_from_s3():
    """Download the backup from S3."""
    logging.info("Attempting to fetch backup from S3...")

    try:
        session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )
        s3 = session.client("s3")
        
        s3.download_file(BUCKET_NAME, OBJECT_KEY, LOCAL_BACKUP_PATH)
        logging.info("✅ Backup downloaded successfully from S3!")
        return True

    except Exception as e:
        logging.error(f"❌ Failed to fetch backup from S3: {e}")
        return False

def initiate_failover():
    """Initiate the failover process."""
    logging.warning("🚨 Primary system failure detected! Initiating failover...")

    if check_local_backup():
        logging.info("✅ Local backup found. Failover successful!")
        print("✅ Local backup found. Failover successful!")
    else:
        logging.warning("⚠️ No local backup found. Attempting to fetch from S3...")

        if download_from_s3():
            logging.info("✅ Failover completed using S3 backup!")
            print("✅ Failover completed using S3 backup!")
        else:
            logging.critical("❌ Failover failed! No valid backup found.")
            print("❌ Failover failed! No valid backup found.")

if __name__ == "__main__":
    initiate_failover()
