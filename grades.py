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

DATABASE = 'baza.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS oceny (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            przedmiot TEXT NOT NULL,
            wartosc REAL NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS pomodoro (
            data TEXT PRIMARY KEY,
            minuty INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def calculate_average(grades):
    if not grades: return 0.0
    # print(grades)
    # print(sum(grades))
    # print(len(grades))
    # print(sum(grades) / len(grades))
    return round(sum(grades) / len(grades), 2)

@grades_bp.route('/')
def grades_page():
    conn = get_db()
    rows = conn.execute('SELECT * FROM oceny').fetchall()
    conn.close()

    przedmioty_lista = [
        "Budowa i analiza algorytmów", "Organizacja i architektura systemów",
        "Matematyka I", "Podstawy programowania Python",
        "Arkusze kalkulacyjne", "Język obcy"
    ]

    view_data = {p: {'oceny': [], 'srednia': 0.0} for p in przedmioty_lista}
    wszystkie_oceny = []

    for row in rows:
        p = row['przedmiot']
        val = row['wartosc']
        if p in view_data:
            view_data[p]['oceny'].append(val)
            wszystkie_oceny.append(val)

    for p in view_data:
        view_data[p]['srednia'] = calculate_average(view_data[p]['oceny'])

    srednia_ogolna = calculate_average(wszystkie_oceny)
    ilosc_piatek = wszystkie_oceny.count(5.0)
    ilosc_dwoj = wszystkie_oceny.count(2.0)
    laczna_ilosc = len(wszystkie_oceny)

    return render_template(
        'grades.html',
        dziennik=view_data,
        srednia_ogolna=srednia_ogolna,
        ilosc_piatek=ilosc_piatek,
        ilosc_dwoj=ilosc_dwoj,
        laczna_ilosc=laczna_ilosc
    )

@grades_bp.route('/dodaj', methods=['POST'])
def add_grade():
    try:
        subject = request.form.get('przedmiot')
        grade = float(request.form.get('ocena').replace(',', '.'))
        if 2.0 <= grade <= 5.0:
            conn = get_db()
            conn.execute('INSERT INTO oceny (przedmiot, wartosc) VALUES (?, ?)', (subject, grade))
            conn.commit()
            conn.close()
    except:
        pass
    return redirect(url_for('grades.grades_page'))

@grades_bp.route('/usun/<subject>/<int:index>')
def delete_grade(subject, index):
    conn = get_db()
    rows = conn.execute('SELECT id FROM oceny WHERE przedmiot = ?', (subject,)).fetchall()
    if 0 <= index < len(rows):
        grade_id = rows[index]['id']
        conn.execute('DELETE FROM oceny WHERE id = ?', (grade_id,))
        conn.commit()
    conn.close()
    return redirect(url_for('grades.grades_page'))

@grades_bp.route('/export')
def export_csv():
    conn = get_db()
    rows = conn.execute('SELECT * FROM oceny').fetchall()
    conn.close()

    data = {}
    for row in rows:
        p = row['przedmiot']
        if p not in data: data[p] = []
        data[p].append(row['wartosc'])

    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')
    writer.writerow(['Przedmiot', 'Oceny', 'Srednia'])

    for subject, grades in data.items():
        avg = calculate_average(grades)
        grades_str = ", ".join([str(g) for g in grades])
        writer.writerow([subject, grades_str, avg])

    return Response('\ufeff' + output.getvalue(),
                    mimetype="text/csv",
                    headers={"Content-disposition": "attachment; filename=oceny.csv"})
