from tkinter import *
from PIL import ImageTk, Image

widthpixels = 700
heightpixels = 500
titleBorderWidth = 2
opBorderWidth = 2

class App(object):
    """Interface for the program"""
    def __init__(self, master, title='ADS Helptool'):
        """Initialise the window with menu on the left and bottom"""
        self.master = master
        self.master.geometry('{}x{}'.format(widthpixels, heightpixels))
        self.master.minsize(width=widthpixels, height=heightpixels)
        self.master.title("ADS Helptool")

        self.titleBorder = Frame(master, highlightthickness=titleBorderWidth, highlightbackground="grey", highlightcolor="grey")
        self.titleBorder.place(x=-titleBorderWidth, y=-titleBorderWidth)
        self.title = Label(self.titleBorder, text=title, font=("OratorStd", 20))
        self.title.pack(side="top", anchor="w")

        self.opBorder = Frame(master, height=100, bg="grey")
        self.opBorder.pack(side="bottom", fill=BOTH)
        self.opBorder.pack_propagate(0)

        self.opMenu = Frame(self.opBorder, height=98)
        self.opMenu.pack(fill=BOTH, expand=1, pady=(2,0))
        self.opMenu.pack_propagate(0)
        self.opMenu.grid_columnconfigure(0, weight=1)

        self.opText = Label(self.opMenu, text="Operation:", font=("OratorStd", 18))
        self.opText.grid(column=0, row=0, pady=(10,0))

        # self.operation = Label(self.opMenu, text="current operation", font=("OratorStd", 12), fg="green")
        # self.operation.grid(column=0, row=1)
        default = StringVar(self.opMenu)
        default.set("Op 1")
        self.operation = OptionMenu(self.opMenu, default, "Op 1", "Op 2", "Op 3")
        self.operation.grid(column=0, row=1)

        self.rew = Button(self.opMenu, image=rewImg)
        self.rew.grid(column=1, row=0, rowspan=2, pady=(10,0), padx=(0,20))

        self.play = Button(self.opMenu, image=playImg)
        self.play.grid(column=2, row=0, rowspan=2, pady=(10,0), padx=(0,20))

        self.step = Button(self.opMenu, image=stepImg)
        self.step.grid(column=3, row=0, rowspan=2, pady=(10,0), padx=(0,20))

        self.stop = Button(self.opMenu, image=stopImg)
        self.stop.grid(column=4, row=0, rowspan=2, pady=(10,0), padx=(0,20))

        self.fwd = Button(self.opMenu, image=fwdImg)
        self.fwd.grid(column=5, row=0, rowspan=2, pady=(10,0), padx=(0,20))


root = Tk()

rewImg = ImageTk.PhotoImage(Image.open("icons/rew.png"))
playImg = ImageTk.PhotoImage(Image.open("icons/play.png"))
stepImg = ImageTk.PhotoImage(Image.open("icons/step.png"))
stopImg = ImageTk.PhotoImage(Image.open("icons/stop.png"))
fwdImg = ImageTk.PhotoImage(Image.open("icons/fwd.png"))

app = App(root)

root.mainloop()