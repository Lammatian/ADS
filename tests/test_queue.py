import sys
import pytest
sys.path.append('../')

from structures.queue import Queue

class TestClass(object):

	def test(self):
		q = Queue()

		assert q.peek() == None
		assert q.isEmpty()

		q.enqueue(1)

		assert not q.isEmpty()
		assert q.peek() == 1
		assert q.dequeue() == 1
		assert q.peek() == None
		assert q.isEmpty()

		q.enqueue(1)
		q.enqueue(2)

		assert q.peek() == 1
		assert q.dequeue() == 1
		assert q.peek() == 2
		assert q.dequeue() == 2
		assert q.dequeue() == None