from ast import If
from pyscraper.scrap.node import Node
from typing import Optional
from pyscraper.commons import String

class Tree:

    __spaces : int = 2

    def __init__(self, info: Optional[str] = None) -> None:
        self.__root: Node = None  # type: ignore
        if type(info) == str:
            self.__root = Node(info)
            self.__root.set_id(1)
            self.__stream : str = ""
            self.__children_per_level : dict = {}

    def get_root(self) -> Node:
        return self.__root

    def get_stream(self, id : bool = False) -> str:
        self.__stream = ""
        if self.__root != None:
            self.__stream = f'{self.__root.get_id()}: {self.__root.get_info()}'
            self.__get_stream(self.__root, 0)
            if id == False:
                self.__stream = String.unnumber(self.__stream,"").replace(":",">")[2:]
            return self.__stream
        else:
            return '';

    def __get_stream(self, node: Node, spaces: int) -> None:
        if node != None:
            iterator: int = 1
            while node.get_child(iterator) != None:
                self.__stream = f'{self.__stream}\n{" " * (spaces)}|{"-" * (Tree.__spaces - 1)}{node.get_child(iterator).get_id()}: {node.get_child(iterator).get_info()}'
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
                print(f'{" " * spaces}|-> {node.get_child(iterator).get_info()}')
                self.__print(node.get_child(iterator), spaces + Tree.__spaces)
                iterator = iterator + 1

    def __print_id(self, node: Node, spaces: int) -> None:
        if node != None:
            iterator: int = 1
            while node.get_child(iterator) != None:
                print(f'{" " * spaces}|-{node.get_id()}: {node.get_child(iterator).get_info()}')
                self.__print_id(node.get_child(iterator), spaces + Tree.__spaces)
                iterator = iterator + 1

    def get_children_per_level(self):
        self.__get_children_per_level(self.__root)
        return self.__children_per_level
    
    def __get_children_per_level(self, node : Node):
        if node != None:
            try :
                self.__children_per_level[len(str(node.get_id()))] = self.__children_per_level[len(str(node.get_id()))] + 1 
            except:
                self.__children_per_level[len(str(node.get_id()))] = 1

            iterator: int = 1
            while node.get_child(iterator) != None:
                self.__get_children_per_level(node.get_child(iterator))
                iterator = iterator + 1

    def get_largest_info(self) -> int:
        largest_info : int = 0

        if self.__root != None:
            queue : list = []
            queue.append(self.__root)
            
            while len(queue) > 0:
                node : Node = queue[0]

                queue.pop(0)

                if len(node.get_info()) > largest_info:
                    largest_info = len(node.get_info())
                
                for number_child in range(0, node.get_number_children()):
                    queue.append(node.get_child(number_child))
    
        return largest_info