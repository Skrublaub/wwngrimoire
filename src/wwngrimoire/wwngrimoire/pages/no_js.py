import logging

from flask import render_template, Blueprint

no_js_bp = Blueprint("no_js", __name__)  # no javascript blueprint
logger = logging.getLogger(__name__)


@no_js_bp.route("/nojs")
def no_js_home_page():
    return render_template("home.html")


@no_js_bp.route("/about")
def about_page():
    return render_template("about.html")


@no_js_bp.route("/nojs/search/<query>")
def no_js_search(query):
    pass
