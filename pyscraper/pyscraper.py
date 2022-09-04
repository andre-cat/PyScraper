from pyscraper.html.browser import Browser
from pyscraper.html.scraper import Scraper
from pyscraper.html.painter import Painter
from pyscraper.commons import Printer
from pyscraper.constants import PATH
from os import path

class PyScraper:
    def do_this():
        print("Dummt text")

    def download_html(link: str = "about:blank") -> None:
        html: tuple(str, str) = Browser.get_html(link)
        title: str = html[0]
        elements: str = html[1]

        Printer.make_file(path=path.dirname(PATH), name=title, type="html", text=elements)
