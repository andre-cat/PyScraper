# CLASSES
from io import TextIOWrapper


class File:
    @staticmethod
    def print(path: str = "", name: str = "file", type: str = "", text: str = "") -> None:
        file: TextIOWrapper = open(f"{path}/{name}{type}", "w", encoding="utf-8")
        file.write(text)
        file.close


from unicodedata import normalize
import re as regex


class String:
    @staticmethod
    def unnumber(string: str, where_number: str) -> str:
        return regex.sub("[0-9]", where_number, string)

    @staticmethod
    def drop_accents(string: str) -> str:
        return normalize("NFKD", string).encode("ascii", "ignore").decode("ascii")

    @staticmethod
    def make_alphanumeric(string: str) -> str:
        return regex.sub("[^A-Za-z0-9 ]+", "", string)

    @staticmethod
    def set_snake_case(string: str) -> str:
        return regex.sub(" ", "_", string)


from os import path
from typing import Final

# CONSTANTS
PATH: Final[str] = path.dirname(path.dirname(__file__))  # Path of project
PARENT_PATH: Final[str] = path.dirname(path.dirname(path.dirname(__file__)))

# METHODS
def print_error(file: str, exception: Exception):
    print(f"EXCEPTION ON {file}: {exception}")
