def encrypt (string):
	nonencrypted = string
	first_l = [ord(c) for c in s]
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
		if swapped_l[j] == 33:
			swapped_l[j] = 126
		else:
			swapped_l[j] = swapped_l[j-1]
	for k in range(0, len(swapped_l)):
		if swapped_l[k] > 64:
			swapped_l[k] = swapped_l[k]*2-126+33
		else:
			swapped_l[k] = swapped_l[k]*2
	encrypted = ""
	for i in swapped_l:
    	encrypted = encrypted + chr(i)
    return encrypted
    
			

