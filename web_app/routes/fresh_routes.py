from flask import Blueprint, render_template, current_app #, session
from app.models.fresh import Fresh
fresh_routes = Blueprint("fresh_routes", __name__)
@fresh_routes.route("/freshs")
def freshs():
    freshs = Fresh.all()
    return render_template("freshs.html", freshs=freshs)