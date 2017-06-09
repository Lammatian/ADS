import sys
sys.path.append('../')

from structures import array

class DArray(object):
	"""
	Implementation of a dynamic array data structure using ADS.array.Array

	The above is used instead of Pythons lists (which are dynamic arrays themselves)
	to show how dynamic arrays work under the hood

	This implementation uses growth factor of 1.5
	"""
	def __init__(self, vals=[]):
		"""
		Initialise the array with optional initial values

		According to the growth factor, the initial length of the array 
		will be equal to 1.5 of the length of the argument

		If no initial values are given or just one value is given
		initial length will be equal to 2

		:param vals: optional initial values for the array
		:type vals: T[]
		"""
		self.arr = array.Array(max(3*len(vals)//2, 2), vals)
		self.length = len(vals)
		self.max_length = max(3*len(vals)//2, 2)


	def __iter__(self):
		"""Iterator"""
		return iter(self.arr)


	def __repr__(self):
		"""Representation of the array"""
		return "DArray(" + str(self.arr) + ")"


	def __str__(self):
		"""Return str(self)"""
		return str(self.arr)


	def lookup(self, n):
		"""
		Get the n-th element of the array

		Raises error if n out of bounds
		"""
		return self.arr.lookup(n)


	def update(self, n, val):
		"""
		Update n-th element of the array to given value

		Raises error if n out of bounds
		"""
		self.arr.update(n, val)


	def insert(self, n, val):
		"""
		Insert value at the n-th position of the array

		If the array is full, make a new array of size 3/2 of the old one

		Raises error if n out of bounds of the array
		"""
		if n < self.length and n >= 0:
			if self.length < self.max_length:
				self.arr.insert(n, val)
			else:
				self.arr = array.Array(3*self.max_length//2, self.arr.vals)
				self.max_length = 3*self.max_length//2
				self.arr.insert(n, val)

			self.length += 1
		else:
			raise IndexError("index out of bounds")


	def insertLast(self, val):
		"""
		Insert value at the end of the array

		If the array is full, make a new array of size 3/2 of the old one
		"""
		if self.length < self.max_length:
			self.arr.insertLast(val)
		else:
			self.arr = array.Array(3*self.max_length//2, self.arr.vals)
			self.max_length = 3*self.max_length//2
			self.arr.insertLast(val)

		self.length += 1


	def remove(self, n):
		"""
		Remove the n-th element of the array

		If load factor falls below 1/2, make a new array of size 3/4 of the old one

		Raises error if n out of bounds of the array
		"""
		if n < self.length and n >= 0:
			self.arr.remove(n)
			self.length -= 1

			if self.length/self.max_length < 0.5:
				self.arr = array.Array(max(3*self.max_length//4, 2), self.arr.vals[:self.length])
				self.max_length = max(3*self.max_length//4, 2)
		else:
			raise IndexError("index out of bounds")


	def removeLast(self):
		"""
		Remove the last element of the array

		If load factor falls below 1/2, make a new array of size 3/4 of the old one
		"""
		self.arr.removeLast()
		if self.length:
			self.length -= 1

		if self.length/self.max_length < 0.5:
			self.arr = array.Array(max(3*self.max_length//4, 2), self.arr.vals[:self.length])
			self.max_length = max(3*self.max_length//4, 2)


	def find(self, n):
		"""
		Returns an index of the first occurence of n in the array

		If value is not found, returns -1
		"""
		return self.arr.find(n)