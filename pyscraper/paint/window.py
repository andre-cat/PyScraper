from pyglet import font  # type: ignore
from tkinter.ttk import Style as TStyle
from tkinter.ttk import Notebook as TNotebook
from tkinter.ttk import Frame as TFrame
from tkinter.ttk import Label as TLabel
from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Text
from tkinter import Canvas
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk  # type: ignore
from pyscraper import pyscraper
from pyscraper.commons import PATH
from pyscraper.web.browser import Page
from pyscraper.scrap.tree import Tree
from sys import exc_info  # type : ignore

__window: Tk
__scrap_entry: Entry
__scrap_error_label: Label
__log_scroll: ScrolledText


def __check_page() -> None:
    try:
        link: str = __scrap_entry.get()
        page: Page = pyscraper.get_page(link)
        __add_message(text="Page downloaded!", error=False)
        __scrap_page(page)
    except Exception as exception:
        __add_message(text=f"ERROR DOWNLOADING PAGE", error=True)
        __add_log(str(exception))


def __scrap_page(page: Page) -> None:
    try:
        pyscraper.print_page(page)
        tree: Tree = pyscraper.get_tree(page)
        tag_page: str = pyscraper.get_tag_page(page)
        __paint_page(tree, tag_page, page)
    except Exception as exception:
        __add_message(text=f"ERROR SCRAPING THE PAGE", error=True)
        __add_log(str(exception))


def __paint_page(tree: Tree, tag_page: str, page: Page) -> None:
    try:
        pyscraper.get_paint(tree, tag_page, page)
    except Exception as exception:
        __add_message(text=f"ERROR PAINTING THE PAGE", error=True)
        __add_log(str(exception))


def __add_message(text: str, error: bool) -> None:
    color: str
    if error != True:
        color_medium_violet_red: str = "#32CD32"
        color = color_medium_violet_red
    else:
        color_green_yellow: str = "#C71585"
        color = color_green_yellow
    __scrap_error_label.configure(text=text, foreground=color)
    __window.after(3000, __quit_message)


def __quit_message() -> None:
    __scrap_error_label.configure(text="")


def __add_log(error: str) -> None:
    __log_scroll.configure(state="normal")
    __log_scroll.insert("end", __name__ + ": " + error + "\n\n")
    __log_scroll.configure(state="disabled")


def show():
    global __window
    __window = Tk()
    try:
        __window.title("PyScraper")
        __window["bg"] = "Black"
        __window.resizable(True, True)

        width: int = 500
        height: int = 600
        x: int = (int)(__window.winfo_screenwidth() / 2 - width / 2)
        y: int = (int)(__window.winfo_screenheight() / 2 - height / 2)
        __window.geometry(f"{width}x{height}+{x}+{y}")

        # Fonts
        font.add_directory(PATH + "/resources/fonts/")
        font_tabs: str = "Silkscreen"
        font_title: str = "Superstar"
        font_label: str = "04b03"
        font_entry: str = "Pixolletta8px"
        font_text: str = "Free Pixel"

        # Colors
        color_yale_blue: str = "#004385"
        color_indigo_dye: str = "#033860"
        color_cerulean_crayola: str = "#05B2DC"
        color_cg_blue: str = "#087CA7"
        color_gainsboro: str = "Gainsboro"
        color_white: str = "#FFFFFF"
        color_black: str = "#000000"
        color_lime: str = "#ADFF2F"

        # Style
        style: TStyle = TStyle(__window)
        style.configure(".", background=color_indigo_dye, foreground=color_white, font=(font_label, 12))
        style.configure("TNotebook.Tab", padding=[7, 3], font=(font_tabs, 11), background=color_yale_blue, foreground=color_yale_blue)

        book = TNotebook(__window)

        # TAB_1
        scrap_tab: TFrame = TFrame(master=book)
        scrap_tab.grid_columnconfigure(0, weight=1)
        scrap_tab.grid_rowconfigure(0, weight=1)
        scrap_tab.grid_rowconfigure(1, weight=1)
        scrap_tab.grid_rowconfigure(2, weight=1)

        scrap_title: TLabel = TLabel(master=scrap_tab, text="WebPage -> Tree", font=(font_title, 25))
        scrap_title.grid(row=0, column=0, pady=20)

        scrap_image = ImageTk.PhotoImage(Image.open(PATH + "/resources/images/tree.png").resize((150, 150)))

        scrap_canvas = Canvas(scrap_tab, bg=color_indigo_dye, width=scrap_image.width(), height=scrap_image.height(), bd=0, highlightthickness=0, relief="flat")
        scrap_canvas.create_image(scrap_image.width() / 2, scrap_image.height() / 2, image=scrap_image, anchor="center")
        scrap_canvas.grid(row=1, column=0)

        scrap_entry_frame: TFrame = TFrame(master=scrap_tab)
        scrap_entry_frame.grid(row=2, column=0, pady=20, padx=30, sticky="ew")

        scrap_entry_label: TLabel = TLabel(master=scrap_entry_frame, text="Enter a link to generate a site structure tree:")
        scrap_entry_label.pack(side="top", fill="x")

        global __scrap_entry
        __scrap_entry = Entry(master=scrap_entry_frame, background=color_cg_blue, foreground=color_white, font=(font_entry, 11), justify="center", border=0, insertbackground=color_white, selectbackground=color_lime, selectforeground=color_black)
        #__scrap_entry.insert(0, "about:blank")
        __scrap_entry.insert(0, "https://www.w3schools.com/xml/cd_catalog.xml")
        __scrap_entry.pack(side="top", fill="both", expand=True, pady=5, ipady=3)

        global __scrap_error_label
        __scrap_error_label = Label(master=scrap_entry_frame, font=(font_tabs, 11), background=color_indigo_dye)
        __scrap_error_label.pack(side="top", fill="x", expand=True, pady=10)

        scrap_button: Button = Button(master=scrap_tab, text="Scrap", font=(font_title, 18), foreground=color_cerulean_crayola, background=color_white, width=7, borderwidth=0, command=__check_page)
        scrap_button.grid(row=3, column=0, pady=40)

        # TAB_2

        log_tab: Frame = Frame(master=book, background=color_cg_blue)

        log_frame: Frame = Frame(master=log_tab, background=color_indigo_dye, width=20)
        log_frame.pack(side="left", expand=False, fill="y")

        global __log_scroll
        __log_scroll = ScrolledText(master=log_tab, font=(font_text, 13), foreground=color_gainsboro, background=color_cg_blue, state="disabled", wrap="word", borderwidth=0, border=0, highlightthickness=0)
        __log_scroll.pack(side="left", expand=True, fill="both")

        # TAB_3

        about_tab: TFrame = TFrame(master=book)

        about_text: Text = Text(master=about_tab, background=color_indigo_dye, foreground=color_gainsboro, font=(font_text, 18), wrap="word", highlightthickness=0, bd=0)
        about_text.insert("end", "Web application to visualize web sites using trees (data structure)\n\n")
        about_text.insert("end", "Andrea Arias\n")
        about_text.insert("end", "David Barcos\n")
        about_text.insert("end", "Omar Cifuentes\n")
        about_text.configure(state="disabled")
        about_text.pack(expand=True, fill="both", padx=30, pady=30)

        # NOTEBOOK
        book.add(scrap_tab, text="Web Scrapper")
        book.add(log_tab, text="Error Log", sticky="nsew")
        book.add(about_tab, text="About")
        book.pack(expand=True, fill="both")

        __window.mainloop()

    except Exception as exception:
        exc_type, exc_obj, exc_tb = exc_info()  
        error: str = f"{str(exception)} | {__name__} | Line {exc_tb.tb_lineno} -> " #type:ignore
        raise Exception(error)
