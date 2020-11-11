import sys
import webbrowser
from typing import Optional

import typer

from project.config import config as parse_config

app = typer.Typer()


@app.command()
def links(name: Optional[str] = typer.Argument(None)):
    """Open links"""

    config = parse_config()

    if not config:
        return

    default = config.get("default")
    projects = config.get("projects")

    project = projects.get(name if name else default)

    if not project:
        print(f"Project '{name}' does not exist", file=sys.stderr)
        return

    links = project.get("links")

    for l in links:
        webbrowser.open(l)


@app.command()
def services(name: Optional[str] = typer.Argument(None)):
    """Check services"""

    pass
