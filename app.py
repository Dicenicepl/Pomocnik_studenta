from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
