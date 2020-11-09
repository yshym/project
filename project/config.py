import sys
from pathlib import Path

import toml

CONFIG_PATH = f"{Path.home()}/.project.toml"


def config():
    try:
        with open(CONFIG_PATH) as f:
            return toml.loads(f.read())
    except FileNotFoundError:
        print(f"Config file '{CONFIG_PATH}' does not exist", file=sys.stderr)

if __name__ == "__main__":
    print(config())
