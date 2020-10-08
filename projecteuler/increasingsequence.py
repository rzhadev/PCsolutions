def increasing_sequence(mylist):
	for x in range(0,len(mylist)):
		if mylist[x] < mylist[x-1] or mylist[x] > mylist[x+1]:
			mylist.remove(mylist[x])
			break 
	return all(x<y for x,y in zip(mylist, mylist[1:]))
	
print(increasing_sequence([5,1,2,3,4]))






