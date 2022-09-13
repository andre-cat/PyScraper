class Page:
    def __init__(self, title: str = "", type: str = "", source: str = "") -> None:
        self.__title: str = title
        self.__type: str = type
        self.__source: str = source

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str) -> None:
        self.__title = title

    def get_type(self) -> str:
        return self.__type

    def set_type(self, type: str) -> None:
        self.__type = type

    def get_source(self) -> str:
        return self.__source

    def set_source(self, source: str) -> None:
        self.__source = source
