from flask import Blueprint, render_template, request

links_bp = Blueprint("links",__name__, url_prefix="/api/links")

@links_bp.route("/", methods=["GET"])
def get_links():
    return "Links"

@links_bp.route("/", methods=["POST"])
def save_links():
    return "post"