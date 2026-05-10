from PIL import Image, ImageDraw, ImageFont
import os

# -----------------------------
# OUTPUT FOLDER
# -----------------------------
os.makedirs("images", exist_ok=True)

# -----------------------------
# FONT SETTINGS (LARGE + READABLE)
# -----------------------------
try:
    TITLE_FONT = ImageFont.truetype("arial.ttf", 65)
    TEXT_FONT = ImageFont.truetype("arial.ttf", 45)
except:
    TITLE_FONT = ImageFont.load_default()
    TEXT_FONT = ImageFont.load_default()


def create_image(filename, title, lines):

    img = Image.new("RGB", (1700, 950), color=(15, 15, 15))
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((60, 50), title, fill=(0, 255, 200), font=TITLE_FONT)

    y = 180

    for line in lines:
        draw.text((80, y), line, fill=(255, 255, 255), font=TEXT_FONT)
        y += 75

    img.save(f"images/{filename}")


# -----------------------------
# PROJECT STRUCTURE
# -----------------------------
create_image(
    "project_structure.png",
    "Email Automation System Structure",
    [
        "src/ | templates/ | data/",
        "outputs/ | logs/ | images/",
        "FastAPI + SMTP + APScheduler",
        "Production Python Project"
    ]
)

# -----------------------------
# CONTACTS
# -----------------------------
create_image(
    "contacts_csv.png",
    "Contacts CSV",
    [
        "Rahul Sharma | rahul@example.com",
        "Priya Singh | priya@example.com",
        "Aman Verma | aman@example.com"
    ]
)

# -----------------------------
# REMINDERS
# -----------------------------
create_image(
    "reminders_csv.png",
    "Reminders CSV",
    [
        "Webinar Reminder | 18:30",
        "Assignment Reminder | 10:00",
        "Payment Reminder | 09:00"
    ]
)

# -----------------------------
# TEMPLATE
# -----------------------------
create_image(
    "template_preview.png",
    "Email Template",
    [
        "Hello {{name}}",
        "Reminder: {{title}}",
        "Date: {{date}}",
        "Time: {{time}}"
    ]
)

# -----------------------------
# TERMINAL OUTPUT
# -----------------------------
create_image(
    "terminal_output.png",
    "Dry Run Output",
    [
        "Processing: rahul@example.com",
        "Status: success",
        "Processing: priya@example.com",
        "Report Generated"
    ]
)

# -----------------------------
# SCHEDULER
# -----------------------------
create_image(
    "scheduler_output.png",
    "Scheduler Engine",
    [
        "APScheduler Started",
        "Jobs Triggered",
        "Emails Dispatched",
        "Execution Completed"
    ]
)

# -----------------------------
# REPORT
# -----------------------------
create_image(
    "report_output.png",
    "Delivery Report",
    [
        "email | status",
        "rahul@example.com | success",
        "priya@example.com | success"
    ]
)

# -----------------------------
# SWAGGER
# -----------------------------
create_image(
    "swagger_ui.png",
    "FastAPI Swagger UI",
    [
        "POST /contacts",
        "POST /templates",
        "POST /reminders",
        "POST /campaigns"
    ]
)

# -----------------------------
# GITHUB
# -----------------------------
create_image(
    "github_repo.png",
    "GitHub Repository",
    [
        "Advanced Email Automation System",
        "FastAPI + SMTP + APScheduler",
        "Production-Level Project"
    ]
)

# -----------------------------
# LOGS (REAL FILE BASED)
# -----------------------------
log_lines = []

try:
    with open("logs/app.log", "r", encoding="utf-8") as f:
        lines = f.readlines()
        log_lines = [line.strip()[:95] for line in lines[-8:]]
except:
    log_lines = [
        "No logs found",
        "Run main.py first",
        "Logs will appear here"
    ]

create_image(
    "logs_preview.png",
    "System Logs (Live Data)",
    log_lines
)

print("All images generated successfully inside images/")