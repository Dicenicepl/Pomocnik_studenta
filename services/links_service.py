from repositories import links_repository
from models.link import Link
from flask import jsonify

def getAllLinks():
    links = links_repository.getAllLinks()
    if not links:
        return jsonify([]), 200

    json = jsonify([
    {
        "id": l.id,
        "name": l.name,
        "url": l.url,
        "icon": l.icon
    } for l in links
    ])
    return json, 200

def getLinkById(id:int):
    link = links_repository.getLinkById(id)
    if not link:
        return "Link not found", 404
    json = jsonify({
        "id": link.id,
        "name": link.name,
        "url": link.url,
        "icon": link.icon
    })
    return json, 200


def createLink(data):
    if "name" not in data or "url" not in data:
        return "Invalid data", 400

    link = links_repository.createLink(data)
    return jsonify({
        "id": link.id,
        "name": link.name,
        "url": link.url,
        "icon": link.icon
    }), 201

def updateLink(id: int, data):
    updated = links_repository.updateLink(id, data)
    if not updated:
        return "Link not found", 404
    return "Updated link", 200


def deleteLink(id: int):
    deleted = links_repository.deleteLink(id)
    if not deleted:
        return "Link not found", 404
    return "Deleted link", 200

