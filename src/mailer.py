import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, DRY_RUN


class Mailer:

    async def send_email(self, to_email, subject, body):

        if DRY_RUN:
            print(f"[DRY RUN] Email simulated to {to_email}")
            return {
                "status": "dry-run-success"
            }

        message = MIMEMultipart()
        message["From"] = SMTP_USER
        message["To"] = to_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        try:
            smtp = aiosmtplib.SMTP(
                hostname=SMTP_HOST,
                port=SMTP_PORT,
                use_tls=True
            )

            await smtp.connect()
            await smtp.login(SMTP_USER, SMTP_PASS)
            await smtp.send_message(message)
            await smtp.quit()

            return {
                "status": "success"
            }

        except Exception as e:
            return {
                "status": "failed",
                "error": str(e)
            }