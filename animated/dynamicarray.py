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
	_title = "Dynamic array"

	def __init__(self, canvas, vals=[]):
		"""
		Initialise the array with optional initial values

		According to the growth factor, the initial length of the array 
		will be equal to 1.5 of the length of the argument

		If no initial values are given or just one value is given
		initial length will be equal to 2

		:param vals: optional initial values for the array
		:type vals: T[]
		"""
		self.canvas = canvas
		self._arr = array.Array(max(3*len(vals)//2, 2), vals)
		self._length = len(vals)
		self._max_length = max(3*len(vals)//2, 2)

		# graphical representation of dynamic array
		self.graphic = []
		for i, val in enumerate(self._arr._vals):
			if i < self._length:
				rect = canvas.create_rectangle(50*i+50, canvas.winfo_reqheight()//2-25, 50*i+100, canvas.winfo_reqheight()//2+25, fill="white")
				text = canvas.create_text((50*i+75, canvas.winfo_reqheight()//2), text=str(val))
			else:
				rect = canvas.create_rectangle(50*i+50,\
											   canvas.winfo_reqheight()//2-25,\
											   50*i+100,\
											   canvas.winfo_reqheight()//2+25,\
											   dash=(5,5))
				text = canvas.create_text((50*i+75, canvas.winfo_reqheight()//2), text="")
			self.graphic.append((rect, text))


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
			self._lookup_animation(n, 0)
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
			self._update_animation(n, val, 0)
			self._arr.put(n, val)
		else:
			raise IndexError("index out of bounds")


	def insert(self, n, val):
		"""
		Insert value at the n-th position of the array

		If the array is full, make a new array of size 3/2 of the old one

		Raises error if n out of bounds of the array

		:param n: index in the array
		:param val: value to insert
		:type n: int
		:type val: T
		"""
		if n < self._length and n >= 0:
			if self._length < self._max_length:
				self._arr = array.Array(self._max_length, self._arr._vals[:n] + [val] + self._arr._vals[n:self._length])
			else:
				self._arr = array.Array(3*self._max_length//2, self._arr._vals[:n] + [val] + self._arr._vals[n:self._length])
				self._max_length = 3*self._max_length//2

			self._length += 1
		else:
			raise IndexError("index out of bounds")


	def insertLast(self, value):
		"""
		Insert value at the end of the array

		If the array is full, make a new array of size 3/2 of the old one

		:param value: value to insert
		:type value: T
		"""
		if self._length < self._max_length:
			self._arr.put(self._length, value)
			self._length += 1
			self._insertLastNotFull_animation(value, 0)
		else:
			self._arr = array.Array(3*self._max_length//2, self._arr._vals[:self._length] + [value])
			self._max_length = 3*self._max_length//2
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


	def find(self, value):
		"""
		Returns an index of the first occurence of value in the array

		If value is not found, returns -1

		:param value: index in the array:
		:type value: int
		"""
		self._find_animation(value, 0, 0)
		return self._arr.find(value)


	def _lookup_animation(self, n, step):
		"""Animation of the lookup operation"""
		if step == 0:
			# highlight the entry looked up
			self.canvas.itemconfig(self.graphic[n][0], fill="green")
			self.canvas.after(1500, self._lookup_animation, n, 1)
		elif step == 1:
			# clean up and finish
			self.canvas.itemconfig(self.graphic[n][0], fill="white")
			return


	def _insertNotFull_animation(self, n, val, step):
		"""Animation of the insert operation to not full array"""
		pass


	def _insertFull_animation(self, n, val, step):
		"""Animation of the insert operation to full array"""
		pass


	def _insertLastNotFull_animation(self, val, step):
		"""Animation of insertion at last place if the array is not full"""
		if step == 0:
			self.canvas.itemconfig(self.graphic[self._length-1][0], dash=(), fill="green")
			self.canvas.after(500, self._insertLastNotFull_animation, val, 1)
		elif step == 1:
			self.canvas.itemconfig(self.graphic[self._length-1][1], text=str(val))
			self.canvas.after(1500, self._insertLastNotFull_animation, val, 2)
		elif step == 2:
			self.canvas.itemconfig(self.graphic[self._length-1][0], fill="white")
			return


	def _insertLastFull_animation(self, val, step):
		"""Animation of insertion at last place if the array is full"""
		pass


	def _removeNoResize_animation(self, n, step):
		"""Animation of removal if no resizing is needed"""
		pass


	def _removeResize_animation(self, n, step):
		"""Animation of removal if resizing is needed"""
		pass


	def _removeLastNoResize_animation(self, step):
		"""Animation of removal from last place if no resizing is needed"""
		pass


	def _removeLastResize_animation(self, step):
		"""Animation of removal from last place if resizing is needed"""
		pass


	def _update_animation(self, n, val, step):
		"""Animation of the update operation"""
		if step == 0:
			# highlight the entry looked up
			self.canvas.itemconfig(self.graphic[n][0], fill="green")
			self.canvas.after(500, self._update_animation, n, val, 1)
		elif step == 1:
			# update the entry with value
			self.canvas.itemconfig(self.graphic[n][1], text=str(val))
			self.canvas.after(1500, self._update_animation, n, val, 2)
		elif step == 2:
			# clean up and finish
			self.canvas.itemconfig(self.graphic[n][0], fill="white")
			return


	def _find_animation(self, val, step, n):
		"""Animation of the find operation"""
		if step == 0:
			# highlight current entry yellow and check if found value
			self.canvas.itemconfig(self.graphic[n][0], fill="yellow")
			if self._arr._vals[n] == val:
				self.canvas.after(250, self._find_animation, val, 2, n)
			else:
				self.canvas.after(500, self._find_animation, val, 1, n)
		elif n == self._length-1 and step < 2:
			# value not found, alert with red entry
			self.canvas.itemconfig(self.graphic[n][0], fill="red")
			self.canvas.after(500, self._find_animation, val, 3, n)
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
