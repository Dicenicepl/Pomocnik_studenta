from flask import jsonify
from repositories import reminder_repository
from datetime import datetime

def reminderToJson(r):
    return {
        "id": r.id,
        "task_id": r.task_id,
        "notify_at": r.notify_at.isoformat(),
        "type": r.type,
        "sent": r.sent
    }

def getAllReminders():
    reminders = reminder_repository.getAll()
    return jsonify([reminderToJson(r) for r in reminders]), 200

def createReminder(data):
    required = ["task_id", "notify_at", "type"]
    if any(k not in data for k in required):
        return jsonify({"error": "Invalid data"}), 400

    data["notify_at"] = datetime.fromisoformat(data["notify_at"])

    reminder = reminder_repository.create(data)
    return jsonify(reminderToJson(reminder)), 201

def updateReminder(id: int, data):
    if "notify_at" in data:
        data["notify_at"] = datetime.fromisoformat(data["notify_at"])

    reminder = reminder_repository.update(id, data)
    if not reminder:
        return jsonify({"error": "Not found"}), 404

    return jsonify(reminderToJson(reminder)), 200

def deleteReminder(id: int):
    if not reminder_repository.delete(id):
        return jsonify({"error": "Not found"}), 404
    return "", 204
