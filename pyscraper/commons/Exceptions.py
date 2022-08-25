class NodeException(Exception):
    def __init__(self, message: str):
        self.__message = 'Node exception: ' + message;

class ListException(Exception):
    def __init__(self, message: str):
        self.__message = 'List exception: ' + message;

class TreeException(Exception):
    def __init__(self, message: str):
        self.__message = 'Tree exception: ' + message;