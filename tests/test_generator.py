import pytest
from passwordManager import generator, validate

class Tests: 
    def test_input_below_6(self):
        password = generator.generate_password(3)
        assert validate.validate_password(password) == True
        assert len(password) != 3
        
        
    def test_input_above__15(self):
        password = generator.generate_password(20)
        assert validate.validate_password(password) == True
        assert len(password) != 20
        
    def test_input_within_range(self):
        password1 = generator.generate_password(6)
        assert validate.validate_password(password1) == True
        assert len(password1) == 6
        password2 = generator.generate_password(15)
        assert validate.validate_password(password2) == True
        assert len(password2) == 15
        
    def test_with_no_input(self):
        password = generator.generate_password()
        assert len(password) >= 6
        assert len(password) <= 15
        assert validate.validate_password(password) == True
        
    