class ArrayFullError(Exception):
	"""Error returned when array is full"""
	def __init__(self, msg="array is full"):
		super(ArrayFullError, self).__init__(msg)


class Array(object):
	"""
	Implementation of an array using Python list

	Python lists themself are implemented using dynamic arrays
	so this implementation makes perfect sense and should work as actual array

	In this version, array is of bounded length to imitate static array structure
	"""
	def __init__(self, length, vals=[]):
		"""
		Initialise the array with obligatory length and optional initial values

		:param length: length of the array
		:param vals: initial values
		:type length: int
		:type vals: T[]
		"""
		if len(vals) > length:
			raise IndexError("index out of bounds")
		else:
			self.vals = [None]*length

			for i in range(len(vals)):
				self.vals[i] = vals[i]

			self.length = len(vals)
			self.max_length = length


	def __iter__(self):
		"""Iterator"""
		return iter(self.vals[:self.length])


	def __repr__(self):
		"""Representation of the array"""
		return "Array(" + str(self.max_length) + ", " + str(self.vals[:self.length]) + ")"


	def __str__(self):
		"""Return str(self)"""
		return str(self.vals[:self.length])


	def lookup(self, n):
		"""
		Get n-th element of the array

		Raises error if n out of bounds of the array
		"""
		if n < self.length and n >= 0:
			return self.vals[n]
		else:
			raise IndexError("index out of bounds")


	def update(self, n, val):
		"""
		Update n-th element of the array to val

		Raises error if n out of bounds of the array
		"""
		if n < self.length and n >= 0:
			self.vals[n] = val
		else:
			raise IndexError("index out of bounds")


	def insert(self, n, val):
		"""
		Insert value at n-th position in the array

		Raises error if n out of bounds of the array or the array is full
		"""
		if n < self.length and n >= 0 and self.length < self.max_length:
			temp = self.vals[n:]
			self.vals[n] = val
			self.vals[n+1:] = temp

			self.length += 1
		elif n >= self.length or n < 0:
			raise IndexError("index out of bounds")
		else:
			raise ArrayFullError()


	def insertLast(self, val):
		"""
		Inserts value at the end of the array

		Raises error if the array is full
		"""
		if self.length == self.max_length:
			raise ArrayFullError()
		else:
			self.vals[self.length] = val
			self.length += 1


	def remove(self, n):
		"""
		Removes value at n-th position in the array

		Raises error if n out of bounds of the array
		"""
		if n < self.length and n >= 0:
			self.vals = self.vals[:n] + self.vals[n+1:]
			self.length -= 1
		else:
			raise IndexError("index out of bounds")


	def removeLast(self):
		"""
		Removes last value in the array

		Does nothing if the array is empty
		"""
		if self.length:
			self.vals[self.length-1] = None
			self.length -= 1


	def find(self, val):
		"""
		Returns an index of the first occurrence of the value

		If value is not in the array, returns -1
		"""
		try:
			return self.vals.index(val)
		except ValueError:
			return -1
