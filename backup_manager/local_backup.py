import os
import shutil
import datetime

# Define directories
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKUP_SOURCE_DIR = os.path.join(BASE_DIR, "databases")  
BACKUP_DEST_DIR = os.path.join(BASE_DIR, "backups", "local")

def ensure_backup_dir():
    """Ensure local backup directory exists."""
    if not os.path.exists(BACKUP_DEST_DIR):
        os.makedirs(BACKUP_DEST_DIR)

def rotate_backups(max_backups=5):
    """Delete oldest backups if exceeding max_backups."""
    backups = sorted(
        [f for f in os.listdir(BACKUP_DEST_DIR) if f.startswith("local_backup_") and f.endswith(".zip")],
        key=lambda x: os.path.getctime(os.path.join(BACKUP_DEST_DIR, x))
    )
    while len(backups) > max_backups:
        oldest_backup = backups.pop(0)
        os.remove(os.path.join(BACKUP_DEST_DIR, oldest_backup))
        print(f"🗑️ Deleted old backup: {oldest_backup}")

def create_local_backup():
    """Create a local zip backup."""
    ensure_backup_dir()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"local_backup_{timestamp}.zip"
    backup_path = os.path.join(BACKUP_DEST_DIR, backup_name)

    print(f"🔄 Creating local backup: {backup_path}")
    
    shutil.make_archive(backup_path.replace(".zip", ""), 'zip', BACKUP_SOURCE_DIR)
    
    print(f"✅ Backup created successfully at: {backup_path}")
    
    rotate_backups()  # ✅ Rotation added here

    return backup_path

if __name__ == "__main__":
    create_local_backup()
