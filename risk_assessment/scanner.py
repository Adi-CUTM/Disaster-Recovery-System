



# import os
# import time
# import json
# import hashlib
# import requests
# from monitoring_logging.logger import backup_logger, error_logger
# from risk_assessment.threat_cleanup import cleanup_threats

# # API Configuration for VirusTotal
# VIRUSTOTAL_API_KEY = "507945d4e23a35be3738389326a9aaa2415de5f4850fb65bb32a84373245ffc2"
# VIRUSTOTAL_API_URL = "https://www.virustotal.com/api/v3/files"

# # Define threat storage directory
# THREATS_DIR = os.path.join(os.path.dirname(__file__), "threats")
# FOUND_ISSUES_FILE = os.path.join(THREATS_DIR, "found_issues.json")

# # Target file extensions (updated with .txt, .ppt, and .pptx)
# TARGET_EXTENSIONS = [
#     ".pdf", ".zip", ".jpg", ".jpeg", ".png", ".gif",  # Existing types
#     ".txt", ".ppt", ".pptx"  # New types added
# ]

# # Target drives to scan
# DRIVES_TO_SCAN = ["C:\\", "D:\\", "E:\\"]


# def ensure_threats_dir():
#     """Ensure that the threats directory exists."""
#     os.makedirs(THREATS_DIR, exist_ok=True)


# def get_file_hash(file_path):
#     """Generate SHA256 hash of the file."""
#     try:
#         with open(file_path, "rb") as f:
#             file_hash = hashlib.sha256(f.read()).hexdigest()
#         return file_hash
#     except Exception as e:
#         error_logger.error(f"❌ Error calculating file hash: {e}")
#         return None


# def scan_with_virustotal(file_path):
#     """Send file hash or upload file to VirusTotal for scanning."""
#     file_hash = get_file_hash(file_path)

#     if not file_hash:
#         return None

#     headers = {
#         "x-apikey": VIRUSTOTAL_API_KEY,
#     }
#     params = {"hash": file_hash}

#     try:
#         # Check if the file hash already exists in VirusTotal
#         response = requests.get(f"{VIRUSTOTAL_API_URL}/{file_hash}", headers=headers)

#         if response.status_code == 200:
#             result = response.json()
#             if result["data"]["attributes"]["last_analysis_stats"]["malicious"] > 0:
#                 return "Malicious"
#             else:
#                 return "Clean"
#         else:
#             # If hash is not found, upload file for scanning
#             files = {"file": (os.path.basename(file_path), open(file_path, "rb"))}
#             upload_response = requests.post(VIRUSTOTAL_API_URL, headers=headers, files=files)

#             if upload_response.status_code == 200:
#                 analysis_result = upload_response.json()
#                 if analysis_result["data"]["attributes"]["last_analysis_stats"]["malicious"] > 0:
#                     return "Malicious"
#                 else:
#                     return "Clean"
#             else:
#                 error_logger.error(f"⚠️ Error uploading file: {upload_response.json()}")
#                 return "Unknown"
#     except Exception as e:
#         error_logger.error(f"❌ Error connecting to VirusTotal API: {e}")
#         return "Error"


# def scan_files_in_directory(directory):
#     """Scan files in a directory recursively and check for threats."""
#     found_issues = []

#     for root, _, files in os.walk(directory):
#         for file in files:
#             if any(file.lower().endswith(ext) for ext in TARGET_EXTENSIONS):
#                 file_path = os.path.join(root, file)

#                 print(f"🔍 Scanning file: {file_path}")
#                 scan_result = scan_with_virustotal(file_path)

#                 if scan_result == "Malicious":
#                     issue = {
#                         "file_path": file_path,
#                         "severity": "Critical",
#                         "issue": "Malicious file detected via VirusTotal",
#                     }
#                     found_issues.append(issue)
#                     backup_logger.warning(f"⚠️ Malicious file found: {file_path}")
#                 elif scan_result == "Clean":
#                     backup_logger.info(f"✅ File is safe: {file_path}")
#                 elif scan_result == "Error":
#                     error_logger.error(f"❌ Error scanning file: {file_path}")

#     return found_issues


# def system_scan(severity_filter=None, delay=0.3):
#     """
#     Scans system drives and checks for harmful files using VirusTotal.
#     Automatically triggers threat cleanup after scanning.
#     """
#     ensure_threats_dir()
#     all_found_issues = []

#     print("\n🔍 Scanning system drives for threats...\n")
#     for drive in DRIVES_TO_SCAN:
#         if os.path.exists(drive):
#             print(f"📂 Scanning drive: {drive}")
#             found_issues = scan_files_in_directory(drive)
#             all_found_issues.extend(found_issues)
#         else:
#             print(f"⚠️ Drive {drive} not accessible. Skipping...")

#         time.sleep(delay)

#     # Save found issues to JSON file
#     try:
#         with open(FOUND_ISSUES_FILE, "w", encoding="utf-8") as file:
#             json.dump(all_found_issues, file, indent=4)
#         print(f"\n✅ Scan complete. Total issues found: {len(all_found_issues)}")
#         print(f"📄 Scan results saved to: {FOUND_ISSUES_FILE}")
#         backup_logger.info(f"System scan complete. {len(all_found_issues)} issues found.")
#     except Exception as e:
#         error_logger.error(f"❌ Failed to save found issues: {e}")
#         print(f"❌ Error saving scan results: {e}")
#         return

#     # Trigger threat cleanup for high/critical severity issues
#     print("\n🚀 Starting threat cleanup for detected high-severity threats...\n")
#     cleanup_threats()
#     print("🔔 Threat cleanup finished. Check logs and reports for details.\n")
#     backup_logger.info("Threat cleanup process completed after scan.")

#     return all_found_issues


# if __name__ == "__main__":
#     system_scan(severity_filter=["Critical", "High"])



import os
import time
import json
import hashlib
import shutil
import requests
from monitoring_logging.logger import backup_logger, error_logger
from risk_assessment.threat_cleanup import cleanup_threats

# API Configuration for VirusTotal
VIRUSTOTAL_API_KEY = "507945d4e23a35be3738389326a9aaa2415de5f4850fb65bb32a84373245ffc2"
VIRUSTOTAL_API_URL = "https://www.virustotal.com/api/v3/files"

# Define directories
BASE_DIR = os.path.dirname(__file__)
THREATS_DIR = os.path.join(BASE_DIR, "threats")
LOG_DIR = os.path.join(BASE_DIR, "log")  # Log directory for quarantine log
QUARANTINE_LOG_FILE = os.path.join(LOG_DIR, "quarantine_log.json")
FOUND_ISSUES_FILE = os.path.join(THREATS_DIR, "found_issues.json")

# Target file extensions
TARGET_EXTENSIONS = [".pdf", ".zip", ".jpg", ".jpeg", ".png", ".gif", ".txt", ".ppt", ".pptx"]

# Target drives to scan
DRIVES_TO_SCAN = ["C:\\", "D:\\", "E:\\"]


def ensure_directories():
    """Ensure that the necessary directories exist."""
    os.makedirs(THREATS_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)


def get_file_hash(file_path):
    """Generate SHA256 hash of the file."""
    try:
        with open(file_path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        return file_hash
    except Exception as e:
        error_logger.error(f"❌ Error calculating file hash: {e}")
        return None


def quarantine_file(file_path):
    """Move a malicious file to the threats (quarantine) folder."""
    try:
        if os.path.exists(file_path):
            quarantined_path = os.path.join(THREATS_DIR, os.path.basename(file_path))
            shutil.move(file_path, quarantined_path)
            log_quarantine(file_path, quarantined_path)
            backup_logger.warning(f"⚠️ File quarantined: {quarantined_path}")
            return quarantined_path
    except Exception as e:
        error_logger.error(f"❌ Error quarantining file {file_path}: {e}")
    return None


def log_quarantine(original_path, quarantined_path):
    """Log quarantined files in the quarantine log file."""
    quarantine_log = []
    if os.path.exists(QUARANTINE_LOG_FILE):
        with open(QUARANTINE_LOG_FILE, "r", encoding="utf-8") as file:
            try:
                quarantine_log = json.load(file)
            except json.JSONDecodeError:
                quarantine_log = []

    quarantine_log.append({"original_path": original_path, "quarantined_path": quarantined_path, "timestamp": time.ctime()})
    
    with open(QUARANTINE_LOG_FILE, "w", encoding="utf-8") as file:
        json.dump(quarantine_log, file, indent=4)


def scan_with_virustotal(file_path):
    """Send file hash or upload file to VirusTotal for scanning."""
    file_hash = get_file_hash(file_path)
    if not file_hash:
        return None

    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    try:
        response = requests.get(f"{VIRUSTOTAL_API_URL}/{file_hash}", headers=headers)
        if response.status_code == 200:
            result = response.json()
            if result["data"]["attributes"]["last_analysis_stats"]["malicious"] > 0:
                return "Malicious"
            else:
                return "Clean"
    except Exception as e:
        error_logger.error(f"❌ Error connecting to VirusTotal API: {e}")
    return "Error"


def scan_files_in_directory(directory):
    """Scan files in a directory recursively and check for threats."""
    found_issues = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in TARGET_EXTENSIONS):
                file_path = os.path.join(root, file)
                print(f"🔍 Scanning file: {file_path}")
                scan_result = scan_with_virustotal(file_path)

                if scan_result == "Malicious":
                    issue = {"file_path": file_path, "severity": "Critical", "issue": "Malicious file detected"}
                    found_issues.append(issue)
                    quarantine_file(file_path)
                elif scan_result == "Clean":
                    backup_logger.info(f"✅ File is safe: {file_path}")
                elif scan_result == "Error":
                    error_logger.error(f"❌ Error scanning file: {file_path}")
    return found_issues


def system_scan(severity_filter=None, delay=0.3):
    """Scans system drives and checks for harmful files using VirusTotal."""
    ensure_directories()
    all_found_issues = []
    print("\n🔍 Scanning system drives for threats...\n")
    for drive in DRIVES_TO_SCAN:
        if os.path.exists(drive):
            print(f"📂 Scanning drive: {drive}")
            found_issues = scan_files_in_directory(drive)
            all_found_issues.extend(found_issues)
        else:
            print(f"⚠️ Drive {drive} not accessible. Skipping...")
        time.sleep(delay)
    
    try:
        with open(FOUND_ISSUES_FILE, "w", encoding="utf-8") as file:
            json.dump(all_found_issues, file, indent=4)
        print(f"\n✅ Scan complete. Total issues found: {len(all_found_issues)}")
    except Exception as e:
        error_logger.error(f"❌ Failed to save found issues: {e}")
    
    print("\n🚀 Starting threat cleanup for detected high-severity threats...\n")
    cleanup_threats()
    backup_logger.info("Threat cleanup process completed after scan.")
    return all_found_issues


if __name__ == "__main__":
    system_scan(severity_filter=["Critical", "High"])
