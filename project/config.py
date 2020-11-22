import sys
from pathlib import Path

import toml

from project.utils import print_error

CONFIG_PATH = f"{Path.home()}/.project.toml"


def config():
    try:
        with open(CONFIG_PATH) as f:
            return toml.loads(f.read())
    except FileNotFoundError:
        print_error(f"Config file '{CONFIG_PATH}' does not exist")


if __name__ == "__main__":
    print(config())
