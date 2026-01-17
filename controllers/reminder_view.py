from flask import Blueprint, render_template, request, redirect, url_for
from services import reminder_service

reminder_view = Blueprint("reminder_view", __name__, url_prefix="/reminders")

@reminder_view.get("/")
def page():
    reminders = reminder_service.getAllReminders()[0].json
    return render_template("reminders.html", reminders=reminders)

@reminder_view.post("/create")
def create():
    data = {
        "task_id": request.form["task_id"],
        "notify_at": request.form["notify_at"],
        "type": request.form["type"]
    }
    reminder_service.createReminder(data)
    return redirect(url_for("reminder_view.page"))

@reminder_view.post("/delete/<int:id>")
def delete(id):
    reminder_service.deleteReminder(id)
    return redirect(url_for("reminder_view.page"))
