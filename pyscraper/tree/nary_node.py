class NaryNode:
    def __init__(self, info: str) -> "NaryNode":
        self.__info: str = info
        self.__links: list = []

    def get_info(self) -> str:
        return self.__info

    def set_info(self, info: str) -> None:
        self.__info: str = info

    def add_son(self, info : str) -> None:
        self.__links.append(info);

    def get_son(self, index: int) -> "NaryNode":
        return self.__links[index-1];