from pyscraper.scrap.tree import Tree
from pyscraper.paint import window
from pyscraper.web.browser import Page
from pyscraper.scrap.node import Node
from pyscraper.scrap.tree import Tree
from pyscraper.paint.paint import Paint

def show_window():
    window.show()

def get_paint(tree : Tree, tag_page : str, page : Page):
    Paint(tree, tag_page, page)