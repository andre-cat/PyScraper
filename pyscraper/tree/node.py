class Node:
    def __init__(self, info: str) -> None:
        self.__info: str = info
        self.__links: list = []
        return None

    def get_info(self) -> str:
        return self.__info

    def set_info(self, info: str) -> None:
        self.__info = info

    def add_son(self, info : str) -> None:
        self.__links.append(info);

    def get_son(self, index: int) -> "Node":
        return self.__links[index-1];