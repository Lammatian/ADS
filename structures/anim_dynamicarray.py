import sys
sys.path.append('../')

from structures import array
from structures.dynamicarray import DArray

class A_DArray(DArray):
    """
    Animated dynamic array as an extension to the dynamic array

    Each operation has its own animation
    """

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


    def remove(self, n):
        """Call remove of DArray and animation"""
        if n < self._length and n >= 0:
            if (self._length-1)/self._max_length >= 0.5:
                self._arr = array.Array(self._max_length, self._arr._vals[:n] + self._arr._vals[n+1:self._length])
            else:
                self._arr = array.Array(max(3*self._max_length//4, 2), self._arr._vals[:n] + self._arr._vals[n+1:self._length])
                self._max_length = max(3*self._max_length//4, 2)

            self._length -= 1
        else:
            raise IndexError("index out of bounds")


    def removeLast(self):
        """Call removeLast of DArray and animation"""
        if (self._length-1)/self._max_length >= 0.5:
            self._arr = array.Array(self._max_length, self._arr._vals[:self._length-1])
        else:
            self._arr = array.Array(max(3*self._max_length//4, 2), self._arr._vals[:self._length-1])
            self._max_length = max(3*self._max_length//4, 2)

        if self._length > 0:
            self._length -= 1


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
        if n < 0 or n >= self._length:
            return

        def notFull(val, n, step):
            # animation when array is not full
            def shift(to, step, current):
                # animation of shifting the elements one place to the right
                if current <= to:
                    self.canvas.after(150, notFull, val, n, 1)
                elif step == 0:
                    self.canvas.itemconfig(self.graphic[current-1][0], fill="green")
                    self.canvas.after(150, shift, to, 1, current)
                elif step == 1:
                    self.canvas.itemconfig(self.graphic[current-1][0], fill="white")
                    self.canvas.itemconfig(self.graphic[current][0], fill="green")
                    self.canvas.itemconfig(self.graphic[current][1], text=str(self._arr._vals[current]))
                    self.canvas.after(150, shift, to, 2, current)
                elif step == 2:
                    self.canvas.itemconfig(self.graphic[current][0], fill="white")
                    self.canvas.after(150, shift, to, 0, current-1)

            if step == 0:
                self.canvas.itemconfig(self.graphic[self._length-1][0], dash=(), fill="white")
                shift(n, step, self._length-1)
            elif step == 1:
                self.canvas.itemconfig(self.graphic[n][0], fill="green")
                self.canvas.after(250, notFull, val, n, 2)
            elif step == 2:
                self.canvas.itemconfig(self.graphic[n][1], text=str(val))
                self.canvas.after(250, notFull, val, n, 3)
            elif step == 3:
                self.canvas.itemconfig(self.graphic[n][0], fill="white")
                return

        def full(val, n, step):
            pass

        # test whether the array is full 
        # by checking if the last entry is dashed
        if self.canvas.itemcget(self.graphic[-1][0], "dash") != "":
            notFull(val, n, 0)
        else:
            full(val, n, 0)


    def _insertLast_animation(self, val):
        """Animation of the insertLast operation"""
        def notFull(val, step):
            # animation when array is not full
            if step == 0:
                self.canvas.itemconfig(self.graphic[self._length-1][0], dash=(), fill="green")
                self.canvas.after(500, notFull, val, 1)
            elif step == 1:
                self.canvas.itemconfig(self.graphic[self._length-1][1], text=str(val))
                self.canvas.after(500, notFull, val, 2)
            elif step == 2:
                self.canvas.itemconfig(self.graphic[self._length-1][0], fill="white")
                return

        def full(val, step):
            # animation when array is full
            def fill(step, n):
                # filling the new array
                if n == self._length:
                    self.canvas.after(500, full, val, 2)
                elif step == 0:
                    self.canvas.itemconfig(new_graphic[n][0], dash=(), fill="green")
                    self.canvas.after(150, fill, 1, n)
                elif step == 1:
                    self.canvas.itemconfig(new_graphic[n][1], text=str(self._arr._vals[n]))
                    self.canvas.after(150, fill, 2, n)
                elif step == 2:
                    self.canvas.itemconfig(new_graphic[n][0], fill="white")
                    self.canvas.after(150, fill, 0, n+1)

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

                self.canvas.after(500, full, val, 1)
            elif step == 1:
                # 'copy' all entries from old to new array
                fill(0, 0)
            elif step == 2:
                # swap old array to new array
                self.canvas.delete("old")
                self.canvas.move("new", 0, -100)
                self.graphic = new_graphic
                return

        # test whether the array is full
        # by checking if the last entry is dashed
        if self.canvas.itemcget(self.graphic[-1][0], "dash") != "":
            notFull(val, 0)
        else:
            # tag the old array as ' old'
            self.canvas.addtag_all("old")

            # for keeping the new array graphic
            new_graphic = []

            full(val, 0)


    def _removeNoResize_animation(self, n, step):
        """Animation of removal if no resizing is needed"""
        pass


    def _removeResize_animation(self, n, step):
        """Animation of removal if resizing is needed"""
        pass


    def _removeLastNoResize_animation(self, step):
        """Animation of removal from last place if no resizing is needed"""
        pass


    def _removeLastResize_animation(self, step):
        """Animation of removal from last place if resizing is needed"""
        pass


    def _update_animation(self, n, val, step):
        """Animation of the update operation"""
        if n < 0 or n >= self._length:
            return
        else:
            if step == 0:
                # highlight the entry looked up
                self.canvas.itemconfig(self.graphic[n][0], fill="green")
                self.canvas.after(500, self._update_animation, n, val, 1)
            elif step == 1:
                # update the entry with value
                self.canvas.itemconfig(self.graphic[n][1], text=str(val))
                self.canvas.after(1500, self._update_animation, n, val, 2)
            elif step == 2:
                # clean up and finish
                self.canvas.itemconfig(self.graphic[n][0], fill="white")
                return


    def _find_animation(self, val, step, n):
        """Animation of the find operation"""
        if step == 0:
            # highlight current entry yellow and check if found value
            self.canvas.itemconfig(self.graphic[n][0], fill="yellow")
            if self._arr._vals[n] == val:
                self.canvas.after(250, self._find_animation, val, 2, n)
            else:
                self.canvas.after(500, self._find_animation, val, 1, n)
        elif n == self._length-1 and step < 2:
            # value not found, alert with red entry
            self.canvas.itemconfig(self.graphic[n][0], fill="red")
            self.canvas.after(500, self._find_animation, val, 3, n)
        elif step == 1:
            # value not found, move to next entry
            self.canvas.itemconfig(self.graphic[n][0], fill="white")
            self.canvas.after(0, self._find_animation, val, 0, n+1)
        elif step == 2:
            # value found, show value for 1.5s and return
            self.canvas.itemconfig(self.graphic[n][0], fill="green")
            self.canvas.after(1500, self._find_animation, val, 3, n)
        elif step == 3:
            # clean up and finish
            self.canvas.itemconfig(self.graphic[n][0], fill="white")
            return


    animations = [
        lookup,
        update,
        insert,
        insertLast,
        remove,
        removeLast,
        find
    ]
