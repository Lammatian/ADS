import sys
sys.path.append('../')

from structures.array import *

class A_Array(Array):
	"""
	Animated array as an extension of Array

	Each operation has its own animation
	"""
	def __init__(self, canvas, length, values=[]):
		"""
		Initialise the array with obligatory length and optional initial values

		:param length: length of the array
		:param values: initial values
		:param canvas: canvas on which the array will be drawn
		:type length: int
		:type values: T[]
		:type canvas: tkinter.Canvas
		"""
		super(A_Array, self).__init__(length, values)

		# graphical representation of the data structure
		self.canvas = canvas
		self.graphic = []

		for i, val in enumerate(self._vals):
			rect = canvas.create_rectangle(50*i+50, canvas.winfo_reqheight()//2-25, 50*i+100, canvas.winfo_reqheight()//2+25, fill="white")
			text = canvas.create_text((50*i+75, canvas.winfo_reqheight()//2), text=str(val))
			self.graphic.append((rect, text))


	def lookup(self, index):
		"""Call lookup of Array and animation"""
		self._lookup_animation(index, 0)

		return super(A_Array, self).lookup(index)


	def put(self, index, value):
		"""Call put of Array and animation"""
		super(A_Array, self).put(index, value)

		self._put_animation(index, value, 0)


	def find(self, value):
		"""Call find of Array and animation"""
		self._find_animation(value, 0, 0)

		return super(A_Array, self).find(value)


	def _lookup_animation(self, n, step):
		"""
		Animation of lookup operation
		
		Step parameter to keep track of the progress
		"""
		if n < 0 or n >= self._max_length:
			return
		else:
			if step == 0:
				# highlight the entry looked up
				self.canvas.itemconfig(self.graphic[n][0], fill="green")
				self.canvas.after(1500, self._lookup_animation, n, 1)
			elif step == 1:
				# clean up and finish
				self.canvas.itemconfig(self.graphic[n][0], fill="white")
				return


	def _put_animation(self, n, val, step):
		"""
		Animation of put operation
		
		Step parameter to keep track of the progress
		"""
		if n < 0 or n >= self._max_length:
			return
		else:
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
		"""
		Animation of find operation

		Step and n parameters to keep track of the progress
		"""
		if step == 0:
			# highlight current entry yellow and check if found value
			self.canvas.itemconfig(self.graphic[n][0], fill="yellow")
			if self._vals[n] == val:
				self.canvas.after(250, self._find_animation, val, 2, n)
			else:
				self.canvas.after(500, self._find_animation, val, 1, n)
		elif n == self._max_length-1 and step < 2:
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