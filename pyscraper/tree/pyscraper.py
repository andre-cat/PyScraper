from nary_tree import NaryTree as Tree

class PyScraper:
    def run():
        tree: Tree = Tree()

        tree.get_root().add_son(1)
        tree.get_root().add_son(2)
        tree.get_root().add_son(3)
        
        tree.get_root().get_son(3).add_son(31)
        tree.get_root().get_son(3).add_son(31)

        tree.get_root().get_son(2).add_son(21)
        tree.get_root().get_son(2).get_son(1).add_son(3)

        tree.draw();

if __name__ == "pyscraper":
    PyScraper.run()
