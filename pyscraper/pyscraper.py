from pyscraper.html import browser
from pyscraper.html import scraper
from pyscraper.html import painter

def get_html(link: str) -> tuple:
    return browser.get_html(link)

def print_html(html : tuple) -> None:
    browser.print_html(html)

def write_html(html_name : str) -> None:
    scraper.write_html(html_name);