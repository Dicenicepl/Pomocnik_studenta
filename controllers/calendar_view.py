from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from services import calendar_service

calendar_view = Blueprint("calendar_view", __name__)

@calendar_view.get("/calendar")
def calendar_page():
    response, _ = calendar_service.getAllEvents()
    events = response.json
    return render_template("calendar.html", events=events)


@calendar_view.post("/calendar/create")
def create_event():
    data = {
        "title": request.form["title"],
        "type": request.form["type"],
        "start": datetime.strptime(
            request.form["start"], "%Y-%m-%dT%H:%M"
        ),
        "end": datetime.strptime(
            request.form["end"], "%Y-%m-%dT%H:%M"
        ),
        "location": request.form["location"],
        "description": request.form["description"]
    }

    calendar_service.createEvent(data)
    return redirect(url_for("calendar_view.calendar_page"))


@calendar_view.post("/calendar/update/<int:id>")
def update_event(id: int):
    data = {
        "title": request.form["title"],
        "type": request.form["type"],
        "start": datetime.strptime(
            request.form["start"], "%Y-%m-%dT%H:%M"
        ),
        "end": datetime.strptime(
            request.form["end"], "%Y-%m-%dT%H:%M"
        ),
        "location": request.form["location"],
        "description": request.form["description"]
    }

    calendar_service.updateEvent(id, data)
    return redirect(url_for("calendar_view.calendar_page"))


@calendar_view.post("/calendar/delete/<int:id>")
def delete_event(id: int):
    calendar_service.deleteEvent(id)
    return redirect(url_for("calendar_view.calendar_page"))
