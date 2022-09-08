import unittest
from pyscraper import pyscraper
import re

class TestPyscraper(unittest.TestCase):

    def test_download_html(self) -> None:
        #pyscraper.get_html('https://realpython.com/beautiful-soup-web-scraper-python/')

        html="""<html lang="en">
        <head>
            <meta charset="utf-8"/>
            <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
            <title>
            My html page
            </title>
        </head>
        <body>
            <p>
            Today is a beautiful day. We go swimming and fishing.
            </p>
            <p>
            Hello there. How are you?
            </p>
        </body>
        </html>"""

        print(html)

if __name__ == '__main__':
    unittest.main()
