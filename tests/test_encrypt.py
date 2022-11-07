import pytest
from passwordManager import encrypt

class Tests:
	def test_odd_chars(self):
		encrypted = encrypt.encryptFunction("hello")
		assert encrypted == "morqu{hnwpx'mw)"
	
	def test_even_chars(self):
		encrypted = encrypt.encryptFunction("test")
		assert encrypted == "tvyvz#w})iq}"
		
	def test_len_2(self):
		encrypted = encrypt.encryptFunction("~}")
		assert encrypted == "\"$'\"&,"
	
	def test_len_1(self):
		encrypted = encrypt.encryptFunction("A")
		assert encrypted == "BDG"