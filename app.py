from tkinter import *

widthpixels = 700
heightpixels = 500
titleBorderWidth = 2
opBorderWidth = 2

class App(object):
    """Interface for the program"""
    def __init__(self, master, title='ADS helptool'):
        """Initialise the window with menu on the left and bottom"""
        master.geometry('{}x{}'.format(widthpixels, heightpixels))

        self.titleBorder = Frame(master, highlightthickness=titleBorderWidth, highlightbackground="grey", highlightcolor="grey")
        self.titleBorder.place(x=-titleBorderWidth, y=-titleBorderWidth)
        self.title = Label(self.titleBorder, text=title, font=("OratorStd", 20))
        self.title.pack(side="top", anchor="w")

        self.opBorder = Frame(master, height=100, bg="grey")
        self.opBorder.pack(side="bottom", fill=BOTH)
        self.opBorder.pack_propagate(0)

        self.opMenu = Frame(self.opBorder, height=98)
        self.opMenu.pack(side="bottom", fill=BOTH)
        self.opMenu.pack_propagate(0)

        self.opText = Label(self.opMenu, text="Operation:", font=("OratorStd", 18))
        self.opText.pack(side="top", anchor="w", padx=(10,0), pady=(10,0))

        self.operation = Label(self.opMenu, text="current op", font=("OratorStd", 12), fg="green")
        self.operation.pack(side="top", anchor="w", padx=(10,0))


root = Tk()

app = App(root)

root.mainloop()