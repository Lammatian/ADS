import tkinter as tk
from PIL import ImageTk, Image
from functools import partial # to be able to pass arguments to buttons/menus
import inspect # to get functions in a class
import sys
from types import FunctionType
import argDialog
import ast # to pass proper arguments
from resizingCanvas import ResizingCanvas
import tkinter.messagebox as mbox # for help messages

from structures import *

widthpixels = 700
heightpixels = 500
titleBorderWidth = 2
opBorderWidth = 2


# Animation classes available for the user to pick from in the `load` -> `data structures` menu item.
AVAILABLE_ANIMATIONS = [
    A_Array,
    A_DArray,
    A_Stack,
    A_Queue,
    A_LinkedList
]


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
        self.title = tk.Label(self.titleBorder, text=title, font=("OratorStd", 20), bg="white")
        self.title.pack(side="top", anchor="w")

        # bottom operation menu border
        self.opBorder = tk.Frame(master, height=100, bg="dim grey")
        self.opBorder.pack(side="bottom", fill="both")
        self.opBorder.pack_propagate(0)

        # bottom operation menu
        self.opMenu = tk.Frame(self.opBorder, height=98, bg="white")
        self.opMenu.pack(fill="both", expand=1, pady=(2,0))
        self.opMenu.pack_propagate(0)
        self.opMenu.grid_columnconfigure(0, weight=1)

        # bottom Operation text
        self.opText = tk.Label(self.opMenu, text="Operation:", font=("OratorStd", 18), bg="white")
        self.opText.grid(column=0, row=0, sticky="W", pady=(10,0), padx=(20,0))

        # bottom Operations menu
        self.default = tk.StringVar(self.opMenu)
        self.default.set("Op1")
        self.operations = tk.OptionMenu(self.opMenu, self.default, "Op1", "Op2", "Op3")
        self.operations.grid(column=0, row=1, sticky="W", padx=(20,0))

        # bottom buttons
        self.rew = tk.Button(self.opMenu, image=rewImg)
        self.rew.grid(column=1, row=0, rowspan=2, pady=(10,0), padx=(0,20))

        self.play = tk.Button(self.opMenu, image=playImg, command=self._perform)
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

        for animation_class in AVAILABLE_ANIMATIONS:
            self.dsmenu.add_command(label=animation_class._title, command=partial(self._load, animation_class))

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
        self.master.bind("<Return>", self._perform)

        # for arrow key scrolling through operations
        self.operation_options = ["Op1", "Op2", "Op3"]
        self.current_op = 0
        self.master.bind("<Down>", self._down_scroll)
        self.master.bind("<Up>", self._up_scroll)

        # for getting function documentation
        self.master.bind("<Key-h>", self._get_help)

        # fast exiting
        self.master.bind("<Key-q>", lambda event: self.master.quit())

        # return value label
        self.returnVal = tk.Label(self.master, text="Return value", font=("OratorStd", 12))
        self.returnVal.pack(side="bottom", anchor="w")

        # canvas for presenting data structures
        self.canvas = ResizingCanvas(master)
        self.canvas.pack(pady=(50,0), fill=tk.BOTH, expand=True)


    def _load(self, what):
        """Loads appropriate data structure or algorithm"""
        self.title.config(text=what._title)
        print("Loading", what)
        if what:
            self._update_ops(what)


    def _update_ops(self, what):
        """
        Updates operation menu to show operations available for
        given data structure (if data structure is chosen)
        """
        self.operations['menu'].delete(0, 'end')

        self.public_functions = {func.__name__: func for func in what.animations}
        self.operation_options = sorted(list(self.public_functions.keys()))
        self.default.set(self.operation_options[0])

        for op in self.operation_options:
            self.operations['menu'].add_command(label=op, command=tk._setit(self.default, op))

        self._initialise_ds(what)


    def _initialise_ds(self, what):
        """
        Initialise a data structure inside a dialog window
        where all the arguments can be given
        """
        self.canvas.delete(tk.ALL)

        if self._get_arguments(what.__init__):
            argDial = argDialog.ArgDialog(self.master, self._get_arguments(what.__init__), "Initialisation")
            # initialise the data structure
            self.ds = what(self.canvas, *[ast.literal_eval(r) for r in argDial.result])
        else:
            self.ds = what(self.canvas)

        self.canvas.item = self.ds


    def _perform(self, event=None):
        """
        Perform given function

        May ask for additional parameters
        if the function has arguments
        """
        # get the function to be performed from the list of public functions
        # which was initialised in _update_ops
        function = self.public_functions[self.default.get()]

        if self._get_arguments(function):
            argDial = argDialog.ArgDialog(self.master, self._get_arguments(function), "Give parameters")
            result = function(self.ds, *[ast.literal_eval(r) for r in argDial.result])
        else:
            result = function(self.ds)

        if result != None:
            self.returnVal['text'] = "Return value: " + str(result)
        else:
            self.returnVal['text'] = "No return value"


    def _get_arguments(self, function):
        """Gets the arguments of a given function"""
        if function.__name__ == "__init__":
            # to omit canvas in initialisation
            return function.__code__.co_varnames[2:function.__code__.co_argcount]
        else:
            return function.__code__.co_varnames[1:function.__code__.co_argcount]


    def _get_help(self, event):
        """Get help for chosen operation"""
        if self.ds:
            mbox.showinfo("{}: {}".format(self.ds._title, self.public_functions[self.default.get()].__name__),\
                          "How the hell do you get docstring of super function?")


    def _down_scroll(self, event):
        """Scroll down the option menu"""
        self.current_op = (self.current_op + 1)%len(self.operation_options)
        self.default.set(self.operation_options[self.current_op])


    def _up_scroll(self, event):
        """Scroll up the option menu"""
        self.current_op = (self.current_op - 1)%len(self.operation_options)
        self.default.set(self.operation_options[self.current_op])


root = tk.Tk()

# load images
rewImg = ImageTk.PhotoImage(Image.open("icons/rew.png"))
playImg = ImageTk.PhotoImage(Image.open("icons/play.png"))
stepImg = ImageTk.PhotoImage(Image.open("icons/step.png"))
stopImg = ImageTk.PhotoImage(Image.open("icons/stop.png"))
fwdImg = ImageTk.PhotoImage(Image.open("icons/fwd.png"))

app = App(root)

root.mainloop()