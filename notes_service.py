from models import db, Note

def get_all_notes():
    return Note.query.all()

def create_note(title, content, format="markdown"):
    note = Note(title=title, content=content, format=format)
    db.session.add(note)
    db.session.commit()
    return note

def update_note(note, title, content, format):
    note.title = title
    note.content = content
    note.format = format
    db.session.commit()
    return note

def delete_note(note):
    db.session.delete(note)
    db.session.commit()
