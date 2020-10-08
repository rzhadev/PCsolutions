def special_triplet(n):
	for a in range(3,n):
		for b in range(4,n):
			c = n - a - b
			if c**2 == a**2 + b**2:
				return a*b*c
print(special_triplet(1000))