import sys
import os
from cli.helpers import run_local_backup, run_cloud_backup, check_backup_status
from monitoring_logging.logger import backup_logger, error_logger
from monitoring_logging.monitor import monitor_backups

# Import Phishing & Ransomware Modules
from phishing_sim.send_phishing_email import send_email
from phishing_sim.track_clicks import track_phishing_clicks
from ransom_attack.ransomware_recovery import recover_files
from ransom_attack.ransomware_recovery import decrypt_file

# ✅ Updated: Import failover_handler for phishing recovery & disaster recovery
from recovery_site.failover_handler import initiate_failover


def show_menu():
    """Display the CLI Menu."""
    print("\n🔹 Disaster Recovery CLI - Main Menu")
    print("1️⃣  Check Database Connection")
    print("2️⃣  Run Risk Assessment")
    print("3️⃣  Verify Backups")
    print("4️⃣  Run Local Backup")
    print("5️⃣  Run Cloud Backup")
    print("6️⃣  Check Backup Status")
    print("7️⃣  Monitor Backups")
    print("8️⃣  Run Phishing Simulation")
    print("9️⃣  Recover from Phishing Attack")
    print("🔟  Launch Ransomware Attack")
    print("1️⃣1️⃣  Recover from Ransomware Attack")
    print("1️⃣2️⃣  Initiate Disaster Recovery")
    print("0️⃣  Exit")
    print("👉 Enter your choice (0-12): ", end="")


def run_command(command, interval=300, max_checks=None):
    """Run the selected command."""
    try:
        backup_logger.info(f"🚀 Executing command: {command}")

        if command == "check-db":
            from core.db import engine
            print("✅ Database connection verified.")
            backup_logger.info("✅ Database connection verified successfully.")

        elif command == "risk-check":
            from risk_assessment.scanner import system_scan
            from risk_assessment.report_generator import generate_report

            print("\n🚀 Starting system risk assessment...\n")
            vulnerabilities = system_scan()
            generate_report(vulnerabilities)
            print("✅ Risk assessment completed.\n")
            backup_logger.info("✅ Risk assessment completed successfully.")

        elif command == "verify-backups":
            from backup_manager.verifier import verify_backups
            verify_backups()
            backup_logger.info("✅ Backup verification completed successfully.")

        elif command == "local-backup":
            run_local_backup()
            backup_logger.info("✅ Local backup executed successfully.")

        elif command == "cloud-backup":
            run_cloud_backup()
            backup_logger.info("✅ Cloud backup executed successfully.")

        elif command == "backup-status":
            check_backup_status()
            backup_logger.info("✅ Backup status check completed successfully.")

        elif command == "monitor-backups":
            backup_dir = os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', 'backups', 'local')
            )
            backup_logger.info(f"🛡️ Starting backup monitoring in: {backup_dir}")

            monitor_backups(
                backup_dir,
                interval=interval,
                max_checks=max_checks
            )

        # 🚨 Phishing Simulation
        elif command == "phish-sim":
            print("\n🚨 Simulating a phishing attack...\n")
            send_email()
            track_phishing_clicks()
            print("✅ Phishing simulation completed.\n")
            backup_logger.info("✅ Phishing simulation executed successfully.")

        # 🔄 Phishing Recovery - Use failover_handler to restore backup
        elif command == "phish-recover":
            print("\n🔐 Recovering from phishing attack and restoring backup...\n")

            # ✅ Call initiate_failover() for backup recovery
            initiate_failover()

            print("✅ Phishing recovery completed successfully!\n")
            backup_logger.info("✅ Phishing recovery executed successfully.")

        # 🔄 Ransomware Attack - Monitor and Encrypt ZIP Files in Downloads
        elif command == "ransom-attack":
            print("\n💀 Launching a ransomware attack...\n")

            # Monitor and encrypt .zip files in Downloads
            monitor_downloads()

            print("❌ Your files have been encrypted! Read the ransom note.\n")
            backup_logger.critical("❌ Ransomware attack executed!")

        # 🔓 Ransomware Recovery
        elif command == "ransom-recover":
            print("\n🔓 Recovering encrypted files...\n")

            # ✅ Run decrypt_file to restore encrypted data
            decrypt_file("local_backup.zip")  # Pass encrypted path
            print("✅ Ransomware recovery completed.\n")
            backup_logger.info("✅ Ransomware recovery executed successfully.")

        # 🔄 Disaster Recovery using Failover Handler
        elif command == "disaster-recover":
            print("\n🛠️ Initiating disaster recovery...\n")

            # ✅ Call initiate_failover for failover after disaster
            initiate_failover()

            print("✅ Disaster recovery completed.\n")
            backup_logger.info("✅ Disaster recovery executed successfully.")

        else:
            print(f"❌ Unknown command: {command}")
            backup_logger.warning(f"⚠️ Unknown command attempted: {command}")

    except Exception as e:
        error_logger.error(f"❌ Error while executing command '{command}': {e}")
        print(f"❌ Error: {e}")


def main_loop():
    """Main CLI loop that keeps running until user exits."""
    while True:
        show_menu()
        choice = input().strip()

        # Mapping user input to commands
        commands_map = {
            "1": "check-db",
            "2": "risk-check",
            "3": "verify-backups",
            "4": "local-backup",
            "5": "cloud-backup",
            "6": "backup-status",
            "7": "monitor-backups",
            "8": "phish-sim",
            "9": "phish-recover",
            "10": "ransom-attack",
            "11": "ransom-recover",
            "12": "disaster-recover",
            "0": "exit"
        }

        if choice in commands_map:
            command = commands_map[choice]

            if command == "exit":
                print("\n👋 Exiting Disaster Recovery CLI. Goodbye!")
                backup_logger.info("👋 CLI session terminated by user.")
                break
            else:
                run_command(command)
        else:
            print("❌ Invalid choice! Please choose a valid option.\n")


if __name__ == "__main__":
    main_loop()
