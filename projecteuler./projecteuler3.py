def largest_prime(n):
	i = 2
	while i*i < n:
		while n%i == 0:
			n = n/i
		i += 1
	return n 

print(largest_prime(600851475143))