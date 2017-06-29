import sys
import math
sys.path.append('../')

from structures import array
from structures.dynamicarray import DArray

class A_DArray(DArray):
    """
    Animated dynamic array as an extension to the dynamic array

    Each operation has its own animation
    """
    # side to which animation is sticked
    stick = "left"

    def __init__(self, canvas, values=[]):
        """
        Initialise the array with optional initial values

        :param values: optional initial values for the array
        :param canvas: canvas in which the array will be show
        :type values: T[]
        :type canvas: tkinter.Canvas
        """
        super(A_DArray, self).__init__(values)

        # graphical representation of dynamic array        
        self.canvas = canvas
        self.graphic = []
        for i, val in enumerate(self._arr._vals):
            if i < self._length:
                rect = canvas.create_rectangle(50*i+50,\
                                               canvas.winfo_reqheight()//2-25,\
                                               50*i+100,\
                                               canvas.winfo_reqheight()//2+25,\
                                               fill="white")
                text = canvas.create_text((50*i+75,\
                                           canvas.winfo_reqheight()//2),\
                                           text=str(val))
            else:
                rect = canvas.create_rectangle(50*i+50,\
                                               canvas.winfo_reqheight()//2-25,\
                                               50*i+100,\
                                               canvas.winfo_reqheight()//2+25,\
                                               dash=(5,5))
                text = canvas.create_text((50*i+75,\
                                           canvas.winfo_reqheight()//2),\
                                           text="")
            self.graphic.append((rect, text))


    def lookup(self, index):
        """Call lookup of DArray and animation"""
        self._lookup_animation(index, 0)

        return super(A_DArray, self).lookup(index)


    def update(self, index, value):
        """Call update of DArray and animation"""
        self._update_animation(index, value, 0)

        super(A_DArray, self).update(index, value)


    def insert(self, index, value):
        """Call insert of DArray and animation"""
        super(A_DArray, self).insert(index, value)

        self._insert_animation(index, value)


    def insertLast(self, value):
        """Call insertLast of DArray and animation"""
        super(A_DArray, self).insertLast(value)

        self._insertLast_animation(value)        


    def remove(self, index):
        """Call remove of DArray and animation"""
        super(A_DArray, self).remove(index)
        
        self._remove_animation(index)


    def removeLast(self):
        """Call removeLast of DArray and animation"""
        super(A_DArray, self).removeLast()

        self._removeLast_animation()


    def find(self, value):
        """Call find of DArray and animation"""
        self._find_animation(value, 0, 0)

        return super(A_DArray, self).find(value)


    def _lookup_animation(self, n, step):
        """Animation of the lookup operation"""
        if n < 0 or n >= self._length:
            return
        else:
            if step == 0:
                # highlight the entry looked up
                self.canvas.itemconfig(self.graphic[n][0], fill="green")
                self.canvas.after(1500, self._lookup_animation, n, 1)
            elif step == 1:
                # clean up and finish
                self.canvas.itemconfig(self.graphic[n][0], fill="white")
                return


    def _insert_animation(self, n, val):
        """Animation of the insert operation"""
        if n < 0 or n > self._length:
            return

        def notFull(val, n, step):
            # animation when array is not full
            def shift(to, step, current):
                # animation of shifting the elements one place to the right
                if current <= to:
                    self.canvas.after(150, notFull, val, n, 1)
                elif step == 0:
                    self._swap_color(current-1, "green")
                    self.canvas.after(150, shift, to, 1, current)
                elif step == 1:
                    self._swap_color(current-1, "white")
                    self._swap_color(current, "green")
                    self.canvas.itemconfig(self.graphic[current][1], text=str(self._arr._vals[current]))
                    self.canvas.after(150, shift, to, 2, current)
                elif step == 2:
                    self._swap_color(current, "white")
                    self.canvas.after(150, shift, to, 0, current-1)

            if step == 0:
                self._swap_color(self._length-1, "white")
                self._remove_dash(self._length-1)
                shift(n, step, self._length-1)
            elif step == 1:
                self._swap_color(n, "yellow")
                self.canvas.after(250, notFull, val, n, 2)
            elif step == 2:
                self.canvas.itemconfig(self.graphic[n][1], text=str(val))
                self.canvas.after(250, notFull, val, n, 3)
            elif step == 3:
                self._swap_color(n, "white")
                return


        def full(val, n, step):
            # animation when array is full
            def fill(which, step):
                if which == self._length:
                    # end filling
                    self.canvas.after(500, full, val, n, 2)
                elif which < n:
                    # before insertion
                    # just copy items from old array
                    if step == 0:
                        self._swap_color(which, "green")
                        self._swap_color(which, "green", new_graphic)
                        self._remove_dash(which, new_graphic)
                        self.canvas.after(150, fill, which, 1)
                    elif step == 1:
                        self.canvas.itemconfig(new_graphic[which][1], text=str(self._arr._vals[which]))
                        self.canvas.after(150, fill, which, 2)
                    elif step == 2:
                        self._swap_color(which, "white")
                        self._swap_color(which, "white", new_graphic)
                        self.canvas.after(150, fill, which+1, 0)
                elif which == n:
                    # insertion point
                    # just modify new array
                    if step == 0:
                        self._swap_color(which, "yellow", new_graphic)
                        self._remove_dash(which, new_graphic)
                        self.canvas.after(150, fill, which, 1)
                    elif step == 1:
                        self.canvas.itemconfig(new_graphic[which][1], text=str(self._arr._vals[which]))
                        self.canvas.after(150, fill, which, 2)
                    elif step == 2:
                        self._swap_color(which, "white", new_graphic)
                        self.canvas.after(150, fill, which+1, 0)
                elif which > n:
                    # after insertion
                    # there is an offset between the arrays now
                    if step == 0:
                        self._swap_color(which-1, "green")
                        self._swap_color(which, "green", new_graphic)
                        self._remove_dash(which, new_graphic)
                        self.canvas.after(150, fill, which, 1)
                    elif step == 1:
                        self.canvas.itemconfig(new_graphic[which][1], text=str(self._arr._vals[which]))
                        self.canvas.after(150, fill, which, 2)
                    elif step == 2:
                        self._swap_color(which-1, "white")
                        self._swap_color(which, "white", new_graphic)
                        self.canvas.after(150, fill, which+1, 0)

            if step == 0:
                # create new array, initially all dashed
                for i in range(self._max_length):
                    rect = self.canvas.create_rectangle(50*i+50,\
                                                        self.canvas.winfo_reqheight()//2+75,\
                                                        50*i+100,\
                                                        self.canvas.winfo_reqheight()//2+125,\
                                                        dash=(5,5), tag="new")
                    text = self.canvas.create_text((50*i+75,\
                                                    self.canvas.winfo_reqheight()//2+100),\
                                                    text="",\
                                                    tag="new")
                    new_graphic.append((rect, text))

                self.canvas.after(500, full, val, n, 1)
            elif step == 1:
                # 'copy' all the elements along with the new inserted one
                fill(0, 0)
            elif step == 2:
                # move new array in place of the old one
                self.canvas.delete("old")

                for obj in self.canvas.find_withtag("new"):
                    if len(self.canvas.coords(obj)) == 4:
                        # rect
                        self.canvas.coords(obj, self.canvas.coords(obj)[0],\
                                                self.canvas.winfo_reqheight()//2-25,\
                                                self.canvas.coords(obj)[2],\
                                                self.canvas.winfo_reqheight()//2+25)
                    else:
                        # text
                        self.canvas.coords(obj, self.canvas.coords(obj)[0],\
                                                self.canvas.winfo_reqheight()//2)
                        
                self.graphic = new_graphic
                return

        # test whether the array is full 
        # by checking if the last entry is dashed
        if self.canvas.itemcget(self.graphic[-1][0], "dash") != "":
            notFull(val, n, 0)
        else:
            # tag the old array as ' old'
            self.canvas.addtag_all("old")

            # for keeping the new array graphic
            new_graphic = []

            full(val, n, 0)


    def _insertLast_animation(self, val):
        """Animation of the insertLast operation"""
        self._insert_animation(self._length-1, val)


    def _remove_animation(self, n):
        """Animation of remove operation"""
        if n < 0 or n > self._length:
            return

        def noResize(current, step):
            # animation when no resize is needed
            if current == self._length:
                self.canvas.itemconfig(self.graphic[current][0], dash=(5,5), fill="")
                self.canvas.itemconfig(self.graphic[current][1], text="")
                return
            elif step == 0:
                self._swap_color(current, "green")
                self._swap_color(current+1, "green")
                self.canvas.after(150, noResize, current, 1)
            elif step == 1:
                self.canvas.itemconfig(self.graphic[current][1], text=str(self._arr._vals[current]))
                self.canvas.after(150, noResize, current, 2)
            elif step == 2:
                self._swap_color(current, "white")
                self._swap_color(current+1, "white")
                self.canvas.after(150, noResize, current+1, 0)

        def resize(n, step):
            # animation when resize is needed
            def fill(which, step):
                # filling up the new resized array
                if which == self._length+1:
                    # end filling
                    self.canvas.after(500, resize, n, 2)
                elif which < n:
                    # before removal
                    # just copy items from old array
                    if step == 0:
                        self._swap_color(which, "green")
                        self._swap_color(which, "green", new_graphic)
                        self._remove_dash(which, new_graphic)
                        self.canvas.after(150, fill, which, 1)
                    elif step == 1:
                        self.canvas.itemconfig(new_graphic[which][1], text=str(self._arr._vals[which]))
                        self.canvas.after(150, fill, which, 2)
                    elif step == 2:
                        self._swap_color(which, "white")
                        self._swap_color(which, "white", new_graphic)
                        self.canvas.after(150, fill, which+1, 0)
                elif which == n:
                    # removal point
                    # indicate that this element is not copied with red
                    if step == 0:
                        self._swap_color(which, "red")
                        self.canvas.after(150, fill, which+1, 0)
                elif which > n:
                    # after insertion
                    # there is an offset between the arrays now
                    if step == 0:
                        self._swap_color(which, "green")
                        self._swap_color(which-1, "green", new_graphic)
                        self._remove_dash(which-1, new_graphic)
                        self.canvas.after(150, fill, which, 1)
                    elif step == 1:
                        self.canvas.itemconfig(new_graphic[which-1][1], text=str(self._arr._vals[which-1]))
                        self.canvas.after(150, fill, which, 2)
                    elif step == 2:
                        self._swap_color(which, "white")
                        self._swap_color(which-1, "white", new_graphic)
                        self.canvas.after(150, fill, which+1, 0)
                

            if step == 0:
                # create new array, initially all dashed
                for i in range(self._max_length):
                    rect = self.canvas.create_rectangle(50*i+50,\
                                                        self.canvas.winfo_reqheight()//2+75,\
                                                        50*i+100,\
                                                        self.canvas.winfo_reqheight()//2+125,\
                                                        dash=(5,5), tag="new")
                    text = self.canvas.create_text((50*i+75,\
                                                    self.canvas.winfo_reqheight()//2+100),\
                                                    text="",\
                                                    tag="new")
                    new_graphic.append((rect, text))

                self.canvas.after(500, resize, n, 1)
            elif step == 1:
                # copy elements from the old array to new array
                fill(0, 0)
            elif step == 2:
                # swap old array to new array
                self.canvas.delete("old")
                self.canvas.move("new", 0, -100)
                self.graphic = new_graphic
                return
        
        # test whether resize will be needed
        # by checking if next element after the middle one is dashed or not
        if self.canvas.itemcget(self.graphic[math.ceil(len(self.graphic)/2)][0], "dash") == "":
            self._swap_color(n, "red")
            self.canvas.after(250, noResize, n, 0)
            #noResize(n, 0)
        else:
            # tag the old array as ' old'
            self.canvas.addtag_all("old")

            # for keeping the new array graphic
            new_graphic = []

            resize(n, 0)


    def _removeLast_animation(self):
        """Animation of removeLast operation"""
        self._remove_animation(self._length)


    def _update_animation(self, n, val, step):
        """Animation of the update operation"""
        if n < 0 or n >= self._length:
            return
        else:
            if step == 0:
                # highlight the entry looked up
                self._swap_color(n, "green")
                self.canvas.after(500, self._update_animation, n, val, 1)
            elif step == 1:
                # update the entry with value
                self.canvas.itemconfig(self.graphic[n][1], text=str(val))
                self.canvas.after(1500, self._update_animation, n, val, 2)
            elif step == 2:
                # clean up and finish
                self._swap_color(n, "white")
                return


    def _find_animation(self, val, step, n):
        """Animation of the find operation"""
        if step == 0:
            # highlight current entry yellow and check if found value
            self._swap_color(n, "yellow")
            if self._arr._vals[n] == val:
                self.canvas.after(250, self._find_animation, val, 2, n)
            else:
                self.canvas.after(500, self._find_animation, val, 1, n)
        elif n == self._length-1 and step < 2:
            # value not found, alert with red entry
            self._swap_color(n, "red")
            self.canvas.after(500, self._find_animation, val, 3, n)
        elif step == 1:
            # value not found, move to next entry
            self._swap_color(n, "white")
            self.canvas.after(0, self._find_animation, val, 0, n+1)
        elif step == 2:
            # value found, show value for 1.5s and return
            self._swap_color(n, "green")
            self.canvas.after(1000, self._find_animation, val, 3, n)
        elif step == 3:
            # clean up and finish
            self._swap_color(n, "white")
            return


    def _swap_color(self, index, color, graphic=None):
        """Swap color of rectangle at given index"""
        if graphic == None:
            graphic = self.graphic

        self.canvas.itemconfig(graphic[index][0], fill=color)


    def _remove_dash(self, index, graphic=None):
        """Remove dash of rectangle at given index"""
        if graphic == None:
            graphic = self.graphic

        self.canvas.itemconfig(graphic[index][0], dash=())


    animations = [
        lookup,
        update,
        insert,
        insertLast,
        remove,
        removeLast,
        find
    ]
