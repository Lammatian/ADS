import tkinter as tk
import math

class ResizingCanvas(tk.Canvas):
    """
    A subclass of Canvas for dealing with resizing windows

    Taken from https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width
    and modified for the purpose of the program
    """
    def __init__(self, parent, item=None, **kwargs):
        """
        Initialise resizing canvas

        Item is the data structure held by the canvas
        """
        tk.Canvas.__init__(self, parent, **kwargs)
        self.item = item
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()


    def on_resize(self, event):
        """Resize all elements of canvas on resize of the window"""
        # determine how much has the window changed size
        old_width = self.width
        old_height = self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # move all the objects tagged with "all" tag (by addtag_all method)
        if self.item:
            # move all items to stay where they relatively were
            if self.item.stick == "left":
                # some cool maths (count relative height of object and move to stay at the same relative height)
                relative_height = (self.coords(self.find_all()[0])[1] + self.coords(self.find_all()[0])[3])/(2*(old_height+2))
                self.move("all", 0, (self.height-old_height)*relative_height)
            elif self.item.stick == "bottom":
                # count relative width and move to stay at the same relative width
                relative_width = (self.coords(self.find_all()[0])[0] + self.coords(self.find_all()[0])[2])/(2*(old_width+2))
                self.move("all", (self.width-old_width)*relative_width, self.height-old_height)