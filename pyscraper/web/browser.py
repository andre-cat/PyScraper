import requests
from lxml.html import fromstring  # type: ignore
from pyscraper.commons import PARENT_PATH
from pyscraper.commons import String
from pyscraper.commons import File
from pyscraper.web.page import Page


def get_page(link: str) -> Page:
    try:
        if link != "about:blank":
            response: requests.Response = requests.get(link)
            title: str = String.set_snake_case(String.make_alphanumeric(String.drop_accents(fromstring(response.content).findtext(".//title"))))[0:200]
            type = response.headers["content-type"]
            if type.find("html") != -1:
                type = ".html"
            elif type.find("xml") != -1:
                type = ".xml"
            source: str = response.text
            return Page(title, type, source)
        else:
            return Page("about_blank", "", "")
    except Exception as exception:
        raise Exception(exception)


def print_page(page: Page) -> None:
    File.print(PARENT_PATH, name=page.get_title(), type=page.get_type(), text=page.get_source())
