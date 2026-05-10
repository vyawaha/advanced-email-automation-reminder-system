from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

scheduler = BackgroundScheduler()


def schedule_email(send_function, run_time, args=[]):

    scheduler.add_job(
        send_function,
        'date',
        run_date=run_time,
        args=args
    )


def start_scheduler():
    scheduler.start()
    print("Scheduler Started")