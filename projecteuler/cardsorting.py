values = {"Ace":1,"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Tens":10,"Jack":10,"Queen":10,"King":10}
cards = ["Eight","Nine","Four","Jack","Queen","Three","One","Ace"]
def sort_Deck(cards,values):
	sorted_deck = False
	while not sorted_deck:
		sorted_deck = True
		for x in range(0,len(cards)-1):
			if values[cards[x]] > values[cards[x+1]]:
				cards[x],cards[x+1] = cards[x+1],cards[x]
				sorted_deck = False
	return cards

print(sort_Deck(cards,values))


