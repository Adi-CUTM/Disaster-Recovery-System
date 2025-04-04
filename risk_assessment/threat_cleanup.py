import os
import json
import time
from monitoring_logging.logger import backup_logger, error_logger
from risk_assessment.report_generator import generate_report

# Corrected path for threats directory inside risk_assessment
THREATS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "threats"))
FOUND_ISSUES_PATH = os.path.join(THREATS_DIR, "found_issues.json")
CLEANED_ISSUES_PATH = os.path.join(THREATS_DIR, "cleaned_issues.json")


def ensure_threats_dir():
    """Ensure the threats directory exists inside risk_assessment."""
    if not os.path.exists(THREATS_DIR):
        try:
            os.makedirs(THREATS_DIR)
            backup_logger.info(f" Created threats directory at: {THREATS_DIR}")
        except Exception as e:
            error_logger.error(f"❌ Failed to create threats directory: {e}")
            print(f"❌ Error creating threats directory: {e}")


def load_found_issues():
    """Load detected vulnerabilities from found_issues.json."""
    if not os.path.exists(FOUND_ISSUES_PATH):
        backup_logger.warning(" No found issues file detected. Skipping cleanup.")
        return []

    try:
        with open(FOUND_ISSUES_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        error_logger.error(f" Failed to load found issues: {e}")
        return []


def cleanup_threats():
    """Remove high-severity and critical-severity threats and save cleaned issues."""
    ensure_threats_dir()  # Now correctly checks inside risk_assessment
    found_issues = load_found_issues()

    if not found_issues:
        print("\n No threats found. Cleanup skipped.\n")
        return

    # Generate report before cleanup
    generate_report(found_issues, report_type="found")

    # ✅ Filter out High and Critical severity threats
    cleaned_issues = [
        issue for issue in found_issues
        if issue["severity"] not in ["High", "Critical"]
    ]

    # Simulate cleanup process
    print("\n🛠️ Removing High and Critical severity threats...\n")
    time.sleep(2)

    with open(CLEANED_ISSUES_PATH, "w", encoding="utf-8") as file:
        json.dump(cleaned_issues, file, indent=4)

    backup_logger.info(" Threat cleanup completed. High and Critical threats removed.")
    print("\n Cleanup completed. High and Critical threats removed.\n")

    # Generate report after cleanup
    generate_report(cleaned_issues, report_type="cleaned")


if __name__ == "__main__":
    cleanup_threats()
