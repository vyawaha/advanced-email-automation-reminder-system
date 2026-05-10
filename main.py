import asyncio
from src.worker import process_reminders


if __name__ == "__main__":
    asyncio.run(process_reminders())