from pyglet import font  # type: ignore
from tkinter.ttk import Style as TStyle
from tkinter.ttk import TFrame
from tkinter.ttk import Notebook as TNotebook
from tkinter import Tk
from tkinter import Frame
from tkinter import Canvas
from tkinter.scrolledtext import ScrolledText
from pyscraper.paint import painter
from pyscraper.commons import PATH
from pyscraper.web.browser import Page
from pyscraper.scrap.tree import Tree


class Paint(Tk):
    def __init__(self, tree: Tree, tag_page: str, page: Page) -> None:
        super().__init__()

        width: int = 800
        height: int = 600
        x: int = (int)(self.winfo_screenwidth() / 2 - width / 2)
        y: int = (int)(self.winfo_screenheight() / 2 - height / 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

        self.title("PyScraper")
        self["bg"] = "White"
        self.resizable(True, True)

        # Fonts
        font.add_directory(PATH + "/resources/fonts/")
        font_label: str = "04b03"
        font_tabs: str = "Silkscreen"
        font_text: str = "Free Pixel"

        # Colors
        color_cg_blue: str = "#087CA7"
        color_midnight_blue: str = "#031A6B"
        color_light_slate_gray = "#778899"
        color_white: str = "#FFFFFF"
        color_black: str = "#000000"

        style: TStyle = TStyle(self)

        style.configure(".", background=color_white, foreground=color_cg_blue, font=(font_label, 12))
        style.configure("TNotebook.Tab", padding=[7, 3], font=(font_tabs, 10))

        book = TNotebook(self)

        # TAB_1
        tree_tab: Frame = Frame(master=book)
        frame : Frame(tree_tab)
        width : int = 1000
        heigth : int = 1000
        canvas : Canvas = painter.draw_tree(tree, frame, width, height)


        # TAB_2
        tag_tab: TFrame = TFrame(master=book)

        tab_scroll = ScrolledText(master=tag_tab, font=(font_text, 13), foreground="Black", background=color_white, wrap="none", borderwidth=0, border=0, highlightthickness=0)
        tab_scroll.pack(side="left", expand=True, fill="both")
        tab_scroll.insert("end", tag_page)
        tab_scroll.configure(state="disabled")

        # TAB_3
        print_tab: TFrame = TFrame(master=book)

        print_scroll = ScrolledText(master=print_tab, font=(font_text, 13), foreground=color_light_slate_gray, background=color_white, wrap="none", borderwidth=0, border=0, highlightthickness=0)
        print_scroll.pack(side="left", expand=True, fill="both")
        print_scroll.insert("end", tree.get_stream(True))
        print_scroll.configure(state="disabled")

        # TAB_4
        source_tab: TFrame = TFrame(master=book)

        source_scroll = ScrolledText(master=source_tab, font=(font_text, 13), foreground=color_black, background=color_white, wrap="none", borderwidth=0, border=0, highlightthickness=0)
        source_scroll.pack(side="left", expand=True, fill="both")
        source_scroll.insert("end", page.get_source())
        source_scroll.configure(state="disabled")

        book.add(tree_tab, text="Tree")
        book.add(tag_tab, text="Page With Tags Only")
        book.add(print_tab, text="Page With IDs")
        book.add(source_tab, text="Page Source")

        book.pack(expand=True, fill="both")
