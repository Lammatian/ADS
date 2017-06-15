import sys
import pytest
sys.path.append('../')

from structures.array import Array

class TestClass(object):

	def test_main(self):
		a = Array(3, [1,2])

		assert str(a) == "[1, 2, None]"


	def test_lookup(self):
		a = Array(3, [1,2])

		assert a.lookup(0) == 1

		with pytest.raises(IndexError):
			a.lookup(3)

		with pytest.raises(IndexError):
			a.lookup(-1)


	def test_put(self):
		a = Array(3, [1,2])
		a.put(1, 5)

		assert str(a) == "[1, 5, None]"

		a = Array(3, [1,2,3])

		with pytest.raises(IndexError):
			a.put(-1, 0)

		with pytest.raises(IndexError):
			a.put(3, 0)


	def test_find(self):
		a = Array(3, [1,2,3])

		assert a.find(1) == 0
		assert a.find(3) == 2
		assert a.find(5) == -1