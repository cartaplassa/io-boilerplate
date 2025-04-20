#!/usr/bin/env python3
"""
Converts Markdown heading links to Obsidian wiki links in a file.

Args:
    filepath: Path to the Markdown file.
"""

__author__ = "Cartaplassa"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import os
import logging
from datetime import datetime
from pathlib import PurePath

path = PurePath()

def setup_argparse():
    parser = argparse.ArgumentParser()
    # Required positional arguments
    parser.add_argument(
        "number",
        type=int,
        help="Annual number of shipment"
    )
    parser.add_argument(
        "date",
        type=str,
        help="Date of shipment, eg. 01.01.2025"
    )
    # Defaulted IO arguments
    parser.add_argument(
        "-i", "--input", 
        type=str,
        help="Path to input table",
        default="../sheets/input.xlsx"
    )
    parser.add_argument(
        "-o", "--output", 
        type=str,
        help="Path to output folder",
        default="../output"
    )
    # Optional verbosity
    parser.add_argument(
        "-v", "--verbosity",
        action="count",
        help="Set verbosity level"
    )
    # Specify output of "--version"
    parser.add_argument(
        "-V", "--version",
        action="version",
        version=f"%(prog)s (version {__version__})"
    )
    return parser.parse_args()

logging.getLogger().setLevel(logging.NOTSET)
logger = logging.getLogger()
FILE_HANDLER_FMT = (
    "%(asctime)s-%(msecs)04d [%(levelname)s]"
    "(%(name)s:%(funcName)s:%(lineno)d): %(message)s"
)
CLI_HANDLER_FMT = (
    "%(asctime)s-%(msecs)04d [%(levelname)s]"
    "(%(name)s): %(message)s"
)

def setup_logger(args):
    if not os.path.exists('logs'): os.mkdir('logs')

    file_handler = logging.FileHandler(
        "logs/debug-" + datetime.strftime(
            datetime.now(), '%Y-%m%d-%H%M%S'
        ) + ".log"
    )
    file_handler.setFormatter(logging.Formatter(
        fmt=FILE_HANDLER_FMT,
        datefmt="%Y-%m%d-%H%M%S"
    ))
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    cli_handler = logging.StreamHandler()
    cli_handler.setLevel(logging.CRITICAL)
    cli_handler.setFormatter(logging.Formatter(
        fmt=CLI_HANDLER_FMT,
        datefmt="%H%M%S"
    ))
    logger.addHandler(cli_handler)

    if not args.verbosity:
        cli_handler.setLevel(logging.ERROR)
    elif args.verbosity == 1:
        cli_handler.setLevel(logging.WARNING)
    elif args.verbosity == 2:
        cli_handler.setLevel(logging.INFO)
    elif args.verbosity >= 3:
        cli_handler.setLevel(logging.DEBUG)
    else:
        logger.critical("Negative verbosity count")
    logger.debug(f"Logger set up with {cli_handler.level} level")


def main(args):
    pass


if __name__ == "__main__":
    args = setup_argparse()
    setup_logger(args)
    main(args)



