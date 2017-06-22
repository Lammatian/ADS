import sys
sys.path.append('../')

from structures.queue import *

class A_Queue(Queue):
    """
    Animated queue as an extension of Queue

    Each operation has its own animation
    """
    def __init__(self, canvas):
        """Initialise an empty queue"""
        super(A_Queue, self).__init__()

        # graphical representation of the queue
        self.canvas = canvas
        self.graphic = []


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
            rect = self.canvas.create_rectangle(50 + 30*(len(self.graphic)+1),\
                                                self.canvas.winfo_reqheight()//2 - 25,\
                                                50 + 30*(len(self.graphic)),\
                                                self.canvas.winfo_reqheight()//2 + 25,\
                                                fill="green",\
                                                tag="rect")
            text = self.canvas.create_text(50 + 30*len(self.graphic) + 15,\
                                           self.canvas.winfo_reqheight()//2,\
                                           text=str(n))
            self.graphic = [(rect, text)] + self.graphic
            self.canvas.after(500, self._enqueue_animation, n, 1)
        elif step == 1:
            self._swap_color("white", 0)
            return


    def _dequeue_animation(self, step):
        """Animation of the dequeue method"""
        if step == 0:
            self._swap_color("red", -1)
            self.canvas.after(500, self._dequeue_animation, 1)
        elif step == 1:
            self.canvas.delete(*self.graphic[-1])
            self.graphic.pop()
            self.canvas.after(250, self._dequeue_animation, 2)
        elif step == 2:
            self.canvas.move("all", -30, 0)


    def _swap_color(self, color, index):
        """Swap color of the first element of the queue"""
        self.canvas.itemconfig(self.graphic[index][0], fill=color)


    animations = [
        isEmpty,
        peek,
        enqueue,
        dequeue
    ]