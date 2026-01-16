from flask import Blueprint, render_template, request, jsonify
from grades import get_db
from datetime import datetime

pomodoro_bp = Blueprint(
    'pomodoro',
    __name__,
    url_prefix='/pomodoro',
    template_folder='templates'
)

@pomodoro_bp.route('/')
def pomodoro_page():
    conn = get_db()
    rows = conn.execute('SELECT * FROM pomodoro ORDER BY date').fetchall()
    conn.close()

    labels = [row['date'] for row in rows]
    values = [row['minutes'] for row in rows]

    total_minutes = sum(values)
    total_sessions = total_minutes // 5

    return render_template(
        'pomodoro.html',
        labels=labels,
        values=values,
        total_minutes=total_minutes,
        total_sessions=total_sessions
    )

@pomodoro_bp.route('/save', methods=['POST'])
def save_pomodoro():
    data = request.get_json()
    minutes = data.get('minutes', 5)

    today = datetime.now().strftime("%d.%m")

    conn = get_db()
    row = conn.execute('SELECT minutes FROM pomodoro WHERE date = ?', (today,)).fetchone()

    if row:
        conn.execute('UPDATE pomodoro SET minutes = ? WHERE date = ?', (row['minutes'] + minutes, today))
    else:
        conn.execute('INSERT INTO pomodoro (date, minutes) VALUES (?, ?)', (today, minutes))

    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})
