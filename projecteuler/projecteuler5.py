def smallest_multiple(step):
	check_list = [11,13,14,16,17,18,19,20] #replaces a range 
	for num in range(step,999999999,step): #starts at 20 and steps by 20 
		if all(num % n == 0 for n in check_list): #generator expression		
			return num 
	return None 

print(smallest_multiple(20))




