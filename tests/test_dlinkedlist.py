import sys
import pytest
sys.path.append('../') # to make folders with code visible

from structures.dlinkedlist import *

class TestClass(object):

	def test_main(self):
		l = DLinkedList([1,2,3,4])

		assert str(l) == "1 <-> 2 <-> 3 <-> 4"
		assert l.length == 4


	def test_lookup(self):
		l = DLinkedList([1,2,3,4])

		assert l.lookup(2) == 3
		assert l.lookup(3) == 4

		with pytest.raises(IndexError):
			l.lookup(4)


	def test_insertBefore(self):
		l = DLinkedList([1,2,3,4])
		l.insertBefore(5, l.head)

		assert str(l) == "5 <-> 1 <-> 2 <-> 3 <-> 4"
		assert l.length == 5
		assert l.head.val == 5

		l = DLinkedList([1,2,3,4])
		l.insertBefore(5, l.tail)

		assert str(l) == "1 <-> 2 <-> 3 <-> 5 <-> 4"
		assert l.length == 5


	def test_insertAfter(self):
		l = DLinkedList([1,2,3,4])
		l.insertAfter(3, l.head)

		assert str(l) == "1 <-> 3 <-> 2 <-> 3 <-> 4"
		assert l.length == 5

		l = DLinkedList([1,2,3,4])
		l.insertAfter(5, l.tail)

		assert str(l) == "1 <-> 2 <-> 3 <-> 4 <-> 5"
		assert l.length == 5
		assert l.tail.val == 5


	def test_insertFirst(self):
		l = DLinkedList([1,2,3,4])
		l.insertFirst(0)

		assert str(l) == "0 <-> 1 <-> 2 <-> 3 <-> 4"
		assert l.length == 5
		assert l.head.val == 0


	def test_insertLast(self):
		l = DLinkedList([1,2,3,4])
		l.insertLast(5)

		assert str(l) == "1 <-> 2 <-> 3 <-> 4 <-> 5"
		assert l.length == 5
		assert l.tail.val == 5


	def test_remove(self):
		l = DLinkedList([1,2,3,4])
		l.remove(l.head)

		assert str(l) == "1 <-> 3 <-> 4"
		assert l.length == 3

		l = DLinkedList([1,2,3,4])
		l.remove(l.head.next.next.next)

		assert str(l) == "1 <-> 2 <-> 3 <-> 4"
		assert l.length == 4


	def test_removeFirst(self):
		l = DLinkedList([1,2,3,4])
		l.removeFirst()

		assert str(l) == "2 <-> 3 <-> 4"
		assert l.length == 3
		assert l.head.val == 2


	def test_removeLast(self):
		l = DLinkedList([1,2,3,4])
		l.removeLast()

		assert str(l) == "1 <-> 2 <-> 3"
		assert l.length == 3
		assert l.tail.val == 3


	def test_delete(self):
		l = DLinkedList([1,2,3,4])
		l.delete(1)

		assert str(l) == "2 <-> 3 <-> 4"
		assert l.length == 3
		assert l.head.val == 2

		l = DLinkedList([1,2,3,4])
		l.delete(4)

		assert str(l) == "1 <-> 2 <-> 3"
		assert l.length == 3
		assert l.tail.val == 3

		l = DLinkedList([1,2,3,4])
		l.delete(5)

		assert str(l) == "1 <-> 2 <-> 3 <-> 4"
		assert l.length == 4