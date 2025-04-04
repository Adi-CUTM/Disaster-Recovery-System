import subprocess
from monitoring_logging.logger import backup_logger, error_logger

def run_local_backup():
    try:
        backup_logger.info("Starting local backup...")
        subprocess.run(["python", "backup_manager/local_backup.py"], check=True)
        backup_logger.info("Local backup completed successfully.")
    except subprocess.CalledProcessError as e:
        error_logger.error(f"Local backup failed: {e}")

def run_cloud_backup():
    try:
        backup_logger.info("Starting cloud backup...")
        subprocess.run(["python", "backup_manager/cloud_backup.py"], check=True)
        backup_logger.info("Cloud backup uploaded successfully.")
    except subprocess.CalledProcessError as e:
        error_logger.error(f"Cloud backup failed: {e}")

def check_backup_status():
    try:
        backup_logger.info("Checking backup status...")
        subprocess.run(["python", "backup_manager/backup_status.py"], check=True)
        backup_logger.info("Backup status check completed.")
    except subprocess.CalledProcessError as e:
        error_logger.error(f"Backup status check failed: {e}")

