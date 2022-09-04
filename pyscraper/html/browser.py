import requests
from lxml.html import fromstring
from pyscraper.commons import String

class Browser:

    def get_html(link: str) -> tuple:
        response = requests.get(link)
        title = String.set_snake_case(String.make_alphanumeric(String.drop_accents(fromstring(response.content).findtext('.//title'))))[0:200]
        elements = response.text
        return (title , elements);