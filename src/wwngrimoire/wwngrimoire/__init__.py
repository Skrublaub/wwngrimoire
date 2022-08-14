import logging

from typer import Typer, Option
from flask import Flask, url_for, redirect

from wwngrimoire.utils.log import initiate_logger
from wwngrimoire.utils.spell_utils import generate_json as utils_generate_json

from wwngrimoire.pages.no_js import no_js_bp

app: Flask = Flask(__name__)
cli: Typer = Typer()

app.register_blueprint(no_js_bp)

# initiate_logger()  # makes flask double print
logger = logging.getLogger(__name__)


@cli.command(help="start the wwngrimoire server")
def start(
    debug_mode: bool = Option(
        False, "-d", "--debug", help="flag to start the server in debug mode"
    )
) -> None:
    app.run(debug=debug_mode)


@cli.command(help="generate spell(s) json")
def generate_json() -> None:
    utils_generate_json()


@app.route("/")
@app.route("/home")
def home_page():
    no_js_url: url_for = url_for("no_js.no_js_home_page")
    return redirect(no_js_url)


def enter() -> None:
    cli()


if __name__ == "__main__":
    start()
