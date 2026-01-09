from database import db
class Link(db.Model):
    __tablename__ = "links"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    icon = db.Column(db.String)