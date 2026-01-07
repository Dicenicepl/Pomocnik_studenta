Dokumentacja API – System Organizacji Nauki (Flask, bez auth)
1. Informacje ogólne
API zaprojektowane dla lokalnej aplikacji webowej opartej o Flask.
Brak autoryzacji (single-user, lokalna baza SQLite).
Format danych: JSON
Prefix API: /api
2. Kalendarz
GET /api/calendar/events – lista wydarzeń (query: date, view)
POST /api/calendar/events – dodanie wydarzenia
GET /api/calendar/events/{id}
PUT /api/calendar/events/{id}
DELETE /api/calendar/events/{id}

Event:
{ title, type, start, end, location, description }
3. Zadania i projekty
GET /api/tasks
POST /api/tasks
PUT /api/tasks/{id}
DELETE /api/tasks/{id}

Task:
{ title, priority, due_date, completed }
4. Przypomnienia
GET /api/reminders
POST /api/reminders
PUT /api/reminders/{id}
DELETE /api/reminders/{id}

Reminder:
{ task_id, notify_at, type }
5. Szybkie linki
GET /api/links
POST /api/links
PUT /api/links/{id}
DELETE /api/links/{id}

Link:
{ name, url, icon, shortcut }
6. Notatki
GET /api/notes
POST /api/notes
PUT /api/notes/{id}
DELETE /api/notes/{id}

Note:
{ title, format, content }
7. Oceny i ECTS
GET /api/grades
POST /api/grades
DELETE /api/grades/{id}
GET /api/grades/average
GET /api/grades/ects
GET /api/grades/export?format=csv

Grade:
{ subject, grade, ects }
8. Pomodoro
POST /api/pomodoro/start
POST /api/pomodoro/stop
POST /api/pomodoro/reset
GET /api/pomodoro/stats
9. Ustawienia
GET /api/settings
PUT /api/settings

Settings:
{ theme, notifications, avatar }
10. Backup
POST /api/backup/create
POST /api/backup/restore
GET /api/export/json
GET /api/export/db
