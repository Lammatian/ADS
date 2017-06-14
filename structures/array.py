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

			self.max_length = length


	def __iter__(self):
		"""Iterator"""
		return iter(self.vals)


	def __repr__(self):
		"""Representation of the array"""
		return "Array(" + str(self.max_length) + ", " + str(self.vals) + ")"


	def __str__(self):
		"""Return str(self)"""
		return str(self.vals)


	def lookup(self, n):
		"""
		Get n-th element of the array

		Raises error if n out of bounds of the array
		"""
		if n < self.max_length and n >= 0:
			return self.vals[n]
		else:
			raise IndexError("index out of bounds")


	def insert(self, n, val):
		"""
		Insert value as the n-th element of the array
		If n-th element of the array already contains
		a value, it gets replaced

		Raises error if n out of bounds of the array
		"""
		if n < self.max_length and n >= 0:
			self.vals[n] = val
		else:
			raise IndexError("index out of bounds")


	def find(self, val):
		"""
		Returns an index of the first occurrence of the value

		If value is not in the array, returns -1
		"""
		try:
			return self.vals.index(val)
		except ValueError:
			return -1
