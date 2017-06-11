import sys
import pytest
sys.path.append('../')

from structures.stack import *

class TestClass(object):

	def test(self):
		s = Stack()

		assert s.peek() == None
		assert s.isEmpty()

		s.push(1)

		assert not s.isEmpty()
		assert s.peek() == 1
		assert s.pop() == 1
		assert s.isEmpty()

		s.pop()
		s.push(1)
		s.push(2)

		assert s.peek() == 2
		assert s.pop() == 2
		assert s.pop() == 1