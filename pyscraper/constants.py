from os import path
from typing import Final

# Path of project
PATH: Final[str] = path.dirname(path.dirname(__file__))
PARENT_PATH: Final[str] =path.dirname(path.dirname(path.dirname(__file__)))