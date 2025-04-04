import os
import datetime
from monitoring_logging.logger import backup_logger, error_logger

# Final path for risk assessment reports
REPORTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "reports", "risk_assessments")
)


def ensure_reports_dir():
    """Create the risk_assessments directory if it doesn't exist."""
    if not os.path.exists(REPORTS_DIR):
        try:
            os.makedirs(REPORTS_DIR)
            backup_logger.info(f"✅ Created reports directory at: {REPORTS_DIR}")
        except Exception as e:
            error_logger.error(f"❌ Failed to create reports directory: {e}")
            print(f"❌ Error creating reports directory: {e}")


def generate_report(vulnerabilities, report_type="general"):
    """Generate a risk assessment report and save it to the reports directory.

    Args:
        vulnerabilities (list): List of detected vulnerabilities.
        report_type (str): Type of report (e.g., 'found', 'cleaned', 'general').
    """
    ensure_reports_dir()

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"risk_assessment_{report_type}_{timestamp}.txt"
    report_path = os.path.join(REPORTS_DIR, report_filename)

    try:
        with open(report_path, "w", encoding="utf-8") as report_file:
            report_file.write(f"📄 Risk Assessment Report ({report_type.capitalize()})\n")
            report_file.write(f"🕒 Date: {datetime.datetime.now()}\n")
            report_file.write("=" * 60 + "\n\n")

            if not vulnerabilities:
                report_file.write("✅ No vulnerabilities found. Your system is secure.\n")
            else:
                for vuln in vulnerabilities:
                    report_file.write(f"[{vuln['severity']}] {vuln['issue']}\n")

                report_file.write("\n⚠️ Total Issues Found: {}\n".format(len(vulnerabilities)))

            report_file.write("=" * 60 + "\n")
            report_file.write("🔒 End of Report\n")

        backup_logger.info(f"📝 {report_type.capitalize()} risk assessment report saved to: {report_path}")
        print(f"\n📝 {report_type.capitalize()} risk assessment report saved to: {report_path}\n")
        return report_path

    except Exception as e:
        error_logger.error(f"❌ Failed to generate {report_type} report: {e}")
        print(f"❌ Error generating {report_type} report: {e}")
