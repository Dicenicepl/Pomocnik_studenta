from flask import Flask, render_template, request, jsonify, abort
from database import db
from models import Note

app = Flask(__name__)

# ===== DATABASE CONFIG =====
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# ===== HTML ROUTES =====
@app.route("/")
def main_page():
    return render_template("Main_page.html")

@app.route("/tasks")
def tasks():
    return render_template("Tasks.html")

@app.route("/calendar")
def calendar():
    return render_template("Calendar.html")

@app.route("/notes")
def notes():
    return render_template("Notes.html")

@app.route("/pomodoro")
def pomodoro():
    return render_template("Pomodoro.html")

@app.route("/reminders")
def reminders():
    return render_template("Reminders.html")

@app.route("/notifications")
def notifications():
    return render_template("Notifications.html")

@app.route("/settings")
def settings():
    return render_template("Settings.html")

@app.route("/fast-urls")
def fast_urls():
    return render_template("Fast_URLs.html")

@app.route("/grades")
def grades():
    return render_template("Grades_ECTS_points.html")

@app.route("/backup")
def backup():
    return render_template("Backup_data_export.html")

# ===== API: NOTES =====
@app.route("/api/notes", methods=["GET"])
def api_get_notes():
    notes = Note.query.all()
    return jsonify([note.to_dict() for note in notes])

@app.route("/api/notes", methods=["POST"])
def api_create_note():
    data = request.get_json(force=True)

    if not data or "title" not in data or "content" not in data:
        abort(400)

    note = Note(
        title=data["title"],
        content=data["content"],
        format=data.get("format", "markdown")
    )

    db.session.add(note)
    db.session.commit()

    return jsonify(note.to_dict()), 201

@app.route("/api/notes/<int:id>", methods=["PUT"])
def api_update_note(id):
    note = Note.query.get_or_404(id)
    data = request.get_json(force=True)  

    if not data:
        abort(400)

    note.title = data.get("title", note.title)
    note.content = data.get("content", note.content)
    note.format = data.get("format", note.format)

    db.session.commit()
    return jsonify(note.to_dict())


@app.route("/api/notes/<int:id>", methods=["DELETE"])
def api_delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({"message": "Note deleted"})

if __name__ == "__main__":
    app.run(debug=True)
