def fibonacci(n):
	a,b = 1,1
	while a < n:
		if a%2 == 0:
			yield a 
		a,b = b,a+b 

print(sum(fibonacci(4000000)))