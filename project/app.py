import subprocess
import sys
import webbrowser
from os import getenv
from typing import Optional

import typer
from colorama import Fore

from project.config import config as parse_config

app = typer.Typer()


@app.command()
def list():
    """List projects"""

    config = parse_config()

    if not config:
        return

    print("\n".join(f"· {k}" for k in config.get("projects").keys()))


def get_project(name):
    config = parse_config()

    if not config:
        return

    default = config.get("default")
    projects = config.get("projects")

    return projects.get(name if name else default)


@app.command()
def links(name: Optional[str] = typer.Argument(None)):
    """Open links"""

    project = get_project(name)

    if not project:
        print(f"{Fore.RED}Project '{name}' does not exist", file=sys.stderr)
        return

    links = project.get("links")

    for l in links:
        webbrowser.open(l)


@app.command()
def services(name: Optional[str] = typer.Argument(None)):
    """Check services"""

    project = get_project(name)
    services = project.get("services")

    for s in services:
        service_is_running = not bool(
            subprocess.run(["pgrep", s], stdout=subprocess.DEVNULL).returncode
        )
        running_text = f"{Fore.GREEN}running"
        not_running_text = f"{Fore.RED}not running"

        print(
            f"{s} - {running_text if service_is_running else not_running_text}"
        )


@app.command()
def code(name: Optional[str] = typer.Argument(None)):
    """Open code"""

    project = get_project(name)
    path = project.get("path")

    if not path:
        print(
            f"{Fore.RED}You have not added the path to '{name}' to the config file",
            file=sys.stderr,
        )
        return

    subprocess.run([getenv("EDITOR"), path])
