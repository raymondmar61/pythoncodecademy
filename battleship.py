from random import randint

#A single ship is hidden in a random location on a 5x5 grid. The player will have 10 guesses to try to sink the ship.
board = []

#generate our board, which we'll make into a 5 x 5 grid of all "O"s, for "ocean."
for i in range(0,5):
	board.append(["O"] * 5)

#our board is a list of lists to help us do this. Let's set up a for loop to go through each of the elements in the outer list (each of which is a row of our board) and print them.
def print_board(board):
	for row in board:
		#get rid of those quote marks and commas.  The .join method uses the string to combine the items in the list.
		print(" ".join(row))
print_board(board)

#we'll use two variables to store the ship's location, ship_row and ship_col
#we first import the randint(low, high) function from the random module.  low and high are inclusive.
#Let's generate a random_row and random_col from zero to four!
def random_row(board):
	return (randint(0,len(board)-1))
def random_col(board):
	return (randint(0,len(board)-1))
#store coordinates for the ship in the variables ship_row and ship_col
ship_row = random_row(board) #python3.5 didn't like ship_row = print(random_row(board))
ship_col = random_col(board)
print(ship_row)
print(ship_col)

#our game to allow the player to make up to 4 guesses before they lose.  range(4) is 0, 1, 2, 3
counter = 1
for turn in range(4):
	#counter, initialize counter one line above for loop
	print("Turn" ,counter)
	counter = counter + 1
	#input guess
	guess_row = int(input("Guess Row: "))
	guess_col = int(input("Guess Col: "))

	#For a guess to be right, guess_col should be equal to ship_col and guess_row should be equal to ship_row
	#we can handle both correct and incorrect guesses from the user
	if ((guess_row == ship_row) and (guess_col == ship_col)):
		print("Congratulations! You sank my battleship!")
		#winner end program use break or quit()
		break
	#If someone runs out of guesses without winning right now, the game just exits.
	elif (counter > 4):
		print("You're out of guesses.  Game Over")
		#winner end program use break or quit()
		quit()
	elif (guess_row >= 5 or guess_row < 0) or (guess_col >= 5 or guess_col < 0):
		print("Oops, that's not even in the ocean.")
	#the player guesses a location that was already guessed
	elif (board[guess_row][guess_col] == "X"):
		print("You guessed that one already.")
	else:
		print("You missed my battleship!")
		board[guess_row][guess_col] = "X"
		print_board(board)

# Extra Credit

# You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements—maybe you can think of some more!

# Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

# Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

# Make your game a two-player game.

# Use functions to allow your game to have more features like rematches, statistics and more!

# Some of these options will be easier after we cover loops in the next lesson. Think about coming back to Battleship! after a few more lessons and see what other changes you can make!
