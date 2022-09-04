from Node import NaryNode as Node

class NaryTree:
    def __init__(self, info: str = None) -> "NaryTree":
        if info == None:
            self.__root: Node = None
        else:
            self.__root: Node = Node(info)

    def get_root(self) -> Node:
        return self.__root

    def draw(self) -> None:
        if self.__root != None:
            print(self.__root.get_info())
            self.__draw(self.__root, 0)

    def __draw(self, node: Node, spaces: int) -> None:
        iterator : int = 0
        while node.get(iterator) != None:
            iterator = iterator +1 
            print(f'{" " * spaces}|--{str(node.get(iterator))}');
            if node.get(0).get(0) != None:
                self.__draw(node, spaces + 3);
    
    
