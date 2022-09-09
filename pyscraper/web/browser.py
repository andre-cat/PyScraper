import requests
from requests import Response
from lxml.html import fromstring # type: ignore 
from pyscraper.constants import PARENT_PATH
from pyscraper.commons import string
from pyscraper.commons import file
from pyscraper.web.webpage import Page

def get_html(link: str) -> Page:
    try:
        if link != 'about:blank':
            response: Response = requests.get(link)
            title: str = string.set_snake_case(string.make_alphanumeric(string.drop_accents(fromstring(response.content).findtext('.//title'))))[0:200]
            type = response.headers['content-type']
            if type.find('html') != -1:
                type = 'html'
            elif type.find('xml') != -1:
                type = 'xml'
            elements: str = response.text
            return Page(title, type, elements)
        else:
            return Page('about_blank', '','')
    except Exception as exception:
        print(f'Error en {__file__}: {exception}')
        return Page('', '', '')

def print_html(page : Page) -> None:
    file.print(PARENT_PATH, name=page.get_title(), type=page.get_type(), text=page.get_elements())

