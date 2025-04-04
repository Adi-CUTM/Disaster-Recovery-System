import os
import zipfile
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# AWS credentials and config
AWS_ACCESS_KEY = "AKIAU6GD24HFHAA2LME5"
AWS_SECRET_KEY = "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"
BUCKET_NAME = "itm-disaster"
BACKUP_DIR = r"E:\Saved Games\disaster-recovery-system\backups\local"
ZIP_PATH = r"E:\Saved Games\disaster-recovery-system\backups\local_backup.zip"
S3_OBJECT_NAME = "local_backup.zip"


# Step 1: Create dummy backup files
def create_dummy_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    for i in range(1, 4):
        file_path = os.path.join(BACKUP_DIR, f"dummy_file_{i}.txt")
        with open(file_path, "w") as f:
            f.write(f"This is dummy backup file {i}.")
    print(f"✅ Dummy backup files created in {BACKUP_DIR}")


# Step 2: Zip the backup folder
def create_zip_backup():
    with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(BACKUP_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.dirname(BACKUP_DIR))
                zipf.write(file_path, arcname)
    print(f"✅ Backup ZIP created at {ZIP_PATH}")


# Step 3: Upload the ZIP file to S3
def upload_backup():
    try:
        s3 = boto3.client('s3',
                          aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_KEY)

        print(f"🔄 Uploading {ZIP_PATH} to S3 bucket '{BUCKET_NAME}'...")

        s3.upload_file(ZIP_PATH, BUCKET_NAME, S3_OBJECT_NAME)

        print("✅ Backup successfully uploaded to S3!")

    except FileNotFoundError:
        print("❌ Backup file not found.")
    except NoCredentialsError:
        print("❌ AWS credentials not available.")
    except ClientError as e:
        print(f"❌ AWS Client error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# Main process
if __name__ == "__main__":
    create_dummy_backup()
    create_zip_backup()
    upload_backup()
