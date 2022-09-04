from pyscraper.pyscraper import PyScraper
from pyscraper.constants import PATH
from pyglet import font
from tkinter import Tk
from tkinter.ttk import Style
from tkinter.ttk import Notebook
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter.scrolledtext import ScrolledText 
from tkinter import constants as tkcons

class Window(Tk):

    def __init__(self):
        super().__init__()
        
        self.title('PyScraper')
        self['bg'] = 'white'

        houses = [None] * 8
        inputs = []
        outputs = []

        # Set fonts
        font.add_directory(PATH + '/resources/fonts/')
        font_title = 'Superstar'
        font_text = '04b03'
        font_misc = '3Dventure'

        midnight_blue = '#031a6b'
        indigo_dye = '#033860'
        cg_blue = '#087ca7'
        yale_blue = '#004385'
        cerulean_crayola = '#05b2dc'

        width = 500
        height = 500
        x = (int)(self.winfo_screenwidth() / 2 - width / 2)
        y = (int)(self.winfo_screenheight() / 2 - height / 2)
        self.geometry(str(width) + 'x' + str(height) + '+' + str(x) + '+' + str(y))

        estyle = Style()
        estyle.configure('TNotebook', background=yale_blue)

        book = Notebook(self)

        link_tab = Frame(master=book, background='red')
        estyle.configure('TFrame', background=indigo_dye)

        # Tab code 1
        tab_1 = Frame(master=book, background=indigo_dye)
        tab_1.grid_columnconfigure(0, weight=1)
        tab_1.grid_rowconfigure([1, 2, 4], weight=1)

        title_1 = Label(master=tab_1, text='PROBLEMA 1', font=(font_title, 25), foreground='White', background=indigo_dye)
        title_1.grid(column=0, row=0, pady=5)

        # Days input
        days_element = Frame(master=tab_1, background=indigo_dye)
        days_element.grid(column=0, row=1)

        days_label = Label(master=days_element, text='Días de competencia en el vecindario:', font=(font_text, 12), foreground='White', background=indigo_dye)
        days_label.pack(side=tkcons.TOP)

        days_input = Entry(master=days_element, font=(font_text, 12), foreground=midnight_blue, background='GreenYellow', justify=tkcons.CENTER, width=4)
        days_input.insert(0, '')
        days_input.pack(side=tkcons.TOP)

        days_error = Label(master=days_element, font=(font_text, 10), foreground='#ff0095', background=indigo_dye)
        days_error.pack(side=tkcons.TOP, fill=tkcons.BOTH, expand=True)
        # End days input

        # Inputs problem 1
        input_element = Frame(master=tab_1, background=indigo_dye)
        input_element.grid(column=0, row=2)

        input_label = Label(master=input_element, text='Entradas:', font=(font_text, 12), foreground='White', background=indigo_dye)
        input_label.pack(side=tkcons.TOP)

        big_box_1 = Frame(master=input_element, background=indigo_dye)
        big_box_1.pack(side=tkcons.TOP)

        for index in range(len(houses)):
            box = Frame(master=big_box_1, background=indigo_dye, borderwidth=0)
            box.grid(row=0, column=index, padx=5)

            my_input = Entry(master=box, font=(font_text, 12), foreground=midnight_blue, background='GreenYellow', justify=tkcons.CENTER, width=3)
            my_input.insert(0, '')
            my_input.pack(side=tkcons.TOP)
            inputs.append(my_input)

            number = Label(master=box, text=(index + 1), font=(font_text, 12), foreground='White', background=indigo_dye)
            number.pack(side=tkcons.TOP)

        input_error = Label(master=input_element, font=(font_text, 10), foreground='#ff0095', background=indigo_dye)
        input_error.pack(side=tkcons.TOP, fill=tkcons.BOTH, expand=True)
        # End inputs problem 1

        button_1 = Button(master=tab_1, text='Calcular', font=(font_title, 12), foreground=cerulean_crayola, background='White', borderwidth=0, command=PyScraper.do_this)
        button_1.grid(column=0, row=3, pady=1)

        # Outputs problem 1
        output_element = Frame(master=tab_1, background=indigo_dye)
        output_element.grid(column=0, row=4)

        output_label = Label(master=output_element, text='Salidas:', font=(font_text, 12), foreground='White', background=indigo_dye)
        output_label.pack(side=tkcons.TOP, fill=tkcons.BOTH, expand=True)

        big_box_2 = Frame(master=output_element, background=cg_blue)
        big_box_2.pack(side=tkcons.TOP)

        for index in range(8):
            box = Frame(master=big_box_2, background=indigo_dye, borderwidth=0)
            box.grid(row=0, column=index)

            my_output = Label(master=box, text='', font=(font_text, 12, 'bold'), foreground='White', background=cg_blue, width=4)
            my_output.pack(side=tkcons.TOP)
            outputs.append(my_output)

            number = Label(master=box, text=(index + 1), font=(font_text, 12), foreground='White', background=indigo_dye)
            number.pack(side=tkcons.TOP)
        # End outputs problem 1
        # End tab code 1

        # Tab code 2
        tab_2 = Frame(master=book, background=indigo_dye)
        tab_2.grid_columnconfigure(0, weight=1)
        tab_2.grid_rowconfigure([0, 1, 2, 3], weight=1)

        title_2 = Label(master=tab_2, text='PROBLEMA 2', font=(font_title, 25), foreground='White', background=indigo_dye)
        title_2.grid(column=0, row=0)

        # Input problem 2
        string_element = Frame(tab_2, background=indigo_dye)
        string_element.grid(column=0, row=1)

        string_label = Label(master=string_element, text='Cadena a permutar:', font=(font_text, 12), foreground='White', background=indigo_dye)
        string_label.pack(side=tkcons.TOP)

        string_input = Entry(master=string_element, font=(font_text, 12), foreground=midnight_blue, background='GreenYellow', justify=tkcons.CENTER, width=30)
        string_input.insert(0, '')
        string_input.pack(side=tkcons.TOP)
        # En input problem 2

        button_2 = Button(master=tab_2, text='Permutar', font=(font_title, 12), foreground=cerulean_crayola, background='White', borderwidth=0, command=PyScraper.do_this)
        button_2.grid(column=0, row=2)

        # Output problem 2
        permutation_element = Frame(tab_2, background=indigo_dye)
        permutation_element.grid(column=0, row=3, sticky=tkcons.EW, padx=100)

        permutation_label = Label(master=permutation_element, text='Permutaciónes:', font=(font_text, 12), foreground='White', background=indigo_dye)
        permutation_label.pack(side=tkcons.TOP)

        permutation_output = ScrolledText(master=permutation_element, font=(font_text, 12), foreground='White', background=cg_blue, width=30, height=7, state=tkcons.DISABLED, wrap=tkcons.WORD)
        permutation_output.pack(side=tkcons.TOP, fill=tkcons.BOTH, expand=True)
        # End output problem 2
        # End code 2

        book.add(link_tab, text='Scraper')
        book.add(tab_1, text='Scrapper')
        book.add(tab_2, text='About')
        book.pack(expand=True, fill=tkcons.BOTH)

        permutation_output.focus()

        self.mainloop()
        # End self