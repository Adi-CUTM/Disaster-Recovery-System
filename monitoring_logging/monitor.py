import os
import time
import psutil
from monitoring_logging.logger import backup_logger, error_logger

BACKUP_DIR = r"E:\Saved Games\disaster-recovery-system\backups"
CHECK_INTERVAL = 300  
MAX_CHECKS = None  

def is_backup_directory_valid(backup_dir):
    """Check if the backup directory exists."""
    return os.path.exists(backup_dir)

def get_latest_backup(backup_dir):
    """Get the latest backup file from the directory."""
    try:
        backups = os.listdir(backup_dir)
        if not backups:
            return None
        return max([os.path.join(backup_dir, f) for f in backups], key=os.path.getctime)
    except Exception:
        return None

def check_system_health():
    """Check if the primary system is running."""
    try:
        # Example: Check if a critical process is running
        critical_process = "some_critical_process.exe"  # Change this to actual process
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == critical_process:
                return True  # System is healthy
        return False  # System is down
    except Exception as e:
        error_logger.error(f"❌ Error checking system health: {e}")
        return False

def monitor_backups(backup_dir, interval=CHECK_INTERVAL, max_checks=MAX_CHECKS):
    """Monitors the backup directory for new backups."""
    backup_logger.info(f"🔍 Starting monitoring of backups in: {backup_dir}")
    if not is_backup_directory_valid(backup_dir):
        return
    
    check_count = 0
    try:
        while True:
            latest_backup = get_latest_backup(backup_dir)
            if latest_backup:
                backup_logger.info(f"📌 Monitoring latest backup: {latest_backup}")
            else:
                backup_logger.warning("⚠️ No valid backups detected.")

            check_count += 1
            if max_checks and check_count >= max_checks:
                backup_logger.info("✅ Completed maximum monitoring checks. Stopping monitoring.")
                break

            time.sleep(interval)

    except KeyboardInterrupt:
        backup_logger.info("🛑 Backup monitoring stopped manually.")
    except Exception as e:
        error_logger.error(f"❌ Unexpected error while monitoring backups: {e}")

if __name__ == "__main__":
    monitor_backups(BACKUP_DIR)
