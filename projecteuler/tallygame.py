def tallygame(input_string):
	totals = {'a':0,'b':0,'c':0,'d':0,'e':0}
	for character in input_string:
		if character == character.lower():
			totals[character.lower()] += 1
		elif character == character.upper():
			totals[character.lower()] -= 1
	ordered_scores = [(v,k) for (k,v) in totals.items()] 
	
	ordered_scores1 = sorted(ordered_scores)
	ordered_scores1.reverse()
	return ordered_scores1






