from pyscraper.scrap.node import Node
from typing import Optional
from pyscraper.commons import String

class Tree:

    __spaces : int = 3

    def __init__(self, info: Optional[str] = None) -> None:
        self.__root: Node = None  # type: ignore
        if type(info) == str:
            self.__root = Node(info)
            self.__root.set_id(1)
            self.__stream : str = ""

    def get_root(self) -> Node:
        return self.__root

    def get_stream(self, id : bool = False) -> str:
        self.__stream = ""
        if self.__root != None:
            self.__stream = f'{self.__root.get_id()}: {self.__root.get_info()}'
            self.__get_stream(self.__root, 0)
            if id == False:
                self.__stream = String.unnumber(self.__stream,"").replace(":",">")
            return self.__stream
        else:
            return '';

    def __get_stream(self, node: Node, spaces: int) -> None:
        if node != None:
            iterator: int = 1
            while node.get_child(iterator) != None:
                self.__stream = f'{self.__stream}\n{" " * spaces}|--{node.get_child(iterator).get_id()}: {node.get_child(iterator).get_info()}'
                self.__get_stream(node.get_child(iterator), spaces + Tree.__spaces)
                iterator = iterator + 1

    def print(self, id: bool = False) -> None:
        if self.__root != None:
            if id == False:
                print(self.__root.get_info())
                self.__print(self.__root, 0)
            else:
                print(f"1: {self.__root.get_info()}")
                self.__print_id(self.__root, 0)
        else:
            print("Root = None")

    def __print(self, node: Node, spaces: int) -> None:
        if node != None:
            iterator: int = 1
            while node.get_child(iterator) != None:
                print(f'{" " * spaces}|--> {node.get_child(iterator).get_info()}')
                self.__print(node.get_child(iterator), spaces + Tree.__spaces)
                iterator = iterator + 1

    def __print_id(self, node: Node, spaces: int) -> None:
        if node != None:
            iterator: int = 1
            while node.get_child(iterator) != None:
                print(f'{" " * spaces}|--{node.get_id()}: {node.get_child(iterator).get_info()}')
                self.__print_id(node.get_child(iterator), spaces + Tree.__spaces)
                iterator = iterator + 1
