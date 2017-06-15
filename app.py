import tkinter as tk
from PIL import ImageTk, Image
from functools import partial # to be able to pass arguments to buttons/menus

from structures import *

widthpixels = 700
heightpixels = 500
titleBorderWidth = 2
opBorderWidth = 2

class App(object):
    """Interface for the program"""
    def __init__(self, master, title='ADS Helptool'):
        """Initialise the window with menu on the left and bottom"""
        # window
        self.master = master
        self.master.geometry('{}x{}'.format(widthpixels, heightpixels))
        self.master.minsize(width=widthpixels, height=heightpixels)
        self.master.title("ADS Helptool")

        # top-left corner title
        self.titleBorder = tk.Frame(master, highlightthickness=titleBorderWidth, highlightbackground="dim grey", highlightcolor="dim grey")
        self.titleBorder.place(x=-titleBorderWidth, y=-titleBorderWidth)
        self.title = tk.Label(self.titleBorder, text=title, font=("OratorStd", 20))
        self.title.pack(side="top", anchor="w")

        # bottom operation menu border
        self.opBorder = tk.Frame(master, height=100, bg="dim grey")
        self.opBorder.pack(side="bottom", fill="both")
        self.opBorder.pack_propagate(0)

        # bottom operation menu
        self.opMenu = tk.Frame(self.opBorder, height=98)
        self.opMenu.pack(fill="both", expand=1, pady=(2,0))
        self.opMenu.pack_propagate(0)
        self.opMenu.grid_columnconfigure(0, weight=1)

        # bottom Operation text
        self.opText = tk.Label(self.opMenu, text="Operation:", font=("OratorStd", 18))
        self.opText.grid(column=0, row=0, sticky="W", pady=(10,0), padx=(20,0))

        # bottom Operations menu
        self.default = tk.StringVar(self.opMenu)
        self.default.set("Op 1")
        self.operations = tk.OptionMenu(self.opMenu, self.default, "Op 1", "Op 2", "Op 3")
        self.operations.grid(column=0, row=1, sticky="W", padx=(20,0))

        # bottom buttons
        self.rew = tk.Button(self.opMenu, image=rewImg)
        self.rew.grid(column=1, row=0, rowspan=2, pady=(10,0), padx=(0,20))

        self.play = tk.Button(self.opMenu, image=playImg)
        self.play.grid(column=2, row=0, rowspan=2, pady=(10,0), padx=(0,20))

        self.step = tk.Button(self.opMenu, image=stepImg)
        self.step.grid(column=3, row=0, rowspan=2, pady=(10,0), padx=(0,20))

        self.stop = tk.Button(self.opMenu, image=stopImg)
        self.stop.grid(column=4, row=0, rowspan=2, pady=(10,0), padx=(0,20))

        self.fwd = tk.Button(self.opMenu, image=fwdImg)
        self.fwd.grid(column=5, row=0, rowspan=2, pady=(10,0), padx=(0,20))

        # menu bar - in the future should be on the right side
        self.menubar = tk.Menu(self.master)

        # load menu
        self.loadmenu = tk.Menu(self.menubar, tearoff=0)

        # data structures menu
        self.dsmenu = tk.Menu(self.loadmenu, tearoff=0)
        self.dsmenu.add_command(label="Array", command=partial(self._load, "Array"))
        self.dsmenu.add_command(label="Dynamic array", command=partial(self._load, "DArray"))

        # algorithms menu
        self.algmenu = tk.Menu(self.loadmenu, tearoff=0)
        self.algmenu.add_command(label="Sorry nothing is here", command=partial(self._load, ""))

        # filling up load menu
        self.loadmenu.add_cascade(label="Data Structures", menu=self.dsmenu)
        self.loadmenu.add_cascade(label="Algorithms", menu=self.algmenu)
        self.menubar.add_cascade(label="Load", menu=self.loadmenu)

        # add exit option
        self.menubar.add_command(label="Exit", command=self.master.quit)

        self.master.config(menu=self.menubar)


    def _load(self, what):
        """Loads appropriate data structure or algorithm"""
        print("Loading", what)
        self._update_ops(what)

    def _update_ops(self, what):
        """
        Updates operation menu to show operations available for
        given data structure (if data structure is chosen)
        """
        self.default.set(Array._ops[0])
        self.operations['menu'].delete(0, 'end')

        new_choices = Array._ops
        for choice in new_choices:
            self.operations['menu'].add_command(label=choice, command=tk._setit(self.default, choice))


root = tk.Tk()

# load images
rewImg = ImageTk.PhotoImage(Image.open("icons/rew.png"))
playImg = ImageTk.PhotoImage(Image.open("icons/play.png"))
stepImg = ImageTk.PhotoImage(Image.open("icons/step.png"))
stopImg = ImageTk.PhotoImage(Image.open("icons/stop.png"))
fwdImg = ImageTk.PhotoImage(Image.open("icons/fwd.png"))

app = App(root)

root.mainloop()