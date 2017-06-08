class Node(object):
	"""Single node of the linked list with a value"""

	def __init__(self, val):
		"""
		Initialise a node

		:param val: data held in the node
		:type val: T
		"""

		self.val = val
		self.next = None


class LinkedList(object):
	"""Implementation of linked list with standard methods"""

	def __init__(self, vals):
		"""
		Initialise a linked list given an array of values

		:param vals: values for the list
		:type vals: T[]
		"""

		self.length = len(vals)

		if not vals:
			self.head = None
			return

		self.head = Node(vals[0])

		dummy = self.head

		for v in vals[1:]:
			self.head.next = Node(v)
			self.head = self.head.next

		self.head = dummy

	def lookup(self, n):
		"""
		Find the n-th value in the list

		Returns an error if n is out of bounds of the linked list

		:param n: index to get
		:type n: int
		"""

		if n > self.length:
			return "Out of bounds."
		else:
			dummy = self.head

			for i in range(n):
				dummy = dummy.next

			return dummy.val

	def insert(self, val, p): 
		"""
		Insert a value to a new node after the given node p

		:param val: value to be inserted
		:param p: predecessor node
		:type val: T
		:type p: Node
		"""

		current_successor = p.next
		p.next = Node(val)
		p.next.next = current_successor

	def insertFirst(self, val):
		"""
		Insert a value at the beginning of the list

		:param val: value to be inserted
		:type val: T
		"""

		new_head = Node(val)
		new_head.next = self.head
		self.head = new_head

	def remove(self, p):
		"""
		Remove a node after the given node if it exists

		:param p: predecessor node
		:type p: Node
		"""

		if p.next:
			p.next = p.next.next

	def removeFirst(self):
		"""Remove the first node of the list if it exists"""

		if self.head:
			self.head = self.head.next

	def delete(self, target):
		"""
		Delete the first value val if it can be found in the list

		:param target: value to be deleted
		:type target: T
		"""

		dummy = self.head

		if self.head.val == target:
			self.head = self.head.next
		else:
			while self.head.next:
				if self.head.next.val == target:
					self.head.next = self.head.next.next
					break

				self.head = self.head.next

			self.head = dummy

	def show(self):
		"""For testing"""
		dummy = self.head

		while dummy:
			print(dummy.val, end="")

			if dummy.next:
				print(" -> ", end="")

			dummy = dummy.next

		print()
