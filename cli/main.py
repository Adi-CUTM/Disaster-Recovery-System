# import argparse
# from .commands import run_command

# def main():
#     parser = argparse.ArgumentParser(description="🚀 Disaster Recovery CLI Tool")
#     parser.add_argument(
#         "command",
#         help="The command to execute",
#         choices=[
#             "check-db",
#             "risk-check",
#             "verify-backups",
#             "local-backup",
#             "cloud-backup",
#             "backup-status",
#             "monitor-backups"
#         ]
#     )
#     parser.add_argument("--interval", type=int, help="Interval between monitoring checks (seconds)", default=300)
#     parser.add_argument("--max-checks", type=int, help="Maximum number of monitoring checks", default=None)

#     args = parser.parse_args()

#     run_command(
#         args.command,
#         interval=args.interval,
#         max_checks=args.max_checks
#     )

# if __name__ == "__main__":
#     main()


import argparse
import time
import sys
from cli.commands import run_command

# ✅ Welcome Banner
def show_banner():
    print("\n" + "=" * 50)
    print("🚀 Welcome to the Disaster Recovery CLI Tool")
    print("🛠️  Manage, Monitor, and Recover from Disasters")
    print("=" * 50 + "\n")

# ✅ Interactive Menu
def show_menu():
    print("📌 What would you like to do today?")
    options = [
        "1️⃣  Check Database Status (check-db)",
        "2️⃣  Perform Risk Assessment (risk-check)",
        "3️⃣  Verify Backups (verify-backups)",
        "4️⃣  Create Local Backup (local-backup)",
        "5️⃣  Backup to Cloud (cloud-backup)",
        "6️⃣  View Backup Status (backup-status)",
        "7️⃣  Monitor Backups (monitor-backups)",
        "8️⃣  Simulate Phishing Attack (phish-sim)",
        "9️⃣  Recover from Phishing (phish-recover)",
        "🔟  Launch Ransomware Attack (ransom-attack)",
        "1️⃣1️⃣  Recover from Ransomware (ransom-recover)",
        "❌ Exit"
    ]

    for option in options:
        print(option)

    while True:
        choice = input("\n👉 Enter your choice (1-11): ").strip()
        
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 11:
                return choice
        print("⚠️ Invalid choice! Please enter a valid number (1-11).")

# ✅ Main Loop - Keeps Running After Each Command
def main_loop():
    show_banner()
    
    while True:
        choice = show_menu()
        command_map = {
            1: "check-db",
            2: "risk-check",
            3: "verify-backups",
            4: "local-backup",
            5: "cloud-backup",
            6: "backup-status",
            7: "monitor-backups",
            8: "phish-sim",
            9: "phish-recover",
            10: "ransom-attack",
            11: "ransom-recover"
        }

        command = command_map.get(choice)

        if command:
            print(f"\n⏳ Running command: {command}...\n")
            time.sleep(1)  # Simulate a short delay before execution
            run_command(command)

        # ✅ Automatically go back to the menu after completing a task
        print("\n✅ Task completed! Returning to the main menu...\n")
        time.sleep(1)

if __name__ == "__main__":
    main_loop()
