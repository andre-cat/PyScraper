from pyscraper.web import browser
from pyscraper.web.page import Page
from pyscraper.scrap import scraper
from pyscraper.scrap.tree import Tree
from pyscraper.paint import painter


def run():
    try:
        painter.show_window()
    except Exception as exception:
        print(exception)


def get_page(link: str) -> Page:
    return browser.get_page(link)


def print_page(page: Page) -> None:
    browser.print_page(page)


def get_tag_page(page: Page) -> str:
    return scraper.get_tag_page(page)


def get_tree(page: Page) -> Tree:
    return scraper.get_tree(page)

def get_paint(tree:Tree, tag_page:str, page:Page) -> None:
    painter.get_paint(tree, tag_page, page)