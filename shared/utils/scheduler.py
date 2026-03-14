from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def check_reminders():
    """Check and process pending reminders"""
    from shared.database.models import Reminder
    
    now = datetime.utcnow()
    pending_reminders = Reminder.objects(is_sent=False, scheduled_time__lte=now)
    
    for reminder in pending_reminders:
        # In production, send email or push notification here
        print(f"Reminder: {reminder.message} for user {reminder.user_id}")
        reminder.is_sent = True
        reminder.save()

def start_scheduler(app):
    """Initialize and start the reminder scheduler"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=lambda: app.app_context().push() or check_reminders(),
        trigger="interval",
        minutes=5
    )
    scheduler.start()
    return scheduler
