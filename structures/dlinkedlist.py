class DLinkedList(object):
	"""Implementation of doubly linked list with standard methods"""
	_title = "Doubly linked list"

	class Node(object):
		"""Single node of the doubly linked list with a value"""
		def __init__(self, val):
			"""
			Initialise a node

			:param val: data held in the node
			:type val: T
			"""
			self.val = val
			self.prev = None
			self.next = None


	def __init__(self, vals=[]):
		"""
		Initialise a doubly linked list given an array of values

		:param vals: values for the list
		:type vals: T[]
		"""
		self.length = len(vals)

		if not vals:
			self.head = None
			self.tail = None
			return

		self.head = DLinkedList.Node(vals[0])

		dummy = self.head

		for i, v in enumerate(vals[1:]):
			self.head.next = DLinkedList.Node(v)
			self.head.next.prev = self.head
			self.head = self.head.next

			if i == len(vals)-2:
				self.tail = self.head

		self.head = dummy
		self.iter = self.head


	def __iter__(self):
		"""Iterator"""
		self.iter = self.head
		return self


	def __next__(self):
		"""For iterator"""
		if not self.iter:
			raise StopIteration
		else:
			prev = self.iter
			self.iter = self.iter.next
			return prev


	def __repr__(self):
		"""Return representation of the list"""
		return "DLinkedList([" + ','.join([str(n.val) for n in self]) + "])"


	def __str__(self):
		"""Return str(self)"""
		return ' <-> '.join([str(n.val) for n in self])


	def reverse(self):
		"""Reverse the list"""
		for node in self:
			node.next, node.prev = node.prev, node.next

		self.head, self.tail = self.tail, self.head


	def lookup(self, n):
		"""
		Find the n-th value in the list

		Returns an error if n is out of bounds of the list

		:param n: index to get
		:type n: int
		"""
		if n > self.length-1:
			raise IndexError("index out of range")
		else:
			dummy = self.head

			for i in range(n):
				dummy = dummy.next

			return dummy.val


	def insertBefore(self, val, p): 
		"""
		Insert a value to a new node before the given node p

		:param val: value to be inserted
		:param p: successor node
		:type val: T
		:type p: Node
		"""
		current_predecessor = p.prev
		p.prev = DLinkedList.Node(val)
		p.prev.next = p
		p.prev.prev = current_predecessor

		if current_predecessor:
			p.prev.prev.next = p.prev

		if p == self.head:
			self.head = self.head.prev

		self.length += 1


	def insertAfter(self, val, p): 
		"""
		Insert a value to a new node after the given node p

		:param val: value to be inserted
		:param p: predecessor node
		:type val: T
		:type p: Node
		"""
		current_successor = p.next
		p.next = DLinkedList.Node(val)
		p.next.prev = p
		p.next.next = current_successor

		if current_successor:
			p.next.next.prev = p.next

		if p == self.tail:
			self.tail = self.tail.next

		self.length += 1


	def insertFirst(self, val):
		"""
		Insert a value at the beginning of the list

		:param val: value to be inserted
		:type val: T
		"""
		if self.head:
			new_head = DLinkedList.Node(val)
			new_head.next = self.head
			self.head.prev = new_head
			self.head = new_head
		else:
			self.tail = DLinkedList.Node(val)
			self.head = self.tail

		self.length += 1


	def insertLast(self, val):
		"""
		Insert a value at the end of the list

		:param val: value to be inserted
		:type val: T
		"""
		if self.head:
			new_tail = DLinkedList.Node(val)
			new_tail.prev = self.tail
			self.tail.next = new_tail
			self.tail = new_tail
		else:
			self.tail = DLinkedList.Node(val)
			self.head = self.tail

		self.length += 1


	def remove(self, p):
		"""
		Remove a node after the given node if it exists

		:param p: predecessor node
		:type p: Node
		"""
		if p.next:
			p.next = p.next.next
			p.next.prev = p
			self.length -= 1


	def removeFirst(self):
		"""Remove the first node of the list if it exists"""
		if self.head:
			self.head = self.head.next
			
			if self.head:
				self.head.prev = None

			self.length -= 1


	def removeLast(self):
		"""Remove the last node of the list if it exists"""
		if self.tail:
			self.tail = self.tail.prev
			self.tail.next = None
			self.length -= 1


	def delete(self, target):
		"""
		Delete the first value val if it can be found in the list

		:param target: value to be deleted
		:type target: T
		"""
		dummy = self.head

		if self.head.val == target:
			self.head = self.head.next
			self.head.prev = None
			self.length -= 1
		else:
			while self.head.next:
				if self.head.next.val == target:
					self.head.next = self.head.next.next
					if self.head.next:
						self.head.next.prev = self.head
					else:
						self.tail = self.tail.prev
						
					self.length -= 1
					break

				self.head = self.head.next

			self.head = dummy