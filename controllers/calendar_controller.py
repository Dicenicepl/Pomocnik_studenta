from flask import Blueprint, request
from services import calendar_service

calendar_bp = Blueprint("calendar", __name__, url_prefix="/api/calendar/events")

@calendar_bp.get("/")
def getAllEvents():
    return calendar_service.getAllEvents()

@calendar_bp.get("/<int:id>")
def getEventById(id:int):
    return calendar_service.getEventById(id)

@calendar_bp.post("/")
def createEvent():
    data = request.json
    return calendar_service.createEvent(data)

@calendar_bp.put("/<int:id>")
def updateEvent(id:int):
    data = request.json
    return calendar_service.updateEvent(id, data)

@calendar_bp.delete("/<int:id>")
def deleteEvent(id:int):
    return calendar_service.deleteEvent(id)