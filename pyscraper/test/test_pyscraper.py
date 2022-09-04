import unittest
from pyscraper.pyscraper import PyScraper

class TestPyscraper(unittest.TestCase):

    def test_download_html(self) -> None:
        PyScraper.download_html(
            'https://realpython.com/beautiful-soup-web-scraper-python/')


if __name__ == '__main__':
    unittest.main()
