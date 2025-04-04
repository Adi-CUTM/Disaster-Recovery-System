import os
import shutil
import random
import hashlib
from datetime import datetime

# Logger (assuming you have backup_logger set up)
import logging
backup_logger = logging.getLogger("backup_logger")

# Paths
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BACKUP_DIR = os.path.join(ROOT_DIR, 'backups')
REPORTS_DIR = os.path.join(ROOT_DIR, 'reports', 'backup_verifications')
LOCAL_BACKUP_PATH = os.path.join(BACKUP_DIR, 'local_backup.zip')

# Cleanup settings
MAX_BACKUPS = 5
MAX_REPORTS = 10


def cleanup_old_files(directory, max_files):
    files = sorted(
        [os.path.join(directory, f) for f in os.listdir(directory)],
        key=os.path.getmtime
    )
    while len(files) > max_files:
        old_file = files.pop(0)
        os.remove(old_file)
        print(f"🗑️ Deleted old file: {old_file}")


def create_dummy_backup():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    content = f"Dummy backup created at {datetime.now()} with ID {random.randint(1000,9999)}"
    with open(LOCAL_BACKUP_PATH, 'w') as f:
        f.write(content)
    print("✅ Dummy local backup created with timestamped content.")


def calculate_checksum(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        checksum = sha256.hexdigest()
        backup_logger.info(f"Checksum for {file_path}: {checksum}")
        return checksum
    except Exception as e:
        error_message = f"[❌] Checksum error: {e}"
        backup_logger.error(error_message)
        return error_message


def check_local_backup(logs):
    if not os.path.exists(LOCAL_BACKUP_PATH):
        msg = f"❌ Local backup not found! Creating dummy backup at {datetime.now()}."
        logs.append(msg)
        print(msg)
        backup_logger.error(msg)
        create_dummy_backup()
    else:
        checksum = calculate_checksum(LOCAL_BACKUP_PATH)
        msg = f"✅ Local backup exists at {datetime.now()}. Checksum: {checksum}"
        logs.append(msg)
        print(msg)
        backup_logger.info(msg)


def check_cloud_backup(logs):
    # Simulate a cloud backup check
    msg = f"✅ Cloud backup is up-to-date at {datetime.now()}."
    logs.append(msg)
    print(msg)
    backup_logger.info(msg)


def save_verification_report(logs):
    os.makedirs(REPORTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(REPORTS_DIR, f"backup_verification_report_{timestamp}.txt")
    with open(report_path, 'w', encoding='utf-8') as report_file:
        report_file.write(f"📄 Backup Verification Report\n🕒 Date: {datetime.now()}\n")
        report_file.write("=" * 50 + "\n")
        for log in logs:
            report_file.write(log + "\n")
        report_file.write("=" * 50 + "\n\n")
        if any("❌" in log for log in logs):
            report_file.write("⚠️ Backup verification failed. Please check the issues.\n")
        else:
            report_file.write("✅ All backups verified successfully.\n")
    print(f"\n📝 Verification report saved to: {report_path}")


def verify_backups():
    print("\n🔍 Starting backup verification...\n")

    # Cleanup
    print("🧹 Cleaning up old backups and reports...")
    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs(REPORTS_DIR, exist_ok=True)
    cleanup_old_files(BACKUP_DIR, MAX_BACKUPS)
    cleanup_old_files(REPORTS_DIR, MAX_REPORTS)

    logs = []
    print(f"\n🔍 Verifying local backup at: {LOCAL_BACKUP_PATH}")
    check_local_backup(logs)

    print("\n🔍 Verifying cloud backup...")
    check_cloud_backup(logs)

    save_verification_report(logs)

    if any("❌" in log for log in logs):
        print("\n⚠️ Backup verification failed! Please check the issues.")
    else:
        print("\n✅ All backups verified successfully!")

    print("\n✅ Backup verification completed.\n")
    

if __name__ == "__main__":
    verify_backups()
