from database import db
from models.calendar import Calendar

def getAll():
    return Calendar.query.all()

def getById(id: int):
    return Calendar.query.filter(Calendar.id == id).first()

def create(event: Calendar):
    db.session.add(event)
    db.session.commit()
    return event

def update(id: int, data: dict):
    event = getById(id)
    if not event:
        return None

    event.title = data["title"]
    event.type = data["type"]
    event.start = data["start"]
    event.end = data["end"]
    event.location = data["location"]
    event.description = data["description"]

    db.session.commit()
    return event

def delete(id: int):
    event = getById(id)
    if not event:
        return False

    db.session.delete(event)
    db.session.commit()
    return True
