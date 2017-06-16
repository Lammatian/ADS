import sys
sys.path.append('../')

from structures import dynamicarray

class Stack(object):
    """
    Stack data structure implemented using dynamic array

    This implementation includes basic operations such as
    peek, pop, push and isEmpty
    """
    _title = "Stack"

    def __init__(self):
        """Initialise an empty stack"""
        self._stack = dynamicarray.DArray([])
        self._top = None


    def __repr__(self):
        """Representation of stack"""
        return super(Stack, self).__repr__()


    def __str__(self):
        """Return str(self)"""
        return repr(self)


    def isEmpty(self):
        """Check if the stack is empty"""
        return self._stack._length == 0


    def peek(self):
        """Peek at the top element of the stack"""
        return self._top


    def push(self, n):
        """Put an element on top of the stack"""
        self._stack.insertLast(n)
        self._top = n


    def pop(self):
        """
        Take the top element from the stack and return it

        Do nothing if the stack is empty
        """
        if not self.isEmpty():
            self._stack.removeLast()
            last_top = self._top

            if self._stack._length:
                self._top = self._stack.lookup(self._stack._length-1)
            else:
                self._top = None

            return last_top