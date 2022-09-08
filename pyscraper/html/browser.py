import requests
from requests import Response
from lxml.html import fromstring # type: ignore 
from pyscraper.constants import PARENT_PATH
from pyscraper.commons import string
from pyscraper.commons import file

def get_html(link: str) -> tuple:
    try:
        if link != 'about:blank':
            response: Response = requests.get(link)
            title: str = string.set_snake_case(string.make_alphanumeric(string.drop_accents(fromstring(response.content).findtext('.//title'))))[0:200]
            elements: str = response.text
            return (title, elements)
        else:
            return ('about_blank', '')
    except Exception as exception:
        return (f'Error en {__file__}: {exception}', None)

def print_html(html : tuple) -> None:
    file.print(PARENT_PATH, name=html[0], type='html', text=html[1])
