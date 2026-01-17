from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from services import reminder_service
from repositories import reminder_repository
from database import db

reminders_bp = Blueprint("reminders", __name__, url_prefix="/api/reminders")

@reminders_bp.get("/")
def get_all():
    return reminder_service.getAllReminders()

@reminders_bp.post("/")
def create():
    return reminder_service.createReminder(request.json)

@reminders_bp.put("/<int:id>")
def update(id):
    return reminder_service.updateReminder(id, request.json)

@reminders_bp.delete("/<int:id>")
def delete(id):
    return reminder_service.deleteReminder(id)

@reminders_bp.get("/check")
def check():
    now = datetime.now()
    future = now + timedelta(minutes=5)

    reminders = reminder_repository.getPendingBetween(now, future)

    result = []
    for r in reminders:
        result.append({
            "id": r.id,
            "task_id": r.task_id,
            "notify_at": r.notify_at.isoformat(),
            "type": r.type
        })
        r.sent = True
    db.session.commit()
    return jsonify(result), 200