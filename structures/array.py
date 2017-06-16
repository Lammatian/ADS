class Array(object):
	"""
	Implementation of an array using Python list

	Python lists themself are implemented using dynamic arrays
	so this implementation makes perfect sense and should work as actual array

	In this version, array is of bounded length to imitate static array structure
	"""
	_title = "Array"

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
			self._vals = [None]*length

			for i in range(len(vals)):
				self._vals[i] = vals[i]

			self._max_length = length


	def __iter__(self):
		"""Iterator"""
		return iter(self._vals)


	def __repr__(self):
		"""Representation of the array"""
		return super(Array, self).__repr__()


	def __str__(self):
		"""Return str(self)"""
		return str(self._vals)


	def lookup(self, n):
		"""
		Get n-th element of the array

		Raises error if n out of bounds of the array

		:param n: index in the array
		:type n: int
		"""
		if n < self._max_length and n >= 0:
			return self._vals[n]
		else:
			raise IndexError("index out of bounds")


	def put(self, n, val):
		"""
		Insert value at the n-th element of the array
		If n-th element of the array already contains
		a value, it gets replaced

		Raises error if n out of bounds of the array

		:param n: index in the array
		:param val: value to be inserted
		:type n: int
		:type val: T
		"""
		if n < self._max_length and n >= 0:
			self._vals[n] = val
		else:
			raise IndexError("index out of bounds")


	def find(self, val):
		"""
		Returns an index of the first occurrence of the value

		If value is not in the array, returns -1

		:param val: value to be found
		:type val: T
		"""
		try:
			return self._vals.index(val)
		except ValueError:
			return -1
