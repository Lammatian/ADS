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
        self.title = Label(self.titleBorder, text=title, font=("Verdana", 20))
        self.title.pack(side="top", anchor="w")

        self.opBorder = Frame(master, width=widthpixels+5, height=100, highlightthickness=opBorderWidth, highlightbackground="grey", highlightcolor="grey")
        self.opBorder.place(x=-2, y=402)
        self.opBorder.place_propagate(0)
        self.opText = Label(self.opBorder, text="Operation:", font=("Verdana", 18))
        self.opText.pack(side="top", anchor="w")


root = Tk()

app = App(root)

root.mainloop()