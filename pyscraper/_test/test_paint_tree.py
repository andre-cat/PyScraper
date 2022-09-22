from tkinter import Tk
from tkinter import Frame
from tkinter import Canvas
from tkinter import Scrollbar
from pyscraper.scrap.tree import Tree
from pyscraper.scrap.node import Node

def paint_tree(canvas: Canvas, tree: Tree):
    if tree.get_root() != None:
        children_per_level: dict = tree.get_children_per_level()
        visited_per_level: dict = {}

        tree_width: int = 0
        tree_heigth : int = 0

        for level in children_per_level:
            tree_heigth = tree_heigth + 1
            visited_per_level[level] = 0
            if children_per_level[level] > tree_width:
                tree_width = children_per_level[level]

        # Node diameter
        d: int = 2 * tree.get_largest_info() * 8
        r: int = d / 2

        # Window width and heigth
        w: int = (tree_width * 2 - 1) * d
        h: int = (tree_heigth * 2 - 1) * d

        canvas.create_line(0,0,w,0,fill='black')
        canvas.create_line(0,0,0,h,fill='black')
        canvas.create_line(w,0,w,h,fill='black')
        canvas.create_line(0,h,w,h,fill='black')

        queue: list = []
        queue.append(tree.get_root())

        # Initial vertical position
        xi : int = 0
        yi : int = 0

        father: dict = {1: [xi, yi]}

        while len(queue) > 0:
            node: Node = queue[0]

            queue.pop(0)

            current_level = len(str(node.get_id()))
            visited_per_level[current_level] = visited_per_level[current_level] + 1
            current_node = visited_per_level[current_level]
            nodes_in_level = children_per_level[current_level]
            
            x = w/2 - (((2*nodes_in_level - 1) - 1) * d)/2 + (((2*current_node - 1) - 1) * d) - r
            y = ((2*current_level - 1) - 1) * d

            #print(node.get_id(),x,y)

            canvas.create_oval(x, y, x + d, y + d, fill="blue", width=0)

            xf : int = father[node.get_id()][0]
            yf : int = father[node.get_id()][1]

            canvas.create_text(x + r, y + r, text=node.get_info(), fill="white", font=('Consolas', 12))
            if node.get_id() != 1:
                canvas.create_line(x+r, y, xf+r, yf+d, dash=3, width=1)

            for number_child in range(node.get_number_children() - 1, -1, -1):
                father[node.get_child(number_child).get_id()] = [x, y]
                queue.append(node.get_child(number_child))


tree: Tree = Tree("uj")
tree.get_root().add_child("A")
tree.get_root().get_child(1).add_child("B")
tree.get_root().get_child(1).add_child("C")
tree.get_root().add_child("D")
tree.get_root().get_child(2).add_child("E")
tree.get_root().get_child(2).add_child("F")
tree.get_root().get_child(2).get_child(1).add_child('z')

window = Tk()

width: int = 700
height: int = 600
x: int = (int)(window.winfo_screenwidth() / 2 - width / 2)
y: int = (int)(window.winfo_screenheight() / 2 - height / 2)
window.geometry(f"{width}x{height}+{x}+{y}")

window.title("PyScraper")
window.resizable(True, True)

# Fonts
# Colors
color_cg_blue: str = "#087CA7"
color_midnight_blue: str = "#031A6B"
color_light_slate_gray = "#778899"
color_white: str = "#FFFFFF"
color_black: str = "#000000"

###########################################################################

tree_tab: Frame = Frame(master=window)
tree_tab.pack(expand=True, fill="both")

tree_container = Frame(master=tree_tab)
tree_container.grid_columnconfigure(0, weight=1)
tree_container.grid_columnconfigure(1, weight=0)
tree_container.grid_rowconfigure(0, weight=1)
tree_container.grid_rowconfigure(1, weight=0)
tree_container.pack(expand=True, fill="both")

tree_canvas = Canvas(master=tree_container, background="white")
tree_canvas.grid(row=0, column=0, sticky="nsew")

tree_scrollbar_ver = Scrollbar(master=tree_container, orient="vertical", command=tree_canvas.yview)
tree_scrollbar_ver.grid(row=0, column=1, sticky="ns")

tree_scrollbar_hor = Scrollbar(master=tree_container, orient="horizontal", command=tree_canvas.xview)
tree_scrollbar_hor.grid(row=1, column=0, sticky="ew")

tree_frame = Frame(master=tree_canvas)
tree_canvas.create_window((0, 0), window=tree_frame, anchor="nw")

tree_canvas.bind("<Configure>", lambda f: tree_canvas.configure(scrollregion=tree_canvas.bbox("all")))
tree_canvas.configure(yscrollcommand=tree_scrollbar_ver.set)
tree_canvas.configure(xscrollcommand=tree_scrollbar_hor.set)

paint_tree(tree_canvas, tree)

window.mainloop()
