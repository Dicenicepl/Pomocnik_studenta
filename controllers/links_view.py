from flask import Blueprint, render_template, request, redirect, url_for
from services import links_service

links_view = Blueprint("links_view", __name__, url_prefix="/links")


@links_view.get("/")
def links_page():
    response, _ = links_service.getAllLinks()
    return render_template("links.html", links=response.json)


@links_view.post("/create")
def create_link():
    data = {
        "name": request.form["name"],
        "url": request.form["url"]
    }
    links_service.createLink(data)
    return redirect(url_for("links_view.links_page"))


@links_view.post("/update/<int:id>")
def update_link(id):
    data = {
        "name": request.form["name"],
        "url": request.form["url"]
    }
    links_service.updateLink(id, data)
    return redirect(url_for("links_view.links_page"))


@links_view.post("/delete/<int:id>")
def delete_link(id):
    links_service.deleteLink(id)
    return redirect(url_for("links_view.links_page"))
