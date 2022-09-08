from unicodedata import normalize
import re as regex


def drop_accents(string: str) -> str:
    return normalize('NFKD', string).encode('ascii', 'ignore').decode('ascii')

def make_alphanumeric(string: str) -> str:
    return regex.sub('[^A-Za-z0-9 ]+', '', string)

def set_snake_case(string: str) -> str:
    return regex.sub(' ', '_', string)