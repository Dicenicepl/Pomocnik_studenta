from flask import Blueprint, request, jsonify, abort
from models.note import Note
from services.notes_service import (
    get_all_notes,
    create_note,
    update_note,
    delete_note
)

notes_bp = Blueprint("notes", __name__)

@notes_bp.route("/api/notes", methods=["GET"])
def api_get_notes():
    notes = get_all_notes()
    return jsonify([note.to_dict() for note in notes])


@notes_bp.route("/api/notes", methods=["POST"])
def api_create_note():
    data = request.get_json()

    if not data or not data.get("title") or not data.get("content"):
        abort(400)

    note = create_note(
        data["title"],
        data["content"],
        data.get("format", "markdown")
    )

    return jsonify(note.to_dict()), 201


@notes_bp.route("/api/notes/<int:id>", methods=["PUT"])
def api_update_note(id):
    note = Note.query.get_or_404(id)
    data = request.get_json()

    note = update_note(
        note,
        data.get("title", note.title),
        data.get("content", note.content),
        data.get("format", note.format)
    )

    return jsonify(note.to_dict())


@notes_bp.route("/api/notes/<int:id>", methods=["DELETE"])
def api_delete_note(id):
    note = Note.query.get_or_404(id)
    delete_note(note)
    return jsonify({"message": "Note deleted"})
