from database import db
class Calendar(db.Model):
    __tablename__ = "calendar"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
