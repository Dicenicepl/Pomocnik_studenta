from flask import Flask
from database import db
from controllers.links_controller import links_bp

app = Flask(__name__)

#Registering outsite controllers
app.register_blueprint(links_bp)

#URI where to read/create .db file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db.init_app(app)

#Create all imported tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)