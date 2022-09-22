from pyscraper.commons import print_error


class Node:
    def __init__(self, info: str) -> None:
        self.__info: str = info
        self.__id: int = 0
        self.__children: list = []
        self.__parent: Node = None  # type: ignore

    def get_info(self) -> str:
        try:
            return self.__info
        except Exception:
            return ""

    def set_info(self, info: str) -> None:
        try:
            self.__info = info
        except Exception as exception:
            print_error(Node.__qualname__, exception)

    def get_id(self) -> int:
        try:
            return self.__id
        except Exception as exception:
            print_error(Node.__qualname__, exception)
            return 0

    def set_id(self, id: int) -> None:
        try:
            self.__id = id
        except Exception as exception:
            print_error(Node.__qualname__, exception)

    def add_child(self, info: str) -> None:
        node: Node = Node(info)
        id: str = f"{self.__id}{len(self.__children) + 1}"
        node.set_id(int(id))
        node.__parent = self
        self.__children.append(node)

    def has_children(self) -> bool:
        if len(self.__children) > 0:
            return True
        else:
            return False

    def get_child(self, index: int) -> "Node":
        try:
            return self.__children[index - 1]
        except Exception:
            return None  # type: ignore

    def get_first_child(self) -> "Node":
        try:
            first_child: Node = self.__children[0]
            return first_child
        except Exception:
            return None  # type: ignore

    def get_last_child(self) -> "Node":
        try:
            return self.__children[-1]
        except Exception:
            return None  # type: ignore

    def get_parent(self) -> "Node":
        return self.__parent

    def get_number_children(self) -> int:
        try:
            number_children : int = len(self.__children)
            return number_children
        except Exception:
            return 0  # type: ignore