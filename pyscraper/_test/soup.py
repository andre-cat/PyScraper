import unittest
from pyscraper.commons import print_error
from bs4 import BeautifulSoup  # type: ignore


class TestSoup(unittest.TestCase):
    def test_scrap_blnak(self) -> None:
        try:            
            soup = BeautifulSoup('', "html.parser")
            print(soup.findChild())
            print(type(soup))
        except Exception as exception:
            print_error(__name__, exception)

if __name__ == "__main__":
    unittest.main()
