import sys
sys.path.append('../')

from structures.dlinkedlist import *

class Queue(object):
    """
    Implementation of Queue using doubly linked list

    Includes basic operations such as isEmpty, enqueue, dequeue, peek
    """
    _title = "Queue"

    def __init__(self):
        """Initialise an empty queue"""
        self._queue = DLinkedList()
        self._front = None


    def __repr__(self):
        """Representation of the queue"""
        return super(Queue, self).__repr__()


    def __str__(self):
        """Return str(self)"""
        return repr(self)


    def isEmpty(self):
        """Check if the queue is empty"""
        return self._queue.length == 0


    def peek(self):
        """Returns the first element in the queue"""
        return self._front


    def enqueue(self, n):
        """Append an element at the end of the queue"""
        if self._queue.length == 0:
            self._front = n
        
        self._queue.insertLast(n)


    def dequeue(self):
        """Remove the front element from the queue and return it"""
        last_front = self._front
        self._queue.removeFirst()
        self._front = self._queue.lookup(0) if self._queue.head else None
        return last_front