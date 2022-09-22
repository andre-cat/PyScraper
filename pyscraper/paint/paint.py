from pyglet import font  # type: ignore
from tkinter.ttk import Style as TStyle
from tkinter.ttk import Frame as TFrame
from tkinter.ttk import Notebook as TNotebook
from tkinter import Tk
from tkinter import Frame
from tkinter import Canvas
from tkinter import Scrollbar
from tkinter.scrolledtext import ScrolledText
from pyscraper.scrap.node import Node
from pyscraper.commons import PATH
from pyscraper.web.browser import Page
from pyscraper.scrap.tree import Tree
from sys import exc_info  # type : ignore


class Paint(Tk):
    def __init__(self, tree: Tree, tag_page: str, page: Page) -> None:
        super().__init__()
        try:

            width: int = 700
            height: int = 600
            x: int = (int)(self.winfo_screenwidth() / 2 - width / 2)
            y: int = (int)(self.winfo_screenheight() / 2 - height / 2)
            self.geometry(f"{width}x{height}+{x}+{y}")

            self.title("PyScraper")
            self["bg"] = "White"
            self.resizable(True, True)

            # Fonts
            font.add_directory(PATH + "/resources/fonts/")
            font_tabs: str = "Silkscreen"
            font_title: str = "Superstar"
            font_label: str = "04b03"
            font_text: str = "Free Pixel"

            # Colors
            color_cg_blue: str = "#087CA7"
            color_white: str = "#FFFFFF"
            color_black: str = "#000000"

            style: TStyle = TStyle(self)

            style.configure(".", background=color_white, foreground=color_cg_blue, font=(font_label, 12))
            style.configure("TNotebook.Tab", padding=[7, 3], font=(font_tabs, 10))

            ###########################################################################

            book = TNotebook(self)

            # TAB_1
            tree_tab: TFrame = TFrame(master=book)

            tree_container = Frame(master=tree_tab)
            tree_container.grid_columnconfigure(0, weight=1)
            tree_container.grid_columnconfigure(1, weight=0)
            tree_container.grid_rowconfigure(0, weight=1)
            tree_container.grid_rowconfigure(1, weight=0)
            tree_container.pack(expand=True, fill="both")

            tree_canvas = Canvas(master=tree_container)
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

            self.paint_tree(tree_canvas, tree)

            # TAB_2
            tag_tab: TFrame = TFrame(master=book)

            tag_scroll: ScrolledText = ScrolledText(master=tag_tab, font=(font_text, 13), foreground="Black", background=color_white, wrap="none", borderwidth=0, border=0, highlightthickness=0)
            tag_scroll.insert("end", tag_page)
            tag_scroll.configure(state="disabled")
            tag_scroll.pack(side="top", expand=True, fill="both")

            # TAB_3
            ides_tab: TFrame = TFrame(master=book)

            ides_scroll = ScrolledText(master=ides_tab, font=(font_text, 13), foreground=color_black, background=color_white, wrap="none", borderwidth=0, border=0, highlightthickness=0)
            ides_scroll.insert("end", tree.get_stream(id=True))
            ides_scroll.configure(state="disabled")
            ides_scroll.pack(side="left", expand=True, fill="both")

            # TAB_5
            rows_tab: TFrame = TFrame(master=book)

            rows_scroll = ScrolledText(master=rows_tab, font=(font_text, 13), foreground=color_black, background=color_white, wrap="none", borderwidth=0, border=0, highlightthickness=0)
            rows_scroll.insert("end", tree.get_stream(id=False))
            rows_scroll.configure(state="disabled")
            rows_scroll.pack(side="left", expand=True, fill="both")

            # TAB_
            source_tab: TFrame = TFrame(master=book)

            source_scroll = ScrolledText(master=source_tab, font=(font_text, 13), foreground=color_black, background=color_white, wrap="none", borderwidth=0, border=0, highlightthickness=0)
            source_scroll.insert("end", page.get_source())
            source_scroll.configure(state="disabled")
            source_scroll.pack(side="left", expand=True, fill="both")

            #################################################################

            book.add(tree_tab, text="Tree")
            book.add(tag_tab, text="Tag Source")
            book.add(ides_tab, text="ID Source")
            book.add(rows_tab, text="Rows Source")
            book.add(source_tab, text="Source")

            book.pack(expand=True, fill="both")

            self.mainloop()

        except Exception as exception:
            exc_type, exc_obj, exc_tb = exc_info()
            error: str = f"{str(exception)} | {Paint.__qualname__} | Line {exc_tb.tb_lineno} -> "  # type:ignore
            raise Exception(error)

    @staticmethod
    def paint_tree(canvas: Canvas, tree: Tree):
        try:
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
                #d: int = 2 * tree.get_largest_info() * 8
                d: int = 10
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
                    y = ((2*current_level - 1) - 1) * d * (0.1*nodes_in_level)

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

        except Exception as exception:
            exc_type, exc_obj, exc_tb = exc_info()
            error: str = f"{str(exception)} | {Paint.__qualname__} | Line {exc_tb.tb_lineno} -> "  # type:ignore
            raise Exception(error)
