import os

from pathlib import Path
from typing import Final

RELATIVE_PATH: Final[Path] = Path(os.path.dirname(__file__))
SPELLS_PATH: Final[Path] = RELATIVE_PATH / "spells"
SPELLS_JSON_NAME: Final[str] = "spells.json"
SPELLS_JSON_PATH: Final[Path] = SPELLS_PATH / SPELLS_JSON_NAME

LOG_FORMAT: Final[str] = "%(asctime)s-%(name)s-%(levelname)s: %(message)s"
LOG_FILE: Final[str] = RELATIVE_PATH / "wwn_log.log"
