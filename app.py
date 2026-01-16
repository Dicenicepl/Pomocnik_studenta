from flask import Flask, render_template

from database import db
from models.note import Note
from models.calendar import Calendar
from models.link import Link


from controllers.links_controller import links_bp

app = Flask(__name__)

@app.get("/")
def dashboard():
    return render_template("Dashboard.html")

#URI where to read/create .db file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db.init_app(app)

#Registering outsite controllers
app.register_blueprint(links_bp)

#Create all imported tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host="192.168.1.189")
