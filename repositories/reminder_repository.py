from models.reminder import Reminder
from database import db
from datetime import datetime

def getAll():
    return Reminder.query.all()

def getById(id: int):
    return Reminder.query.get(id)

def create(data):
    reminder = Reminder(
        task_id=data["task_id"],
        notify_at=data["notify_at"],
        type=data["type"]
    )
    db.session.add(reminder)
    db.session.commit()
    return reminder

def update(id: int, data):
    reminder = getById(id)
    if not reminder:
        return None

    reminder.task_id = data.get("task_id", reminder.task_id)
    reminder.notify_at = data.get("notify_at", reminder.notify_at)
    reminder.type = data.get("type", reminder.type)

    db.session.commit()
    return reminder

def delete(id: int):
    reminder = getById(id)
    if not reminder:
        return False

    db.session.delete(reminder)
    db.session.commit()
    return True

def getPendingBetween(start, end):
    return Reminder.query.filter(
        Reminder.sent == False,
        Reminder.notify_at >= start,
        Reminder.notify_at <= end
    ).all()
