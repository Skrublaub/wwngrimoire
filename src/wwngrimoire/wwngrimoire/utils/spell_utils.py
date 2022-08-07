import json
import logging

from pathlib import Path
from typing import Any

from wwngrimoire.constants import SPELLS_PATH, SPELLS_JSON_NAME

logger = logging.getLogger(__name__)


def generate_json(
    directory: Path | str = SPELLS_PATH, write_json: bool = True
) -> dict[Any]:
    """
    Generates json for all txt files in a directory. Writes json to
    disk after generating if wanted by user

    Args:
        directory (Path | str): Directory to examine the txt files in
            and place the output json in
        write_json (bool): Whether to write json to disk or not in
            directory

    Returns:
        dict[Any]: The json of all
    """
    final_json: dict[Any] = {}

    txt_files: list[Path] = [
        file for file in directory.iterdir() if file.suffix == ".txt"
    ]

    for txt_file in txt_files:
        final_description: str = ""
        spell_description: list[str] = []
        final_level: int = -1
        final_tradition: str = ""

        final_name: str = txt_file.stem.replace("_", " ")

        with txt_file.open("r") as open_file:
            spell_description = open_file.readlines()

        final_level = int(spell_description[0])
        final_tradition = spell_description[1].rstrip()  # get rid of trailing /n
        final_description = "".join(
            spell_description[2:]
        )  # Thinking about getting rid of the newline characters

        final_json[final_name] = {
            "level": final_level,
            "tradition": final_tradition,
            "description": final_description,
        }

    if write_json:
        with open(directory / SPELLS_JSON_NAME, "w") as json_file:
            logger.info(f"writing json to {directory / SPELLS_JSON_NAME}")
            json_file.write(json.dumps(final_json))

    return final_json
