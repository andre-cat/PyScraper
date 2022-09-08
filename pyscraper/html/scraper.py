from bs4 import BeautifulSoup # type: ignore
from pyscraper.constants import PARENT_PATH

def write_html(html_name : str):
    with open(f'{PARENT_PATH}/{html_name}', 'r') as f:
        
        soup = BeautifulSoup(f.read(), 'lxml')

        for child in soup.recursiveChildGenerator():
            if child.name:
                print(f'    {child.tag}')