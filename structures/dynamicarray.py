import sys
sys.path.append('../')

from structures import array

class DArray(object):
    """
    Implementation of a dynamic array data structure using ADS.array.Array

    The above is used instead of Pythons lists (which are dynamic arrays themselves)
    to show how dynamic arrays work under the hood

    This implementation uses growth factor of 2
    """
    _title = "Dynamic array"

    def __init__(self, vals=[]):
        """
        Initialise the array with optional initial values

        According to the growth factor, the initial length of the array 
        will be equal to 2 times the length of the argument

        If no initial values are given or just one value is given
        initial length will be equal to 2

        :param vals: optional initial values for the array
        :type vals: T[]
        """
        self._arr = array.Array(max(4*len(vals)//3, 2), vals)
        self._length = len(vals)
        self._max_length = max(4*len(vals)//3, 2)


    def __iter__(self):
        """Iterator"""
        return iter(self._arr._vals[:self._length])


    def __repr__(self):
        """Representation of the array"""
        return super(DArray, self).__repr__()


    def __str__(self):
        """Return str(self)"""
        return str(self._arr._vals[:self._length])


    def lookup(self, n):
        """
        Get the n-th element of the array

        Raises error if n out of bounds

        :param n: index to be looked up
        :type n: int
        """
        if n >= 0 and n < self._length:
            return self._arr.lookup(n)
        else:
            raise IndexError("index out of bounds")


    def update(self, n, val):
        """
        Update n-th element of the array to given value

        Raises error if n out of bounds

        :param n: index in the array
        :param val: value to insert
        :type n: int
        :type val: T
        """
        if n >= 0 and n < self._length:
            self._arr.put(n, val)
        else:
            raise IndexError("index out of bounds")


    def insert(self, n, val):
        """
        Insert value at the n-th position of the array

        If the array is full, make a new array of
        twice the size of the old one

        Raises error if n out of bounds of the array

        :param n: index in the array
        :param val: value to insert
        :type n: int
        :type val: T
        """
        if n <= self._length and n >= 0:
            if self._length < self._max_length:
                self._arr = array.Array(self._max_length, self._arr._vals[:n] + [val] + self._arr._vals[n:self._length])
            else:
                self._arr = array.Array(2*self._max_length, self._arr._vals[:n] + [val] + self._arr._vals[n:self._length])
                self._max_length = 2*self._max_length

            self._length += 1
        else:
            raise IndexError("index out of bounds")


    def insertLast(self, val):
        """
        Insert value at the end of the array

        If the array is full, make a new array of
        twice the size of the old one

        :param val: value to insert
        :type val: T
        """
        if self._length < self._max_length:
            self._arr.put(self._length, val)
        else:
            self._arr = array.Array(2*self._max_length, self._arr._vals[:self._length] + [val])
            self._max_length = 2*self._max_length

        self._length += 1


    def remove(self, n):
        """
        Remove the n-th element of the array

        If load factor falls below 1/2, make a new array of size 3/4 of the old one

        Raises error if n out of bounds of the array

        :param n: index in the array
        :type n: int
        """
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
        """
        Remove the last element of the array

        If load factor falls below 1/2, make a new array of size 3/4 of the old one
        """

        if (self._length-1)/self._max_length >= 0.5:
            self._arr = array.Array(self._max_length, self._arr._vals[:self._length-1])
        else:
            self._arr = array.Array(max(3*self._max_length//4, 2), self._arr._vals[:self._length-1])
            self._max_length = max(3*self._max_length//4, 2)

        if self._length > 0:
            self._length -= 1


    def find(self, n):
        """
        Returns an index of the first occurence of n in the array

        If value is not found, returns -1

        :param n: index in the array:
        :type n: int
        """
        return self._arr.find(n)