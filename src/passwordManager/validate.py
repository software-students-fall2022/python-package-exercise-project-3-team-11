# Password: 
# 1  capital, 1 number, 1 special character, minimum 6 characters
# (Character: ASCII range 33~126) 

def validate_password(password):
	'''
	Validate password

	1 capital, 1 number, 1 special character, minimum 6 characters
	
	@params str password

	@returns bool (valid or not)
	'''
	has_capital = False
	has_number = False
	has_special_chr = False
	has_min_six_chr = False

	for chr in password:
		if 65 <= ord(chr) <= 90:
			has_capital = True
		elif 48 <= ord(chr) <= 57:
			has_number = True
		elif 97 <= ord(chr) <= 122:
			pass
		elif 33 <= ord(chr) <= 126:
			has_special_chr = True

	if len(password) >= 6:
		has_min_six_chr = True

	return has_capital and has_number and has_special_chr and has_min_six_chr

password = input('Enter your password: ')
if validate_password(password) == False:
	print("This password is invalid. Password should have at least 6 characters with 1 special character, 1 capital, and 1 number.")

'''
To test function
print(validate_password('@A23124') == True)
print(validate_password('1223124') == False)
print(validate_password('A23124') == False)
print(validate_password('@A24') == False)
print(validate_password('asc3#A24') == True)
'''