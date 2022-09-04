from io import TextIOWrapper


class Printer:
    def make_file(path: str = ".", name: str = "file", type: str = "txt", text: str = "") -> None:
        file: TextIOWrapper = open(f"{path}/{name}.{type}", "w", encoding="utf-8")
        file.write(text)
        file.close


from unicodedata import normalize
import re as regex


class String:
    def drop_accents(string: str) -> str:
        return normalize("NFKD", string).encode("ascii", "ignore").decode("ascii")

    def make_alphanumeric(string: str) -> str:
        return regex.sub("[^A-Za-z0-9 ]+", "", string)

    def set_snake_case(string: str) -> str:
        return regex.sub(" ", "_", string)
