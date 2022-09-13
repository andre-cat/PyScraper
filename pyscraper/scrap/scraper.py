from types import NoneType
from pyscraper.commons import PARENT_PATH
from bs4 import BeautifulSoup  # type: ignore
from bs4.element import Tag  # type: ignore
from pyscraper.web.page import Page
from pyscraper.scrap.tree import Tree
from pyscraper.scrap.node import Node

__tag_page: str
__tree: Tree


def __get_soup(page: Page) -> BeautifulSoup:
    with open(f"{PARENT_PATH}/{page.get_title()}{page.get_type()}", "r") as file:
        if page.get_type() == ".html" or page.get_type() == "":
            return BeautifulSoup(file, "html.parser")
        elif page.get_type() == ".xml":
            return BeautifulSoup(file, "xml")


def get_tree(page: Page) -> Tree:
    soup: BeautifulSoup = __get_soup(page)
    root: Tag = soup.findChild()

    if root != None:
        global __tree
        __tree = Tree(root.name)
        __get_tree(root, __tree.get_root())
        return __tree
    return Tree()


def __get_tree(tag: Tag, node: Node) -> None:

    if __exists_next_child(tag):
        node.add_child(tag.findChild().name)
        __get_tree(tag.findChild(), node.get_last_child())

    if __exists_next_sibling(tag):
        node.get_parent().add_child(tag.find_next_sibling().name)
        __get_tree(tag.find_next_sibling(), node.get_parent().get_last_child())


def get_tag_page(page: Page) -> str:
    soup: BeautifulSoup = __get_soup(page)
    root: Tag = soup.findChild()

    if root != None:
        global __tag_page
        __tag_page = root.name
        __get_source_tag(root.findChild(), 0)
        return __tag_page
    else:
        return ""


def __get_source_tag(tag: Tag, spaces: int) -> None:
    global __tag_page

    __tag_page = __tag_page + "\n" + f'{" " * spaces}<{tag.name}>'
    if __exists_next_child(tag):
        __get_source_tag(tag.findChild(), spaces + 3)

    __tag_page = __tag_page + "\n" + f'{" " * spaces}</{tag.name}>'
    if __exists_next_sibling(tag):
        __get_source_tag(tag.find_next_sibling(), spaces)


def __exists_next_child(tag: Tag) -> bool:
    if tag.findChild() != None and type(tag.findChild()) == Tag:
        return True
    else:
        return False


def __exists_next_sibling(tag: Tag) -> bool:
    if tag.find_next_sibling() != None and type(tag.find_next_sibling()) == Tag:
        return True
    else:
        return False
