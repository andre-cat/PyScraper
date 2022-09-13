from pyscraper.web.page import Page
from pyscraper.scrap.tree import Tree
from pyscraper.paint import window
from tkinter import Tk
from tkinter import Frame
from tkinter import Canvas
from pyscraper.web.browser import Page
from pyscraper.scrap.node import Node
from pyscraper.scrap.tree import Tree
from pyscraper.paint.paint import Paint

def show_window():
    window.show()

def get_paint(tree : Tree, tag_page : str, page : Page):
    Paint(tree, tag_page, page)

def draw_tree(t: Tree, frame : Frame, width : int, height, d : int = 20) -> Frame:
    c = Canvas(frame, width=width, height=height)
    c.pack()

    x : int = int(width/2)
    y : int = 1

    c.create_oval(x, y, x+d, y+d)
    c.create_text(x+d/2, y+d/2, text=t.get_root().get_info())

    __draw_tree(t.get_root(),x,y)

    window.mainloop()

def __draw_tree(canvas: Canvas, node:Node, x:int, y:int, d : int = 20) -> None:
    if node != None:
        iterator: int = 1
        y = y + (d*2)
        x = x - int((((node.get_number_children() * 2)+1)*d)/2)     
        while node.get_child(iterator) != None:
            x = x + d
            canvas.create_oval(x, y, x+d, y+d, fill="red")
            canvas.create_text(x, y, text=node.get_child(iterator).get_info())
            iterator = iterator + 1
            x = x + d