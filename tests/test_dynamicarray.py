import sys
import pytest
sys.path.append('../') # to make folders with code visible

from structures.dynamicarray import *
from structures.array import *

class TestClass(object):

	def test_main(self):
		a = DArray([1,2])

		assert str(a) == "[1, 2]"
		assert a.length == 2


	def test_lookup(self):
		a = DArray([1,2])

		assert a.lookup(0) == 1

		with pytest.raises(IndexError):
			a.lookup(2)

		with pytest.raises(IndexError):
			a.lookup(-1)


	def test_update(self):
		a = DArray([1,2,3])
		a.update(0, 4)

		assert str(a) == "[4, 2, 3]"
		assert a.length == 3

		a = DArray([1,2,3])
		a.update(2, 4)

		assert str(a) == "[1, 2, 4]"

		with pytest.raises(IndexError):
			a.update(-1, 5)

		with pytest.raises(IndexError):
			a.update(3, 5)


	def test_insert(self):
		a = DArray([1,2])
		a.insert(1, 5)

		assert str(a) == "[1, 5, 2]"
		assert a.length == 3

		a = DArray([1,2,3])

		a.insert(1, 0)

		assert str(a) == "[1, 0, 2, 3]"

		with pytest.raises(IndexError):
			a.insert(-1, 0)

		with pytest.raises(IndexError):
			a.insert(4, 0)


	def test_insertLast(self):
		a = DArray([1,2])
		a.insertLast(3)

		assert str(a) == "[1, 2, 3]"
		assert a.length == 3


	def test_remove(self):
		a = DArray([1,2,3])
		a.remove(2)

		assert str(a) == "[1, 2]"
		assert a.length == 2

		a.remove(1)

		assert str(a) == "[1]"
		assert a.length == 1

		with pytest.raises(IndexError):
			a.remove(1)


	def test_removeLast(self):
		a = DArray([1,2])
		a.removeLast()

		assert str(a) == "[1]"
		assert a.length == 1

		a.removeLast()

		assert str(a) == "[]"
		assert a.length == 0

		a.removeLast()

		assert str(a) == "[]"
		assert a.length == 0


	def test_find(self):
		a = DArray([1,2,3])

		assert a.find(1) == 0
		assert a.find(3) == 2
		assert a.find(5) == -1