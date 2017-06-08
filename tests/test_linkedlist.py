import sys
import pytest
sys.path.append('../') # to make folders with code visible

from structures.linkedlist import *

class TestClass(object):

	def test_main(self):
		l = LinkedList([1,2,3,4])

		assert str(l) == "1 -> 2 -> 3 -> 4"


	def test_length(self):
		pass


	def test_lookup(self):
		l = LinkedList([1,2,3,4])

		assert l.lookup(2) == 3
		assert l.lookup(3) == 4

		with pytest.raises(IndexError):
			l.lookup(4)


	def test_insert(self):
		l = LinkedList([1,2,3,4])
		l.insert(3, l.head)

		assert str(l) == "1 -> 3 -> 2 -> 3 -> 4"

		l = LinkedList([1,2,3,4])
		l.insert(3, l.head.next.next.next)

		assert str(l) == "1 -> 2 -> 3 -> 4 -> 3"


	def test_insertFirst(self):
		l = LinkedList([1,2,3,4])
		l.insertFirst(0)

		assert str(l) == "0 -> 1 -> 2 -> 3 -> 4"


	def test_remove(self):
		l = LinkedList([1,2,3,4])
		l.remove(l.head)

		assert str(l) == "1 -> 3 -> 4"

		l = LinkedList([1,2,3,4])
		l.remove(l.head.next.next.next)

		assert str(l) == "1 -> 2 -> 3 -> 4"


	def test_removeFirst(self):
		l = LinkedList([1,2,3,4])
		l.removeFirst()

		assert str(l) == "2 -> 3 -> 4"


	def test_delete(self):
		l = LinkedList([1,2,3,4])
		l.delete(1)

		assert str(l) == "2 -> 3 -> 4"

		l = LinkedList([1,2,3,4])
		l.delete(5)

		assert str(l) == "1 -> 2 -> 3 -> 4"