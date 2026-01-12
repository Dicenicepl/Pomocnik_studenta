from database import db
from models.link import Link

def getAllLinks():
    return Link.query.all()

def getLinkById(id: int):
    return Link.query.filter(Link.id == id).first()

def createLink(link: Link):
    db.session.add(link)
    db.session.commit()
    return link

def updateLink(id: int, data):
    link = getLinkById(id)
    if not link:
        return None

    link.name = data.get("name", link.name)
    link.url = data.get("url", link.url)
    link.icon = data.get("icon", link.icon)

    db.session.commit()
    return link

def deleteLink(id: int):
    rows = Link.query.filter(Link.id == id).delete()
    db.session.commit()
    return rows > 0

