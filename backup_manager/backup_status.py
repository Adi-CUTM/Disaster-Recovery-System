import os
import logging
import boto3
from datetime import datetime
from botocore.exceptions import NoCredentialsError, ClientError

# Setup logging
LOG_DIR = "E:/Saved Games/disaster-recovery-system/logs"
os.makedirs(LOG_DIR, exist_ok=True)  # Ensure the logs directory exists
LOG_FILE = os.path.join(LOG_DIR, "backup_status.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
)

# AWS S3 Configuration
AWS_ACCESS_KEY = "AKIAU6GD24HFHAA2LME5"
AWS_SECRET_KEY = "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"
BUCKET_NAME = "itm-disaster"
S3_OBJECT_NAME = "local_backup.zip"

# Backup file paths
LOCAL_BACKUP_PATH = r"E:\Saved Games\disaster-recovery-system\backups\local_backup.zip"


def check_local_backup():
    """Check if local backup exists and retrieve its last modified timestamp."""
    if os.path.exists(LOCAL_BACKUP_PATH):
        modified_time = datetime.fromtimestamp(os.path.getmtime(LOCAL_BACKUP_PATH))
        logging.info(f"✅ Local backup found: {LOCAL_BACKUP_PATH}")
        logging.info(f"   Last modified: {modified_time}")
        return True
    else:
        logging.warning("❌ Local backup not found.")
        return False


def check_cloud_backup():
    """Check if cloud backup exists in S3 and retrieve its last modified timestamp."""
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )

        response = s3.head_object(Bucket=BUCKET_NAME, Key=S3_OBJECT_NAME)
        last_modified = response['LastModified']
        logging.info(f"✅ Cloud backup found in S3 bucket '{BUCKET_NAME}'.")
        logging.info(f"   Last modified: {last_modified}")
        return True

    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            logging.warning("❌ Cloud backup not found in S3.")
        else:
            logging.error(f"❌ AWS Client error: {e}")
        return False
    except NoCredentialsError:
        logging.critical("❌ AWS credentials not available.")
        return False
    except Exception as e:
        logging.error(f"❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    logging.info("🔍 Checking local backup...")
    local_ok = check_local_backup()

    logging.info("🔍 Checking cloud backup...")
    cloud_ok = check_cloud_backup()

    if local_ok and cloud_ok:
        logging.info("🎉 Backup status: ALL GOOD!")
        print("\n🎉 Backup status: ALL GOOD!")
    else:
        logging.warning("⚠️ Backup status: ISSUES FOUND. Check logs for details.")
        print("\n⚠️ Backup status: ISSUES FOUND. Check logs for details.")
