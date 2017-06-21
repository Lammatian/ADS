import sys
sys.path.append('../')

from structures.stack import *

class A_Stack(Stack):
    """
    Animated stack as an extension of stack

    Each operation has its own animation
    """
    def __init__(self, canvas):
        """Initialise an empty stack"""
        super(A_Stack, self).__init__()

        # graphical representation of stack
        self.canvas = canvas
        self.graphic = []


    def isEmpty(self):
        """Call isEmpty method of stack and animation"""
        self._isEmpty_animation()

        return self._stack._length == 0


    def peek(self):
        """Call peek method of stack and animation"""
        self._peek_animation(0)

        return self._top


    def push(self, value):
        """Call push method of stack and animation"""
        super(A_Stack, self).push(value)

        self._push_animation(value, 0)


    def pop(self):
        """Call pop method of stack and animation"""
        self._pop_animation(0)

        return super(A_Stack, self).pop()


    def _isEmpty_animation(self):
        """Animation of the isEmpty operation"""
        pass


    def _peek_animation(self, step):
        """Animation of the peek operation"""
        if self.graphic:
            if step == 0:
                self._swap_color("green")
                self.canvas.after(500, self._peek_animation, 1)
            elif step == 1:
                self._swap_color("white")
                return
        else:
            return


    def _push_animation(self, n, step):
        """Animation of the push operation"""
        if step == 0:
            rect = self.canvas.create_rectangle(350 - 45,\
                                                300 - 30*(self._stack._length+1),\
                                                350 + 45,\
                                                300 - 30*(self._stack._length),\
                                                fill="green")
            text = self.canvas.create_text(350,\
                                           300 - 30*self._stack._length - 15,\
                                           text=str(n))
            self.graphic.append((rect, text))
            self.canvas.after(500, self._push_animation, n, 1)
        elif step == 1:
            self._swap_color("white")
            return

    
    def _pop_animation(self, step):
        """Animation of the pop operation"""
        if step == 0:
            self._swap_color("red")
            self.canvas.after(500, self._pop_animation, 1)
        elif step == 1:
            self.canvas.delete(*self.graphic[-1])
            self.graphic = self.graphic[:-1]
            return


    def _swap_color(self, color):
        """Swap color of a rectangle"""
        self.canvas.itemconfig(self.graphic[-1][0], fill=color)


    animations = [
        isEmpty,
        peek,
        push,
        pop
    ]