from database import db
from datetime import datetime

class Reminder(db.Model):
    __tablename__ = "reminders"

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, nullable=False)
    notify_at = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String, nullable=False)
    sent = db.Column(db.Boolean, default=False)
