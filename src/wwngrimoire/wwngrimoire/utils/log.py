import logging
import sys

from pathlib import Path

from wwngrimoire.constants import LOG_FORMAT, LOG_FILE


def initiate_logger(filename: Path | str = LOG_FILE, filemode: str = "a") -> None:
    """
    Holds the basic config for a logger to be used in the program

    Args:
        filename (Path | str): where to save the log file at
        filemode (str): filemode to write to the log file

    Returns:
        None
    """
    logging.basicConfig(
        format=LOG_FORMAT, level=logging.INFO, filename=filename, filemode=filemode
    )
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    return
