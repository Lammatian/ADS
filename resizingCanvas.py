import tkinter as tk

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
            # move all items to the middle
            if self.item.set_axis == "height":
                for i in self.find_all():
                    if len(self.coords(i)) == 4:
                        # rectangles
                        obj_height = abs(self.coords(i)[1] - self.coords(i)[3])
                        self.coords(i, self.coords(i)[0], self.winfo_reqheight()//2-obj_height//2, self.coords(i)[2], self.winfo_reqheight()//2+obj_height//2)
                    else:
                        # text
                        self.coords(i, self.coords(i)[0], self.winfo_reqheight()//2)
            elif self.item.set_axis == "width_bottom":
                for i in self.find_all():
                    if len(self.coords(i)) == 4:
                        # rectangles
                        # I have no idea why +2 is needed, may not work on other computers
                        obj_width = abs(self.coords(i)[0] - self.coords(i)[2])
                        self.coords(i, self.winfo_reqwidth()//2-obj_width//2, self.winfo_reqheight() - (old_height - self.coords(i)[1] + 2), self.winfo_reqwidth()//2+obj_width//2, self.winfo_reqheight() - (old_height - self.coords(i)[3] + 2))
                    else:
                        # text
                        self.coords(i, self.winfo_reqwidth()//2, self.winfo_reqheight()- (old_height - self.coords(i)[1] + 2))