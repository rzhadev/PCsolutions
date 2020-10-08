def problemone(crystalColors):
	colors = {'r':0,'g':0,'b':0} 
	for color in crystalColors:
		colors[color.lower()] += 1

	if colors['r'] == colors['g'] == colors['b']:
		return colors.values()
	else:
		return None 

print(problemone(['R','G','B','R','R','G','G','B','B','R','G','R','G','R','G','B','B','B']))
		
	



