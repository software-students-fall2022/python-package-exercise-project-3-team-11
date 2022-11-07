import pytest
from passwordManager import generator

class Tests: 
    def test_input_below_6(self):
        password = generator.generate_password(3)
        assert len(password) != 3
        # also need to validate password format using the validate method
    def test_input_above__15(self):
        password = generator.generate_password(20)
        assert len(password) != 20