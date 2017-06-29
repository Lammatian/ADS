import sys
sys.path.append('../')

from structures.stack import *

class A_Stack(Stack):
    """
    Animated stack as an extension of stack

    Each operation has its own animation
    """
    # side to which animation is sticked
    stick = "bottom"

    def __init__(self, canvas):
        """Initialise an empty stack"""
        super(A_Stack, self).__init__()

        # graphical representation of stack
        self.canvas = canvas
        self.graphic = []
        self.length = 0

        # pre-create the rectangles for better resizing alignment
        for i in range(1000):
            rect = self.canvas.create_rectangle(self.canvas.winfo_reqwidth()//2 - 45,\
                                                self.canvas.winfo_reqheight() - 30*(i+2),\
                                                self.canvas.winfo_reqwidth()//2 + 45,\
                                                self.canvas.winfo_reqheight() - 30*(i+1),\
                                                state="hidden",\
                                                fill="green")
            text = self.canvas.create_text(self.canvas.winfo_reqwidth()//2,\
                                           self.canvas.winfo_reqheight() - 30*i -45,\
                                           state="hidden",\
                                           text="")
            self.graphic.append((rect, text))


    def isEmpty(self):
        """Call isEmpty method of stack and animation"""
        self._isEmpty_animation(0)

        return super(A_Stack, self).isEmpty()


    def peek(self):
        """Call peek method of stack and animation"""
        self._peek_animation(0)

        return super(A_Stack, self).peek()


    def push(self, value):
        """Call push method of stack and animation"""
        super(A_Stack, self).push(value)

        self._push_animation(value, 0)


    def pop(self):
        """Call pop method of stack and animation"""
        self._pop_animation(0)

        return super(A_Stack, self).pop()


    def _isEmpty_animation(self, step):
        """Animation of the isEmpty operation"""
        if step == 0:
            self.canvas.itemconfig("rect", fill="green")
            self.canvas.after(500, self._isEmpty_animation, 1)
        elif step == 1:
            self.canvas.itemconfig("rect", fill="white")
            return


    def _peek_animation(self, step):
        """Animation of the peek operation"""
        if self.graphic:
            if step == 0:
                self._swap_color("green")
                self.canvas.after(500, self._peek_animation, 1)
            elif step == 1:
                self._swap_color("white")
                return


    def _push_animation(self, n, step):
        """Animation of the push operation"""
        if step == 0:
            self.canvas.itemconfig(self.graphic[self.length][0], state="normal")
            self.canvas.itemconfig(self.graphic[self.length][1], state="normal", text=str(n))
            self.canvas.after(500, self._push_animation, n, 1)
        elif step == 1:
            self._swap_color("white", self.length)
            self.length += 1
            return

    
    def _pop_animation(self, step):
        """Animation of the pop operation"""
        if self.length > 0:
            if step == 0:
                self._swap_color("red", self.length-1)
                self.canvas.after(500, self._pop_animation, 1)
            elif step == 1:
                self.canvas.itemconfig(self.graphic[self.length-1][0], state="hidden", fill="green")
                self.canvas.itemconfig(self.graphic[self.length-1][1], state="hidden", text="")
                self.length -= 1
                return


    def _swap_color(self, color, index):
        """Swap color of a rectangle"""
        self.canvas.itemconfig(self.graphic[index][0], fill=color)


    animations = [
        isEmpty,
        peek,
        push,
        pop
    ]