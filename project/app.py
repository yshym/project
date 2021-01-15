import subprocess
import sys
import webbrowser
from os import getenv
from typing import Optional

import typer
from colorama import Fore

from project.config import config as parse_config
from project.utils import print_error

app = typer.Typer()


@app.command()
def list():
    """List projects"""

    config = parse_config()

    if not config:
        return

    print(
        "\n".join(
            f"· {k} {'✔' if k == config.get('default') else ''}"
            for k in config.get("projects").keys()
        )
    )


def get_project(name):
    config = parse_config()

    if not config:
        return

    default = config.get("default")
    projects = config.get("projects")

    if not name:
        name = default

    return name, projects.get(name)


@app.command()
def links(name: Optional[str] = typer.Argument(None)):
    """Open links"""

    name, project = get_project(name)

    if not project:
        print_error(f"Project '{name}' does not exist")
        return

    links = project.get("links")

    if not links:
        print_error(
            f"You have not added links of '{name}' to the config file",
        )
        return

    for l in links:
        webbrowser.open(l)


@app.command()
def services(name: Optional[str] = typer.Argument(None)):
    """Check services"""

    name, project = get_project(name)

    if not project:
        print_error(f"Project '{name}' does not exist")
        return

    services = project.get("services")

    if not services:
        print_error(
            f"You have not added services of '{name}' to the config file",
        )
        return

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

    name, project = get_project(name)

    if not project:
        print_error(f"Project '{name}' does not exist")
        return

    path = project.get("path")

    if not path:
        print_error(
            f"You have not added the path to '{name}' to the config file",
        )
        return

    subprocess.run([getenv("EDITOR"), path])
