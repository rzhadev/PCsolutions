def series(n):
	end_sum = 0 
	for x in range(0,n):
		if x%2 == 0:
			end_sum += 4/(2*x + 1)
		else:
			end_sum -= 4/(2*x + 1)
	return end_sum


print(series(100000000))