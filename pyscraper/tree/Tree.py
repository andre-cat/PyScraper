
from pyscraper.tree.node import Node
from typing import Optional

class Tree:
    def __init__(self, info: Optional[str] = None) -> None:
        self.__root: Optional[Node] = None
        if type(info) == str:
            self.__root = Node(info)

    def get_root(self) -> Optional[Node]:
        return self.__root

    def draw(self) -> None:
        if type(self.__root) == Node:
            print(self.__root.get_son(1).__info)
            self.__draw(self.__root, 0)

    def __draw(self, node: Node, spaces: int) -> None:
        iterator : int = 0
        while node.get_son(iterator) != None:
            iterator = iterator +1 
            print(f'{" " * spaces}|--{str(node.get_son(iterator))}');
            if node.get_son(0).get_son(0) != None:
                self.__draw(node, spaces + 3);