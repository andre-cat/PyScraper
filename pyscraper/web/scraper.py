from xmlrpc.client import boolean
from bs4 import BeautifulSoup # type: ignore
from bs4 import Doctype # type: ignore
from bs4.element import PageElement # type: ignore
from bs4.element import NavigableString 
from pyscraper.constants import PARENT_PATH
from pyscraper.web.webpage import Page

def write_html(page : Page) -> None:
    with open(f'{PARENT_PATH}/{page.get_title()}.{page.get_type()}', 'r') as file:
    #with open(f'{PARENT_PATH}/page.html', 'r') as file:
        soup : BeautifulSoup = BeautifulSoup(file, 'html.parser')
        
        #if page.get_type() == 'html':
        #    soup = BeautifulSoup(file, 'html.parser')
        #elif page.get_type() == 'xml':
        #    soup = BeautifulSoup(file, 'xml')

#for element in soup.contents:
#if type(element) == Doctype:
#soup.decompose()

        if len(soup.contents) != 0:
            __walk(soup.contents[0],0)

def __walk(element: PageElement, spaces : int) -> None:
    if type(element) != NavigableString:

        print(f'{" " * spaces}<{element.name}>')

        if __exists_next_child(element):
            __walk(element.contents[0],spaces + 4)
        
        if __exists_next_sibling(element):
            __walk(element.next_sibling,spaces + 4)
        
        print(f'{" " * spaces}</{element.name}>')
        return None

def __exists_next_child(element : PageElement) -> boolean:
    if element.contents[0] != None:
        return True
    else:
        return False

def __exists_next_sibling(element: PageElement) -> boolean:
    if element.next_sibling != None:
        return True;
    else:
        return False;

def __exists_next_parent(element: PageElement) -> boolean:
    if element.parent != None:
        return True;
    else:
        return False;