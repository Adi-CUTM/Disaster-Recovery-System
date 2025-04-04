import os
import logging
import send2trash  # Moves files/folders to the Recycle Bin
from cryptography.fernet import Fernet

# Paths
DOWNLOADS_DIR = "C:/Users/adity/Downloads"
ENCRYPTED_DIR = os.path.join(DOWNLOADS_DIR, "Encrypted")
KEY_FILE = "ransom_key.key"
RANSOM_NOTE = os.path.join(DOWNLOADS_DIR, "ransom_note.txt")
LOGS_DIR = "E:/Saved Games/disaster-recovery-system/logs"
LOG_FILE = os.path.join(LOGS_DIR, "ransomware_recovery.log")

# Ensure log directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Load Encryption Key
def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        logging.error("❌ Encryption key file not found!")
        print("❌ Encryption key file not found!")
        return None

cipher = Fernet(load_key()) if load_key() else None

# Decrypt a file
def decrypt_file(encrypted_path):
    try:
        if not encrypted_path.endswith(".enc"):
            logging.warning(f"⚠️ Skipping non-encrypted file: {encrypted_path}")
            return
        
        with open(encrypted_path, "rb") as f:
            encrypted_data = f.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        original_path = encrypted_path.replace(".enc", "")
        with open(original_path, "wb") as f:
            f.write(decrypted_data)

        os.remove(encrypted_path)  # Remove encrypted file

        logging.info(f"✅ Decrypted: {original_path}")
        print(f"✅ Decrypted: {original_path}")

    except Exception as e:
        logging.error(f"❌ Error decrypting {encrypted_path}: {e}")
        print(f"❌ Error decrypting {encrypted_path}: {e}")

# Move Encrypted folder to Recycle Bin
def move_to_recycle_bin():
    try:
        if os.path.exists(ENCRYPTED_DIR):
            send2trash.send2trash(ENCRYPTED_DIR)
            logging.info(f"🗑️ Moved {ENCRYPTED_DIR} to Recycle Bin.")
            print(f"🗑️ Moved {ENCRYPTED_DIR} to Recycle Bin.")
        else:
            logging.warning(f"⚠️ Encrypted folder not found: {ENCRYPTED_DIR}")

    except Exception as e:
        logging.error(f"❌ Error moving {ENCRYPTED_DIR} to Recycle Bin: {e}")
        print(f"❌ Error moving {ENCRYPTED_DIR} to Recycle Bin: {e}")

# Recover all encrypted files
def recover_files():
    if not cipher:
        print("🔑 No valid encryption key found. Decryption failed.")
        return

    print("🔍 Scanning for encrypted files...")
    logging.info("🔍 Scanning for encrypted files...")

    recovered = False
    for file in os.listdir(DOWNLOADS_DIR):
        if file.endswith(".enc"):  # Target encrypted files
            enc_path = os.path.join(DOWNLOADS_DIR, file)
            print(f"🔓 Decrypting {enc_path}...")
            decrypt_file(enc_path)
            recovered = True

    # Check if the Encrypted folder contains any encrypted files
    if os.path.exists(ENCRYPTED_DIR):
        for file in os.listdir(ENCRYPTED_DIR):
            if file.endswith(".enc"):
                enc_path = os.path.join(ENCRYPTED_DIR, file)
                print(f"🔓 Decrypting {enc_path}...")
                decrypt_file(enc_path)
                recovered = True

    if recovered:
        # Remove ransom note
        if os.path.exists(RANSOM_NOTE):
            os.remove(RANSOM_NOTE)
            logging.info("📜 Ransom note deleted.")
            print("📜 Ransom note deleted.")

        # Move Encrypted folder to Recycle Bin
        move_to_recycle_bin()

        print("✅ Recovery process completed successfully!")
        logging.info("✅ Recovery process completed successfully!")
    else:
        print("❌ No encrypted files found.")
        logging.warning("❌ No encrypted files found.")

if __name__ == "__main__":
    recover_files()


