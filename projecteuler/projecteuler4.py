def palindromatic():
	mylist = [] 
	for a in range(999,100,-1):
		for b in range(999,100,-1):
			n = a*b
			if str(n) == str(n)[::-1]:
				mylist.append(n)
	return max(mylist)

print(palindromatic())