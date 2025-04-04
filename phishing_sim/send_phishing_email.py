import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "220301120215@cutm.ac.in"  # Replace with your email
EMAIL_PASSWORD = "jjke dchj ulot iebv"  # If using Gmail, enable App Passwords

RECIPIENT_EMAIL = "220301120215@cutm.ac.in"  # Send to yourself for testing
TRACKING_URL = "http://localhost:5000/clicked"  # Link that triggers backup deletion

def send_email():
    subject = "Important: Click this link for verification"
    body = f"Click the following link to verify: <a href='{TRACKING_URL}'>Click here</a>"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

# ✅ Prevent automatic execution when imported
if __name__ == "__main__":
    send_email()

