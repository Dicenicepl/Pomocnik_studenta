# 📚 System Organizacji Nauki – API (Flask)

Lekki, lokalny system do organizacji nauki i codziennych obowiązków, zbudowany w **Python Flask**. Projekt działa w trybie **single-user**, bez autoryzacji, z wykorzystaniem **SQLite** jako bazy danych.

Idealny jako backend do aplikacji webowej / desktopowej / mobilnej (np. React, Vue, MAUI, Electron).

---

## 🚀 Funkcje

* 📆 Kalendarz wydarzeń (zajęcia, egzaminy, spotkania)
* ✅ Zadania i projekty z priorytetami
* ⏰ Przypomnienia
* 🔗 Szybkie linki (np. Teams, Moodle, GitHub)
* 📝 Notatki (różne formaty)
* 🎓 Oceny i punkty ECTS + statystyki
* 🍅 Pomodoro (timer + statystyki)
* 🎨 Ustawienia aplikacji
* 💾 Backup i eksport danych

---

## 🛠️ Stack technologiczny

* **Backend:** Flask (Python)
* **Baza danych:** SQLite
* **Format danych:** JSON
* **Architektura:** REST API
* **Autoryzacja:** brak (lokalne, single-user)

---

## 🌐 Informacje ogólne API

* **Prefix:** `/api`
* **Format:** `application/json`
* **Tryb:** lokalny

---

## 📆 Kalendarz

**Endpointy:**

* `GET /api/calendar/events` – lista wydarzeń
  *query:* `date`, `view`
* `POST /api/calendar/events` – dodanie wydarzenia
* `GET /api/calendar/events/{id}` – szczegóły wydarzenia
* `PUT /api/calendar/events/{id}` – edycja
* `DELETE /api/calendar/events/{id}` – usunięcie

**Model Event:**

```json
{
  "title": "Math exam",
  "type": "exam",
  "start": "2026-01-10T10:00",
  "end": "2026-01-10T12:00",
  "location": "Room 204",
  "description": "Final exam"
}
```

---

## ✅ Zadania i projekty

**Endpointy:**

* `GET /api/tasks`
* `POST /api/tasks`
* `PUT /api/tasks/{id}`
* `DELETE /api/tasks/{id}`

**Model Task:**

```json
{
  "title": "Projekt Flask",
  "priority": "high",
  "due_date": "2026-01-20",
  "completed": false
}
```

---

## ⏰ Przypomnienia

**Endpointy:**

* `GET /api/reminders`
* `POST /api/reminders`
* `PUT /api/reminders/{id}`
* `DELETE /api/reminders/{id}`

**Model Reminder:**

```json
{
  "task_id": 1,
  "notify_at": "2026-01-19T18:00",
  "type": "push"
}
```

---

## 🔗 Szybkie linki

**Endpointy:**

* `GET /api/links`
* `POST /api/links`
* `PUT /api/links/{id}`
* `DELETE /api/links/{id}`

**Model Link:**

```json
{
  "name": "Moodle",
  "url": "https://moodle.edu",
  "icon": "school"
}
```

---

## 📝 Notatki

**Endpointy:**

* `GET /api/notes`
* `POST /api/notes`
* `PUT /api/notes/{id}`
* `DELETE /api/notes/{id}`

**Model Note:**

```json
{
  "title": "Wzory z fizyki",
  "format": "markdown",
  "content": "## Dynamika\nF = m * a"
}
```

---

## 🎓 Oceny i ECTS

**Endpointy:**

* `GET /api/grades`
* `POST /api/grades`
* `DELETE /api/grades/{id}`
* `GET /api/grades/average`
* `GET /api/grades/ects`
* `GET /api/grades/export?format=csv`

**Model Grade:**

```json
{
  "subject": "Matematyka",
  "grade": 4.5,
  "ects": 6
}
```

---

## 🍅 Pomodoro

**Endpointy:**

* `POST /api/pomodoro/start`
* `POST /api/pomodoro/stop`
* `POST /api/pomodoro/reset`
* `GET /api/pomodoro/stats`

---

## 🎨 Ustawienia

**Endpointy:**

* `GET /api/settings`
* `PUT /api/settings`

**Model Settings:**

```json
{
  "theme": "dark",
  "notifications": true,
  "avatar": "default.png"
}
```

---

## 💾 Backup i eksport

**Endpointy:**

* `POST /api/backup/create`
* `POST /api/backup/restore`
* `GET /api/export/json`
* `GET /api/export/db`

## 📄 Licencja

MIT – używaj, modyfikuj i rozwijaj bez ograniczeń.

---

> ✨ Idealny projekt do nauki Flask, REST API i architektury aplikacji backendowej.
