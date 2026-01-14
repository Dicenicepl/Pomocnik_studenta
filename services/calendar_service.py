from flask import jsonify
from models.calendar import Calendar
from repositories import calendar_repository


def getAllEvents():
    events = calendar_repository.getAll()

    return jsonify([
        eventToJson(e) for e in events
    ]), 200


def getEventById(id: int):
    event = calendar_repository.getById(id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    return jsonify(eventToJson(event)), 200


def createEvent(data):
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    required = ["title", "type", "start", "end", "location", "description"]
    missing = [f for f in required if f not in data]

    if missing:
        return jsonify({
            "error": "Missing fields",
            "fields": missing
        }), 400

    event = Calendar(
        title=data["title"],
        type=data["type"],
        start=data["start"],
        end=data["end"],
        location=data["location"],
        description=data["description"]
    )

    calendar_repository.create(event)

    return jsonify(eventToJson(event)), 201


def updateEvent(id: int, data: dict):
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    event = calendar_repository.update(id, data)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    return jsonify(eventToJson(event)), 200


def deleteEvent(id: int):
    success = calendar_repository.delete(id)
    if not success:
        return jsonify({"error": "Event not found"}), 404

    return "", 204


def eventToJson(event: Calendar):
    return {
        "id": event.id,
        "title": event.title,
        "type": event.type,
        "start": event.start,
        "end": event.end,
        "location": event.location,
        "description": event.description
    }
