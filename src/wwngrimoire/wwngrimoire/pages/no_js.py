import logging

from flask import redirect, render_template, Blueprint

no_js_bp = Blueprint("no_js", __name__)  # no javascript blueprint
logger = logging.getLogger(__name__)


@no_js_bp.route("/")
def home_page():
    logger.info("redirect happening")
    return redirect("http://127.0.0.1:5000/nojs")


@no_js_bp.route("/nojs")
def no_js_home_page():
    return render_template('home.html')
