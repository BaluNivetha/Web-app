from flask import Blueprint, render_template, current_app #, session
from app.models.frozen import Frozen
frozen_routes = Blueprint("frozen_routes", __name__)
@frozen_routes.route("/frozens")
def frozens():
    frozens = Frozen.all()
    return render_template("frozens.html", frozens=frozens)