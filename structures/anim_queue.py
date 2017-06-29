import sys
sys.path.append('../')

from structures.queue import *

class A_Queue(Queue):
    """
    Animated queue as an extension of Queue

    Each operation has its own animation
    """
    # side to which animation is sticked
    stick = "left"

    def __init__(self, canvas):
        """Initialise an empty queue"""
        super(A_Queue, self).__init__()

        # graphical representation of the queue
        self.canvas = canvas
        self.graphic = []
        self.length = 0

        # create hidden nodes for better resizing alignment
        for i in range(1000):
            rect = self.canvas.create_rectangle(30*i+50,\
                                                self.canvas.winfo_reqheight()//2-25,\
                                                30*i+80,\
                                                self.canvas.winfo_reqheight()//2+25,\
                                                state="hidden",\
                                                fill="green")
            text = self.canvas.create_text(30*i+65,\
                                           self.canvas.winfo_reqheight()//2,\
                                           state="hidden",\
                                           text="")
            self.graphic.append((rect, text))


    def isEmpty(self):
        """Call isEmpty method of Queue and animation"""
        self._isEmpty_animation(0)

        return super(A_Queue, self).isEmpty()


    def peek(self):
        """Call peek method of Queue and animation"""
        self._peek_animation(0)

        return super(A_Queue, self).peek()


    def enqueue(self, value):
        """Call enqueue method of Queue and animation"""
        super(A_Queue, self).enqueue(value)

        self._enqueue_animation(value, 0)


    def dequeue(self):
        """Call dequeue method of Queue and animation"""
        self._dequeue_animation(0)

        return super(A_Queue, self).dequeue()


    def _isEmpty_animation(self, step):
        """Animation of isEmpty method"""
        if step == 0:
            self.canvas.itemconfig("rect", fill="green")
            self.canvas.after(500, self._isEmpty_animation, 1)
        elif step == 1:
            self.canvas.itemconfig("rect", fill="white")
            return


    def _peek_animation(self, step):
        """Animation of peek method"""
        if self.graphic:
            if step == 0:
                self._swap_color("green", -1)
                self.canvas.after(500, self._peek_animation, 1)
            elif step == 1:
                self._swap_color("white", -1)
                return


    def _enqueue_animation(self, n, step):
        """Animation of the enqueue method"""
        if step == 0:
            self.canvas.itemconfig(self.graphic[self.length][0], state="normal")
            self.canvas.itemconfig(self.graphic[self.length][1], state="normal", text=str(n))
            self.canvas.after(500, self._enqueue_animation, n, 1)
        elif step == 1:
            self._swap_color("white", self.length)
            self.length += 1
            return


    def _dequeue_animation(self, step):
        """Animation of the dequeue method"""
        # this should be changed in the future but let it stay for now
        if self.length > 0:
            if step == 0:
                self._swap_color("red", 0)
                self.canvas.after(500, self._dequeue_animation, 1)
            elif step == 1:
                self.canvas.delete(*self.graphic[0])
                self.graphic.pop(0)
                rect = self.canvas.create_rectangle(30*999+50,\
                                             self.canvas.winfo_reqheight()//2-25,\
                                             30*999+80,\
                                             self.canvas.winfo_reqheight()//2+25,\
                                             state="hidden",\
                                             fill="green")
                text = self.canvas.create_text(30*999+65,\
                                        self.canvas.winfo_reqheight()//2,\
                                        state="hidden",\
                                        text="")
                self.graphic.append((rect,text))
                self.canvas.after(250, self._dequeue_animation, 2)
            elif step == 2:
                self.canvas.move("all", -30, 0)
                self.length -= 1
                return


    def _swap_color(self, color, index):
        """Swap color of the first element of the queue"""
        self.canvas.itemconfig(self.graphic[index][0], fill=color)


    animations = [
        isEmpty,
        peek,
        enqueue,
        dequeue
    ]