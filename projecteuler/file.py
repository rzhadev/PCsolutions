#Assignment 7 Text-Based Game

#Welcome User
print("Hello! Welcome to the game! Please input your name, good sir.")
name = input("Insert name: ")
print("Welcome", name, "! Here's how to play the game.")

#Directions
print("Thy quest shall be to findeth the wooden door in the dinette.")
print("To moveth 'long useth the words north, east, south, west.")

#find what room the player is in
def find_room(x,y):
	if(x >= 0 and x < 5 and y >= 0 and y < 5):
		return "first room"
	elif(x >= 5 and x < 10 and y >= 0 and y < 5):
		return "second room"
	elif(x >= 0 and x < 5 and y >= 5 and y < 10):
		return "third room"
	else:
		return "fourth room"
#make a grid and fill with zeroes
matrix = []
for a in range(10): #add new a list
	matrix.append([])
	for b in range(10): #add 5 zeroes to the new list
		matrix[a].append(0)
#start the player at 0,0 on the grid
player_x = 0
player_y = 0
#the location of the door
door_x = 7
door_y = 7
#number of steps 
counter = 0

#game loop
while player_x != door_x or player_y != door_y:
	directions = input("What direction would you like to go in?:")
	walk = int(input("How many steps would you like to take? Choose only a number 1-3:"))
	if(walk > 3):
		print("That number is too big!")
		continue
	elif(walk < 1):
		print("That number is too small!")
		continue
	if directions == "north" and player_x - walk > 0:
		player_x -= walk
	elif directions == "south" and player_x + walk <= len(matrix)-1:
		player_x += walk
	elif directions == "west" and player_y - walk > 0:
		player_y -= walk
	elif directions == "east" and player_y + walk <= len(matrix)-1: 
		player_y += walk
	else:
		print("You ran into a wall")
		continue
	print("You are in the "+find_room(player_x,player_y))
	print("You are currently at "+str(player_x)+" "+str(player_y))
	counter += 1

print("Thee hath found the door.")
print("It took you "+str(counter)+" steps")