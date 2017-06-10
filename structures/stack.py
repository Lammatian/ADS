import sys
sys.path.append('../')

from structures import dynamicarray

class Stack(object):
    """
    Stack data structure implemented using dynamic array

    This implementation includes basic operations such as
    peek, pop, push and isEmpty
    """
    def __init__(self):
        """Initialise an empty stack"""
        self.stack = dynamicarray.DArray([])
        self.top = None


    def __repr__(self):
        """Representation of stack"""
        pass


    def __str__(self):
        """Return str(self)"""
        pass


    def isEmpty(self):
        """Check if the stack is empty"""
        return self.stack.length == 0