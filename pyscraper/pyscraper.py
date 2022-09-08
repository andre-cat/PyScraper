from pyscraper.web import browser
from pyscraper.web import scraper
from pyscraper.web import painter
from pyscraper.web.webpage import Page
from typing import Optional

def get_html(link: str) -> Page:
    return browser.get_html(link)

def print_html(html : Page) -> None:
    browser.print_html(html)

def write_html(html_name : Page) -> None:
    scraper.write_html(html_name);