import pytest
from passwordManagerByAscii import validate

class Tests:
	def test_success_case(self):
		assert validate.validate_password('@A23124') == True
		assert validate.validate_password('asc3#A24') == True
		assert validate.validate_password('Cdqs@4vd') == True
		assert validate.validate_password('Password123@') == True

	
	def test_no_capital(self):
		assert validate.validate_password('123a@cc') == False
		assert validate.validate_password('@cxv353l') == False
		assert validate.validate_password('@#ccavw12') == False

		
	def test_no_special_character(self):
		assert validate.validate_password('Camvf1d') == False
		assert validate.validate_password('MEC0js14m') == False
		assert validate.validate_password('passwordis123') == False

	
	def test_no_number(self):
		assert validate.validate_password('bkdQ@#c') == False
		assert validate.validate_password('mlCdo$@ca') == False
		assert validate.validate_password('pnckqpi!A') == False


	def test_less_than_6(self):
		assert validate.validate_password('cAq1@') == False
		assert validate.validate_password('Pd2#') == False
		assert validate.validate_password('B#1dx') == False


	def test_combination(self):
		assert validate.validate_password('cAqca') == False
		assert validate.validate_password('P22xa') == False
		assert validate.validate_password('B#aQ') == False
