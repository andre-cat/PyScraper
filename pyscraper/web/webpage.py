from typing import Optional

class Page:

    def __init__(self, title: str = '', type: str = '',elements: str = '') -> None:
        self.__title : str= title;
        self.__type : str= type;
        self.__elements : str= elements;
    
    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str) -> None:
        self.__title = title
    
    def get_type(self)-> str:
        return self.__type
    
    def set_type(self, type: str) -> None:
        self.__type = type

    def get_elements(self)-> str:
        return self.__elements
    
    def set_elements(self, elements: str) -> None:
        self.__elements = elements