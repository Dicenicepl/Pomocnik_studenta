import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for, Response, jsonify
import io
import csv

grades_bp = Blueprint(
    'grades',
    __name__,
    url_prefix='/grades',
    template_folder='templates'
)

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            value REAL NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS pomodoro (
            date TEXT PRIMARY KEY,
            minutes INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def calculate_average(grades):
    if not grades: return 0.0
    return round(sum(grades) / len(grades), 2)

@grades_bp.route('/')
def grades_page():
    conn = get_db()
    rows = conn.execute('SELECT * FROM grades').fetchall()
    conn.close()

    subjects_list = [
        "Budowa i analiza algorytmów",
        "Organizacja i architektura systemów",
        "Matematyka I",
        "Podstawy programowania Python",
        "Arkusze kalkulacyjne",
        "Język obcy"
    ]

    view_data = {subject: {'grades': [], 'average': 0.0} for subject in subjects_list}
    all_grades = []

    for row in rows:
        subject = row['subject']
        value = row['value']
        if subject in view_data:
            view_data[subject]['grades'].append(value)
            all_grades.append(value)
    test = 0.0
    for subject in view_data:
        temp_avg = calculate_average(view_data[subject]['grades'])
        view_data[subject]['average'] = temp_avg
        test += temp_avg


    # srednia_ogolna = calculate_average(wszystkie_oceny)
    overall_average = round(test/6, 2)

    count_fives = all_grades.count(5.0)
    count_twos = all_grades.count(2.0)
    total_count = len(all_grades)

    return render_template(
        'grades.html',
        gradebook=view_data,
        overall_average=overall_average,
        count_fives=count_fives,
        count_twos=count_twos,
        total_count=total_count
    )

@grades_bp.route('/add', methods=['POST'])
def add_grade():
    try:
        subject = request.form.get('subject')
        grade = float(request.form.get('grade').replace(',', '.'))
        if 2.0 <= grade <= 5.0:
            conn = get_db()
            conn.execute('INSERT INTO grades (subject, value) VALUES (?, ?)', (subject, grade))
            conn.commit()
            conn.close()
    except:
        pass
    return redirect(url_for('grades.grades_page'))

@grades_bp.route('/delete/<subject>/<int:index>')
def delete_grade(subject, index):
    conn = get_db()
    rows = conn.execute('SELECT id FROM grades WHERE subject = ?', (subject,)).fetchall()
    if 0 <= index < len(rows):
        grade_id = rows[index]['id']
        conn.execute('DELETE FROM grades WHERE id = ?', (grade_id,))
        conn.commit()
    conn.close()
    return redirect(url_for('grades.grades_page'))

@grades_bp.route('/export')
def export_csv():
    conn = get_db()
    rows = conn.execute('SELECT * FROM grades').fetchall()
    conn.close()

    data = {}

    for row in rows:
        subject = row['subject']
        if subject not in data:
            data[subject] = []
        data[subject].append(row['value'])

    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')
    writer.writerow(['Przedmiot', 'Oceny', 'Srednia'])

    for subject, grades_list in data.items():
        avg = calculate_average(grades_list)
        grades_str = ", ".join([str(g) for g in grades_list])
        writer.writerow([subject, grades_str, avg])

    return Response('\ufeff' + output.getvalue(),
                    mimetype="text/csv",
                    headers={"Content-disposition": "attachment; filename=grades.csv"})