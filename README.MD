# 🛡️ Disaster Recovery System

This project simulates a **cybersecurity incident**—specifically a **phishing email carrying a ransomware payload**—to test the effectiveness of a disaster recovery strategy involving both **local and cloud backups**.

## 📌 Project Overview

In real-world environments, organizations face the constant threat of cyber attacks, including phishing and ransomware. This project demonstrates a proactive disaster recovery solution that includes:

- Simulation of a phishing email leading to a ransomware infection
- Local system backup
- Cloud-based backup using **Amazon S3**
- Automated recovery mechanism from both sources in case of attack

---

## 🚀 Features

- 📧 **Phishing Attack Simulation**  
  Demonstrates how a ransomware payload can be delivered through a phishing email and infect the system.

- 🔐 **Ransomware Payload Execution**  
  Simulates encryption of files to mimic real-world ransomware behavior.

- 💾 **Local Backup System**  
  Creates regular backups of critical directories/files locally before attack simulation.

- ☁️ **Cloud Backup via AWS S3**  
  Uses Amazon S3 bucket to upload backups automatically for offsite storage and recovery.

- ♻️ **Disaster Recovery Flow**  
  Allows recovery of files either from local backup or AWS S3 after ransomware attack is detected.

---



## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- AWS CLI configured or AWS credentials in `.aws/credentials`
- IAM user with S3 write access
- `boto3`, `argparse`, `cryptography`, and other required libraries (listed in `requirements.txt`)

### 📦 Installation

```bash
git clone https://github.com/Adi-CUTM/Disaster-Recovery-System.git
cd disaster-recovery-system



🛑 Simulate Attack

python -m cli.main 
This command simulates a phishing email and ransomware encryption on target files.

