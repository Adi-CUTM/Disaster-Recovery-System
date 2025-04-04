import logging
import os

# Ensure logs directory exists
LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# === Backup Logger ===
backup_logger = logging.getLogger('backup_logger')
backup_logger.propagate = False  # Prevent double logging
backup_handler = logging.FileHandler(
    os.path.join(LOG_DIR, 'backup_logs.log'), encoding='utf-8'
)
backup_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
backup_handler.setFormatter(backup_formatter)
backup_logger.addHandler(backup_handler)
backup_logger.setLevel(logging.INFO)

# Optional: Stream logs to console too (for real-time visibility)
backup_stream_handler = logging.StreamHandler()
backup_stream_handler.setFormatter(backup_formatter)
backup_logger.addHandler(backup_stream_handler)

# === Error Logger ===
error_logger = logging.getLogger('error_logger')
error_logger.propagate = False  # Prevent double logging
error_handler = logging.FileHandler(
    os.path.join(LOG_DIR, 'error_logs.log'), encoding='utf-8'
)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)
error_logger.setLevel(logging.ERROR)

# Optional: Stream error logs to console too
error_stream_handler = logging.StreamHandler()
error_stream_handler.setFormatter(error_formatter)
error_logger.addHandler(error_stream_handler)
