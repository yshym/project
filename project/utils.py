import sys

from colorama import Fore


def print_error(text):
    print(Fore.RED + text, file=sys.stderr)
