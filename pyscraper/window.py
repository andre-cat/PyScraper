from pyscraper import pyscraper
from pyscraper.constants import PATH
from pyscraper.web.webpage import Page
from pyglet import font # type: ignore
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter.ttk import Style as TStyle
from tkinter.ttk import Notebook as TNotebook
from tkinter.ttk import Frame as TFrame
from tkinter.ttk import Label as TLabel

def __quit_message() -> None:
    __scrapt_error_label.configure(text='')

def __check_link() -> None:
    __scrapt_error_label.configure(text='')
    link: str = __scrap_entry.get()
    page: Page = pyscraper.get_html(link)
    if page.get_title == '':
        __scrapt_error_label.configure(text='Invalid URL', foreground='MediumVioletRed')
    else:
        __scrapt_error_label.configure(text='Page downloaded!', foreground='GreenYellow')
        pyscraper.print_html(page)
        pyscraper.write_html(page)
    window.after(2000,__quit_message)

window : Tk = Tk()

window.title('PyScraper')
window['bg'] = 'white'
window.resizable(True, True)

# Set fonts
font.add_directory(PATH + '/resources/fonts/')
font_title: str = 'Superstar'
font_label: str = '04b03'
font_entry: str = 'Pixolletta8px'
font_ntabs: str = 'Silkscreen'

midnight_blue: str = '#031A6B'
indigo_dye: str = '#033860'
cg_blue: str = '#087CA7'
cerulean_crayola: str = '#05B2DC'
medium_violet_red: str = '#C71585'
green_yellow: str = 'GreenYellow'

width: int = 500
height: int = 500
x: int = (int)(window.winfo_screenwidth() / 2 - width / 2)
y: int = (int)(window.winfo_screenheight() / 2 - height / 2)
window.geometry(f'{width}x{height}+{x}+{y}')

style: TStyle = TStyle(window)

style.configure('.', background=indigo_dye, foreground='White', font=(font_label, 12))
style.configure('TNotebook.Tab', padding=[7, 3], font=(font_ntabs, 10), foreground=indigo_dye)

book = TNotebook(window)

# TAB_1
scrap_tab: TFrame = TFrame(master=book)
scrap_tab.grid_columnconfigure(0, weight=1)
scrap_tab.grid_rowconfigure(0, weight=1)
scrap_tab.grid_rowconfigure(1, weight=1)
scrap_tab.grid_rowconfigure(2, weight=1)

scrap_title: TLabel = TLabel(master=scrap_tab, text='HTML -> Tree', font=(font_title, 25))
scrap_title.grid(row=0, column=0)

scrap_entry_frame: TFrame = TFrame(master=scrap_tab)
scrap_entry_frame.grid(row=1, column=0, padx=30, sticky='ew')

scrap_entry_label: TLabel = TLabel(master=scrap_entry_frame, text='Enter a link to generate a site structure tree:')
scrap_entry_label.pack(side='top', fill='x', pady=5)

__scrap_entry = Entry(master=scrap_entry_frame, background='White', foreground='Grey', font=(font_entry, 11), justify='center')
__scrap_entry.insert(0, 'about:blank')
__scrap_entry.pack(side='top', fill='both', expand=True, pady=5)

__scrapt_error_label = Label(master=scrap_entry_frame, font=(font_ntabs, 11), background=indigo_dye)
__scrapt_error_label.pack(side='top', fill='both', expand=True, pady=5)

scrap_button: Button = Button(master=scrap_tab, text='Scrap', font=(font_title, 20), foreground=cerulean_crayola, background='White', width=7, borderwidth=0, command=__check_link)
scrap_button.grid(row=2, column=0, pady=1)

book.add(scrap_tab, text='Web Scrapper')
book.pack(expand=True, fill='both')

window.mainloop()
# End window
