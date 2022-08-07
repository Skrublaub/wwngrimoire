import json
import logging

from pathlib import Path
from typing import Any

from wwngrimoire.constants import SPELLS_PATH, SPELLS_JSON_NAME

logger = logging.getLogger(__name__)


def generate_json(directory: Path | str = SPELLS_PATH, write_json: bool = True) -> dict[Any]:
    """
    Generates json for all txt files in a directory. Writes json to
    disk after generating if wanted by user

    Args:
        directory (Path | str): Directory to examine the txt files in
            and place the output json in
        write_json (bool): Whether to write json to disk or not

    Returns:
        dict[Any]: The json of all
    """
    final_json: dict[Any] = {}

    txt_files: list[Path] = [file for file in directory.iterdir() if file.suffix == ".txt"]

    for txt_file in txt_files:
        final_description: str = ""
        spell_description: list[str] = []
        spell_name: str = txt_file.stem  # The_Howl_of_Light_3
        spell_parts: list[str] = spell_name.split("_")  # ['The', 'Howl', 'of', 'light', '3']

        spell_level = spell_parts[-1]  # '3' notice it's a string
        if not spell_level.isnumeric():
            logger.info(f"############### No level found: {txt_file}")
            continue  # Skip if not numeric

        final_name: str = " ".join(spell_parts[:-1])  # The
        final_level: int = int(spell_level)

        with txt_file.open('r') as open_file:
            spell_description = open_file.readlines()

        final_description = "".join(spell_description)

        final_json[final_name] = {"level": final_level, "description": final_description}

    if write_json:
        with open(directory / SPELLS_JSON_NAME, 'w') as json_file:
            logger.info(f"writing json to {directory / SPELLS_JSON_NAME}")
            json_file.write(json.dumps(final_json))

    return final_json
