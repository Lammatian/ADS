class CArray(object):
	"""
	Implementation of an array using Python list

	Python lists themself are implemented using dynamic arrays
	so this implementation makes perfect sense and should work as actual array

	In this version, array is of bounded length to imitate static array structure
	"""
	_title = "Array"

	def __init__(self, canvas, length, vals=[]):
		"""
		Initialise the array with obligatory length and optional initial values

		:param length: length of the array
		:param vals: initial values
		:type length: int
		:type vals: T[]
		"""
		self.canvas = canvas 

		if len(vals) > length:
			raise IndexError("index out of bounds")
		else:
			self._vals = [None]*length

			for i in range(len(vals)):
				self._vals[i] = vals[i]

			self._max_length = length

		# graphical representation of the data structure
		self.graphic = []

		for i, val in enumerate(self._vals):
			rect = canvas.create_rectangle(50*i+50, canvas.winfo_reqheight()//2-25, 50*i+100, canvas.winfo_reqheight()//2+25, fill="white")
			text = canvas.create_text((50*i+75, canvas.winfo_reqheight()//2), text=str(val))
			self.graphic.append((rect, text))


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
			self._lookup_animation(n, 0)
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
			self._put_animation(n, val, 0)
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
		self._find_animation(val, 0, 0)
		try:
			return self._vals.index(val)
		except ValueError:
			return -1


	def _lookup_animation(self, n, step):
		"""animation of lookup operation"""
		if step == 0:
			# highlight the entry looked up
			self.canvas.itemconfig(self.graphic[n][0], fill="green")
			self.canvas.after(1500, self._lookup_animation, n, 1)
		elif step == 1:
			# clean up and finish
			self.canvas.itemconfig(self.graphic[n][0], fill="white")
			return


	def _put_animation(self, n, val, step):
		"""animation of put operation"""
		if step == 0:
			# highlight the entry to be changed
			self.canvas.itemconfig(self.graphic[n][0], fill="green")
			self.canvas.after(500, self._put_animation, n, val, 1)
		elif step == 1:
			# update the value in the entry
			self.canvas.itemconfig(self.graphic[n][1], text=str(val))
			self.canvas.after(1500, self._put_animation, n, val, 2)
		elif step == 2:
			# clean up and finish
			self.canvas.itemconfig(self.graphic[n][0], fill="white")
			return


	def _find_animation(self, val, step, n):
		"""animation of find operation"""
		if n == self._max_length-1 and step != 3:
			# value not found, alert with red entry
			self.canvas.itemconfig(self.graphic[n][0], fill="red")
			self.canvas.after(500, self._find_animation, val, 3, n)
		elif step == 0:
			# highlight current entry blue and check if found value
			self.canvas.itemconfig(self.graphic[n][0], fill="blue")
			if self._vals[n] == val:
				self.canvas.after(250, self._find_animation, val, 2, n)
			else:
				self.canvas.after(500, self._find_animation, val, 1, n)
		elif step == 1:
			# value not found, move to next entry
			self.canvas.itemconfig(self.graphic[n][0], fill="white")
			self.canvas.after(0, self._find_animation, val, 0, n+1)
		elif step == 2:
			# value found, show value for 1.5s and return
			self.canvas.itemconfig(self.graphic[n][0], fill="green")
			self.canvas.after(1500, self._find_animation, val, 3, n)
		elif step == 3:
			# clean up and finish
			self.canvas.itemconfig(self.graphic[n][0], fill="white")
			return