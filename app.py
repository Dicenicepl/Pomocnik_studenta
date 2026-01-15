from flask import Flask, redirect
from grades import grades_bp
from pomodoro import pomodoro_bp

app = Flask(__name__)

app.register_blueprint(grades_bp)
app.register_blueprint(pomodoro_bp)

@app.route('/')
def index():
    return redirect('/grades/')

if __name__ == '__main__':
    app.run(debug=True)
