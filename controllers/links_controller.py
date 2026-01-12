from flask import Blueprint, request
from services import links_service

links_bp = Blueprint("links", __name__, url_prefix="/api/links")

@links_bp.get("/")
def getAllLinks():
    return links_service.getAllLinks()

@links_bp.get("/<int:id>")
def getLinkById(id:int):
    print("ACTIVE: getLinkById")
    return links_service.getLinkById(id)

@links_bp.post("/create")
def createLink():
    data = request.json
    return links_service.createLink(data)
@links_bp.put("/update/<int:id>")
def updateLink(id:int):
    data = request.json
    return links_service.updateLink(id, data)

@links_bp.delete("/delete/<int:id>")
def deleteLink(id:int):
    return links_service.deleteLink(id)