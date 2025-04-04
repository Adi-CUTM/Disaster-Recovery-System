

# from flask import Flask, jsonify
# import os
# import shutil
# import logging
# from datetime import datetime

# app = Flask(__name__)

# # Paths
# BACKUPS_FOLDER = r"E:\Saved Games\disaster-recovery-system\backups"
# LOCAL_BACKUP_FOLDER = os.path.join(BACKUPS_FOLDER, "local")

# # Logging directories
# PHISHING_REPORTS_FOLDER = r"E:\Saved Games\disaster-recovery-system\reports\phishing_reports"
# RECOVERY_REPORTS_FOLDER = r"E:\Saved Games\disaster-recovery-system\reports\recovery_reports"

# # Ensure logging directories exist
# os.makedirs(PHISHING_REPORTS_FOLDER, exist_ok=True)
# os.makedirs(RECOVERY_REPORTS_FOLDER, exist_ok=True)

# # Setup phishing log
# phishing_log_path = os.path.join(PHISHING_REPORTS_FOLDER, "phishing_clicks.log")
# logging.basicConfig(
#     filename=phishing_log_path,
#     level=logging.INFO,
#     format="%(asctime)s - %(message)s"
# )

# def delete_txt_and_zip(folder_path):
#     """Delete .txt and .zip files inside a given folder."""
#     deleted_files = []
#     if os.path.exists(folder_path):
#         for file in os.listdir(folder_path):
#             file_path = os.path.join(folder_path, file)
#             if file.lower().endswith((".txt", ".zip")):
#                 os.remove(file_path)
#                 deleted_files.append(file)
#     return deleted_files

# @app.route("/clicked")
# def delete_local_backups():
#     """Delete .txt and .zip files inside 'backups/local' and 'backups' folders."""
#     try:
#         deleted_local = delete_txt_and_zip(LOCAL_BACKUP_FOLDER)
#         deleted_backups = delete_txt_and_zip(BACKUPS_FOLDER)

#         # Log phishing attempt
#         log_message = f"⚠️ Phishing link clicked! Triggered deletion at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
#         logging.info(log_message)

#         return jsonify({
#             "message": "Operation completed!",
#             "deleted_files_local": deleted_local if deleted_local else "No .txt or .zip files found in 'local'.",
#             "deleted_files_backups": deleted_backups if deleted_backups else "No .txt or .zip files found in 'backups'."
#         }), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # ✅ Function for importing in `commands.py`
# def track_phishing_clicks():
#     """Start the Flask phishing tracking server."""
#     print("📡 Tracking phishing clicks on port 5000...")
#     app.run(port=5000, debug=True)







# from flask import Flask, jsonify
# import os
# import logging
# from datetime import datetime

# app = Flask(__name__)

# # Paths
# BACKUPS_FOLDER = r"E:\Saved Games\disaster-recovery-system\backups"
# LOCAL_BACKUP_FOLDER = os.path.join(BACKUPS_FOLDER, "local")

# # Logging directories
# PHISHING_REPORTS_FOLDER = r"E:\Saved Games\disaster-recovery-system\reports\phishing_reports"
# RECOVERY_REPORTS_FOLDER = r"E:\Saved Games\disaster-recovery-system\reports\recovery_reports"

# # Ensure logging directories exist
# os.makedirs(PHISHING_REPORTS_FOLDER, exist_ok=True)
# os.makedirs(RECOVERY_REPORTS_FOLDER, exist_ok=True)

# # Setup phishing log
# phishing_log_path = os.path.join(PHISHING_REPORTS_FOLDER, "phishing_clicks.log")
# logging.basicConfig(
#     filename=phishing_log_path,
#     level=logging.INFO,
#     format="%(asctime)s - %(message)s"
# )

# def delete_all_files(folder_path):
#     """Delete all files inside a given folder."""
#     deleted_files = []
#     if os.path.exists(folder_path):
#         for file in os.listdir(folder_path):
#             file_path = os.path.join(folder_path, file)
#             if os.path.isfile(file_path):  # Ensure it's a file before deleting
#                 os.remove(file_path)
#                 deleted_files.append(file)
#     return deleted_files

# @app.route("/clicked")
# def delete_local_backups():
#     """Delete all files inside 'backups/local' and 'backups' folders."""
#     try:
#         deleted_local = delete_all_files(LOCAL_BACKUP_FOLDER)
#         deleted_backups = delete_all_files(BACKUPS_FOLDER)

#         # Log phishing attempt
#         log_message = f"⚠️ Phishing link clicked! Triggered deletion at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
#         logging.info(log_message)

#         return jsonify({
#             "message": "Operation completed! All files deleted.",
#             "deleted_files_local": deleted_local if deleted_local else "No files found in 'local'.",
#             "deleted_files_backups": deleted_backups if deleted_backups else "No files found in 'backups'."
#         }), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # ✅ Function for importing in `commands.py`
# def track_phishing_clicks():
#     """Start the Flask phishing tracking server."""
#     print("📡 Tracking phishing clicks on port 5000...")
#     app.run(port=5000, debug=True)
















from flask import Flask, jsonify
import os
import logging
from datetime import datetime

app = Flask(__name__)

# Paths
BACKUPS_FOLDER = r"E:\Saved Games\disaster-recovery-system\backups"
LOCAL_BACKUP_FOLDER = os.path.join(BACKUPS_FOLDER, "local")

# Logging directories
PHISHING_REPORTS_FOLDER = r"E:\Saved Games\disaster-recovery-system\reports\phishing_reports"
os.makedirs(PHISHING_REPORTS_FOLDER, exist_ok=True)

# Setup phishing log
phishing_log_path = os.path.join(PHISHING_REPORTS_FOLDER, "phishing_clicks.log")
logging.basicConfig(filename=phishing_log_path, level=logging.INFO, format="%(asctime)s - %(message)s")

def delete_all_files(folder_path):
    """Delete all files inside a given folder."""
    deleted_files = []
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                deleted_files.append(file)
    return deleted_files

@app.route("/clicked")
def delete_local_backups():
    """Delete all files inside 'local' and 'backups'."""
    try:
        deleted_local = delete_all_files(LOCAL_BACKUP_FOLDER)
        deleted_backups = delete_all_files(BACKUPS_FOLDER)

        # Log phishing attempt
        log_message = f"⚠️ Phishing link clicked! Files deleted at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
        logging.info(log_message)

        return jsonify({
            "message": "Operation completed! All files deleted.",
            "deleted_files_local": deleted_local if deleted_local else "No files found in 'local'.",
            "deleted_files_backups": deleted_backups if deleted_backups else "No files found in 'backups'."
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def track_phishing_clicks():
    """Start the Flask phishing tracking server (without debug mode)."""
    print("📡 Tracking phishing clicks on http://localhost:5000/clicked")
    app.run(port=5000, debug=False, use_reloader=False)
