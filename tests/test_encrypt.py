import pytest
from passwordManagerByAscii import encrypt

class Tests:
	def test_odd_chars(self):
		encrypted = encrypt.encode_password("hello")
		assert encrypted == "morqu{hnwpx'mw)"
	
	def test_even_chars(self):
		encrypted = encrypt.encode_password("test")
		assert encrypted == "tvyvz#w})iq}"
		
	def test_len_2(self):
		encrypted = encrypt.encode_password("~}")
		assert encrypted == "\"$'\"&,"
	
	def test_len_1(self):
		encrypted = encrypt.encode_password("A")
		assert encrypted == "BDG"