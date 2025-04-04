import os
import time
import logging
import boto3
from botocore.exceptions import BotoCoreError, NoCredentialsError

# Logging setup
LOG_DIR = "E:/Saved Games/disaster-recovery-system/logs"
os.makedirs(LOG_DIR, exist_ok=True)  # Ensure logs directory exists

LOG_FILE = os.path.join(LOG_DIR, "failover.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
)

# Backup directory configuration
LOCAL_BACKUP_DIR = "E:/Saved Games/disaster-recovery-system/backups"
os.makedirs(LOCAL_BACKUP_DIR, exist_ok=True)  # Ensure backup directory exists

# AWS S3 Configuration
S3_BUCKET = "itm-disaster"
S3_BACKUP_KEY = "local_backup.zip"

# 🔹 Add AWS Credentials (Replace with your actual credentials)
AWS_ACCESS_KEY = "AKIAU6GD24HFHAA2LME"
AWS_SECRET_KEY = "Ud8MkRLxRpSH+B88Yhjpcl4Vp/hF8hWLq6XOjS0w"

# Initialize S3 client with error handling
try:
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
except BotoCoreError as e:
    logging.critical(f"❌ Failed to initialize S3 client: {e}")
    s3_client = None


def find_latest_local_backup():
    """Finds the latest local backup file (including timestamped ones)."""
    try:
        files = [f for f in os.listdir(LOCAL_BACKUP_DIR) if f.endswith(".zip")]

        if not files:
            logging.warning(f"⚠️ No local backups found in {LOCAL_BACKUP_DIR}. Current files: {os.listdir(LOCAL_BACKUP_DIR)}")
            return None

        latest_backup = max(files, key=lambda f: os.path.getctime(os.path.join(LOCAL_BACKUP_DIR, f)))
        latest_backup_path = os.path.join(LOCAL_BACKUP_DIR, latest_backup)

        logging.info(f"✅ Latest local backup found: {latest_backup_path}")
        return latest_backup_path
    except Exception as e:
        logging.error(f"❌ Error finding local backups: {e}")
        return None


def download_backup_from_s3():
    """Downloads the latest backup from S3 and stores it under backups/cloud/."""
    if not s3_client:
        logging.critical("❌ S3 client is not initialized. Cannot download backup.")
        return None

    timestamp = time.strftime("%Y%m%d_%H%M%S")  # Generate timestamp
    local_filename = f"cloud_backup_{timestamp}.zip"
    local_path = os.path.join(LOCAL_BACKUP_DIR, local_filename)  # Store in backups/cloud/

    try:
        logging.info("📥 Downloading latest cloud backup from S3...")
        s3_client.download_file(S3_BUCKET, S3_BACKUP_KEY, local_path)
        logging.info(f"✅ Backup downloaded successfully: {local_path}")
        return local_path  # Return new filename for restoration
    except NoCredentialsError:
        logging.error("❌ AWS credentials not found! Check your AWS setup.")
    except BotoCoreError as e:
        logging.error(f"❌ Failed to download backup from S3: {e}")
    except Exception as e:
        logging.error(f"❌ Unexpected error during S3 download: {e}")

    return None


def restore_from_backup(backup_file):
    """Restores system from the specified backup file."""
    try:
        logging.info(f"🔄 Restoring from backup: {backup_file}")

        # Simulating restoration process (replace with actual restore logic)
        time.sleep(3)

        logging.info("✅ System successfully recovered from backup.")
    except Exception as e:
        logging.error(f"❌ Error during restoration: {e}")


if __name__ == "__main__":
    logging.info("🚀 Starting disaster recovery process...")

    # Try finding the latest local backup first
    latest_backup = find_latest_local_backup()

    if latest_backup:
        restore_from_backup(latest_backup)
    else:
        logging.warning("⚠️ No local backup found! Downloading from cloud...")
        cloud_backup = download_backup_from_s3()

        if cloud_backup:
            restore_from_backup(cloud_backup)
        else:
            logging.critical("❌ Disaster recovery failed! No valid backup available.")

    logging.info("🏁 Disaster recovery process completed.")
