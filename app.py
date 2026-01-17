from flask import Flask

from database import db
from models.note import Note
from models.link import Link
from models.calendar import Calendar

from controllers.links_controller import links_bp
from controllers.links_view import links_view
from controllers.notes_controller import notes_bp
from controllers.calendar_controller import calendar_bp
from controllers.calendar_view import calendar_view
from pomodoro import pomodoro_bp
from grades import grades_bp

app = Flask(__name__)

#URI where to read/create .db file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db.init_app(app)

#Registering outsite controllers
app.register_blueprint(links_bp)
app.register_blueprint(links_view)
app.register_blueprint(notes_bp)
app.register_blueprint(calendar_bp)
app.register_blueprint(calendar_view)
app.register_blueprint(pomodoro_bp)
app.register_blueprint(grades_bp)


#Create all imported tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
