import pytest
from passwordManager import validate

class Tests:
	def test_input_below_6(self):
		validate = validate.validate_password("hello")
		assert validate.validate_password(password) == True