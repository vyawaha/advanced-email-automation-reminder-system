import asyncio
from datetime import datetime

from src.csv_loader import load_contacts, load_reminders
from src.renderer import render_template
from src.mailer import Mailer
from src.report_generator import generate_report
from src.logger_config import logger


async def process_reminders():

    logger.info("===== EMAIL AUTOMATION WORKER STARTED =====")

    contacts = load_contacts()
    reminders = load_reminders()

    mailer = Mailer()
    results = []

    for _, reminder in reminders.iterrows():

        contact = contacts[
            contacts['email'] == reminder['contact_email']
        ]

        if contact.empty:
            logger.warning(f"Contact not found: {reminder['contact_email']}")
            continue

        contact_data = contact.iloc[0]

        context = {
            "name": contact_data['name'],
            "title": reminder['title'],
            "date": reminder['date'],
            "time": reminder['time']
        }

        body = render_template(
            "templates/reminder_template.md",
            context
        )

        logger.info(f"Sending email to {reminder['contact_email']}")

        response = await mailer.send_email(
            reminder['contact_email'],
            reminder['title'],
            body
        )

        logger.info(f"Status: {response['status']} | {reminder['contact_email']}")

        results.append({
            "email": reminder['contact_email'],
            "title": reminder['title'],
            "status": response['status'],
            "timestamp": str(datetime.now())
        })

        print(f"Processed: {reminder['contact_email']}")

    generate_report(results)

    logger.info("Report generated successfully")
    logger.info("===== EMAIL AUTOMATION WORKER COMPLETED =====")