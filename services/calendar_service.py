from flask import jsonify
from repositories import calendar_repository
from models.calendar import Calendar


def getAllEvents():
    events = calendar_repository.getAll()
    if not events:
        return jsonify([]), 200

    json = jsonify([
        {
            "id": e.id,
            "title": e.title,
            "type": e.type,
            "start": e.start,
            "end": e.end,
            "location": e.location,
            "description": e.description
        } for e in events
    ])

    return json, 200


def getEventById(id: int):
    event = calendar_repository.getById(id)
    if not event:
        return "Event not found", 404

    json = jsonify({
        "id": event.id,
        "title": event.title,
        "type": event.type,
        "start": event.start,
        "end": event.end,
        "location": event.location,
        "description": event.description
    })

    return json, 200


def createEvent(data):
    if not data:
        return "Invalid data", 400
    
    if data["end"] <= data["start"]:
        return "Koniec musi być po starcie", 400


    event = Calendar(
    title=data["title"],
    type=data["type"],
    start=data["start"],
    end=data["end"],
    location=data["location"],
    description=data["description"]
    )

    calendar_repository.create(event)

    return jsonify({
        "id": event.id,
        "title": event.title,
        "type": event.type,
        "start": event.start,
        "end": event.end,
        "location": event.location,
        "description": event.description
    }), 201


def updateEvent(id: int, data):
    updated = calendar_repository.update(id, data)
    if not updated:
        return "Event not found", 404

    return "Updated event", 200


def deleteEvent(id: int):
    deleted = calendar_repository.delete(id)
    if not deleted:
        return "Event not found", 404

    return "Deleted event", 200
