import unittest
from pyscraper.scrap.tree import Tree
from pyscraper.paint import painter
from pyscraper.commons import print_error

class TestTree(unittest.TestCase):
    def test_paint(self) -> None:

        try:
            tree: Tree = Tree("Z")
            tree.get_root().add_child("A")
            tree.get_root().get_child(1).add_child("B")
            tree.get_root().get_child(1).add_child("C")
            tree.get_root().add_child("D")
            tree.get_root().get_child(2).add_child("E")
            tree.get_root().get_child(2).add_child("F")
            

        except Exception as exception:
            print_error(__name__, exception)

if __name__ == "__main__":
    unittest.main()
