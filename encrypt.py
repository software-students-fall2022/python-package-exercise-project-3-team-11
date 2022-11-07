def encrypt (string):
	nonencrypted = string[::-1]
	first_l = [ord(c) for c in nonencrypted]
	swapped_l = []
	for i in range(0, len(first_l)/2):
		if len(first_l)/2 % 2 == 0:
			swapped_l.append(first_l[2*i+1])
			swapped_l.append(first_l[2*i])
		else:
			swapped_l.append(first_l[2*i+1])
			swapped_l.append(first_l[2*i])
			swapped_l.append(first_l[(len(first_l)/2)-1])
	for j in range(0, len(swapped_l)):	
		if swapped_l[j]+(j+1) > 126:
			first = swapped_l[j]+(j+1)-126+33
			swapped_l[j]=first
			second = first + 2*(j+1)
			if second > 126:
				second = second-126+33
			swapped_l.insert(j+1, second)
			third = second + 3*(j+1)
			if third > 126:
				third = third-126+33
			swapped_l.insert(j+2, third)
		else:
			first = swapped_l[j]+(j+1)
			second = first + 2*(j+1)
			if second > 126:
				second = second-126+33
			swapped_l.insert(j+1, second)
			third = second + 3*(j+1)
			if third > 126:
				third = third-126+33
			swapped_l.insert(j+2, third)
	encrypted = ""
	for i in swapped_l:
    	encrypted = encrypted + chr(i)
    return encrypted
    
			

