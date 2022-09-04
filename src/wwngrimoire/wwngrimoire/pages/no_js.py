import logging
import json

from typing import Any
from wwngrimoire.constants import SPELLS_JSON_PATH

from flask import render_template, Blueprint

no_js_bp = Blueprint("no_js", __name__)  # no javascript blueprint
logger = logging.getLogger(__name__)


@no_js_bp.route("/nojs")
def no_js_home_page():
    """
    Renders the nojs homepage for the website

    Returns:
        render_template: render_template("home.html")
    """
    return render_template("home.html")


@no_js_bp.route("/about")
def about_page():
    """
    Is the about page. This doesn't need to be javascript at all

    Returns:
        render_template: render_template("home.html")
    """
    return render_template("about.html")


@no_js_bp.route("/nojs/search")
def search_no_parameter():
    """
    Catches the blank search when pressing enter

    Returns:
        render_template: A render template with all spells in
        hopefully alphabetical order.
    """
    spell_json: dict[Any] = _search_json("")

    return render_template("search.html")


@no_js_bp.route("/nojs/search/<query>")
def no_js_search(query: str):
    """
    Search for a spell bro

    Args:
        query (str): The spell to search for

    Returns:
        render_template: A list of spells that hopefully match the
        search parameters
    """
    spell_json: dict[Any] = _search_json(query)

    return render_template("search.html")


def _search_json(query: str) -> str:
    """
    Helper for the two search functions that can handle the empty
    search parameter and the filled one

    Args:
        query (str): The spell to search for. Can be empty

    Returns:
        str: html str that can be rendered in the search queries
    """
    spell_json: dict[Any] = {}
    matching_spells: dict[Any] = {}

    with SPELLS_JSON_PATH.open("r") as spells_file:
        spell_json = json.load(spells_file)

    if not query:
        matching_spells = spell_json
    else:  # obtain matching spells
        for spell_name, attributes in spell_json:
            if query in spell_name:
                matching_spells[spell_name] = attributes

    pass
