#1 Python Syntax
print("Welcome to Python!")
myvariable = 10
myinteger = 7
myfloat = 1.23
myboolean = True
myinteger = 3
"""
multi-line comment use triple quotation marks
rathter three double quotation marks
"""
countto = 72 + 23
print(countto) #print 95
print(10**2) #print 100
print(5%2) #print 1
print(countto + 100) #print 195
print(108/9) #print 12.0
print(108//9) #print 12
print("\n")

#2 Strings & Console Output
brian = "Hello life!"
print(brian) #print Hello life!
fifthletter = "monty"
print(fifthletter[4]) #print y
fifthletter4 = "monty"[4]
print(fifthletter4) #print y
parrot = "Norwegian Blue"
print(len(parrot)) #print 14
print(parrot.lower()) #print norwegian blue
print(parrot.upper()) #print NORWEGIAN BLUE
print(str(3.14)) #print 3.14.  str() method turns non-strings into strings.
#Methods that use dot notation only work with strings.
print("Spam " + "and " + "eggs.") #print Spam and eggs.
print("The value of pi is around " +str(3.14)+".") #The value of pi is around 3.14.
string1 = "Camelot"
string2 = "place"
print("Let's not go to %s.  'Tis a silly %s." % (string1, string2)) #Let's not go to Camelot.  'Tis a silly place.
print("\n")

#Date and Time
from datetime import datetime
print(datetime.now()) #print current datetime such as 2017-07-21 18:35:41.046993
print(datetime.now().year) #print 2017
print(datetime.now().month) #print 7
print(datetime.now().day) #print 21
now = datetime.now()
print(now) #print 2017-07-21 18:42:19.619062
print(now.year) #print 2017
print(now.month) #print 7
print(now.day) #print 21
print("%s/%s/%s" % (now.month, now.day, now.year)) #print 7/24/2017
print("%s:%s:%s" % (now.hour, now.minute, now.second)) #print 11:59:39
print("%s/%s/%s %s:%s:%s" % (now.month, now.day, now.year, now.hour, now.minute, now.second)) #print 7/24/2017 12:1:49
print("\n")

#3 Conditionals and Control Flow
def clinic():
	print("You've just entered the clinic!")
	print("Do you take the door on the left or the right?")
	answer = input("Type left or right and hit 'Enter'.")
	if answer == "left" or answer == "l":
		print("This is the Verbal Abuse Room, you heap of parrot droppings!")
	elif answer == "right" or answer == "r":
		print("Of course this is the Argument Room, I've told you that already!")
	else:
		print("You didn't pick left or right! Try again.")
		clinic()
#clinic() #comment out to skip the input while reviewing Python
booleanone = 3<5
print(booleanone) #print True
print(5<-1) #print False
print(9==9) #print True
booleanfour = 66>=1000
print(booleanfour) #print False
print(-996<=1000) #print True
def usingcontrolonce():
	if 800 > 700:
		return "Success 1"
def usingcontroltwo():
	if "Raymond" == "Raymond":
		return "Success 2"
print(usingcontrolonce()) #print Success 1
print(usingcontroltwo()) #print Success 2
def greaterlessequal5(answer):	
	if answer > 5:
		print(1)
	elif answer < 5:
		print(-1)
	else:
		print(0)
greaterlessequal5(4) #return -1
greaterlessequal5(5) #return 0
greaterlessequal5(6) #return 1
print("\n")

#PygLatin or Pig Latin
#Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." So "Python" becomes "ythonpay.
print('Welcome to the Pig Latin Translator!')
def pyglatin(word):
	if len(word) > 0 and word.isalpha() == True: #isalpha() returns False string contains non-letter characters.
		print(word)
		word = (word[1:]+word[0]+"ay").lower()
		#print(word[1:]+word[0]+"ay").lower() #error message
		print(word)
	else:
		print("You don't want to enter a word")
#word = input("Enter a word ") #comment out to skip the input while reviewing Python
#pyglatin(word)
print("\n")

#4 Functions
#Functions override add a space separating functions
def tax(bill):
	bill = bill * 1.08
	print("Bill and tax is %.2f" % bill)
def tip(bill):
	bill *= 0.15
	print("Tip is %.2f" % bill)
mealcost = 100
tax(mealcost) #return Bill and tax is 108.00
tip(mealcost) #return Tip is 15.00

def square(n):
	squared = n**2
	print("%d squared is %d" % (n, squared))
square(10) #return 10 squared is 100

def power(base, expontent):
	result = base ** expontent
	return result
print(power(37, 4)) #print 1874161

#a function can call another function.  Must use return statement
def onegoodturn(n):
	return n + 1
def deservesanother(n):
	return onegoodturn(n) + 2
print(onegoodturn(10)) #return 11
print(deservesanother(10)) #return 13
def tax2(bill):
	return bill * 1.08
	print(bill)
def tip2(bill):
	return tax2(bill) + (bill*.15)
	#return (totalbill)
mealcost = 745
print(tax2(mealcost)) #return 804.6
print(tip2(mealcost)) #return 916.35

#Functions Modules module
import math
print(math.sqrt(25)) #print 5.0
print(math.fsum([4,5,6,7])) #print 22.0
print(dir(math))
#It's possible to import only certain variables or functions from a given module. Pulling in just a single function from a module is called a function import, and it's done with the from keyword.
from math import sqrt
print(sqrt(49)) #print 7.0
from math import *
print(fsum([4,5,6])) #print 15.0

def somenumberfunctions(*args):
	print(max(args))
	print(min(args))
somenumberfunctions(-10,5,5,10) #return 10\n -10
	
print(type(42.4)) #print <class 'float'>
number2 = 42.4
string2 = "okay okay"
integer2 = 50
print(type(string2)) #print <class 'str'>
print(type(integer2)) #print <class 'int'>
if type(number2) == float:
	print("yes float")
else:
	print("nothing")
if type(string2) == str:
	print("yes str string")
else:
	print("nothing")
if type(integer2) == int:
	print("yes int integer")
else:
	print("nothing")

def distaincefromzero(variable):
	if type(variable) == int or type(variable) == float:
		return abs(variable)
	else:
		return "Nope"
print(distaincefromzero(-55)) #print 55
print(distaincefromzero("parrot")) #print Nope

def hotelcost(nights):
	return 140 * nights
def planeridecost(city):
	if city == "Charlotte":
		return 183
	elif city == "Tampa":
		return 220
	elif city == "Pittsburgh":
		return 222
	elif city == "Los Angeles":
		return 478
def rentalcarcost(days):
	if days >= 7:
		cost = (40 * days) - 50
		return cost
	elif days >= 3:
		cost = (40 * days) - 20
		return cost
	else:
		cost = 40 * days
		return cost
def tripcost(city, days, spendingmoney):
	return (rentalcarcost(days) + planeridecost(city) + hotelcost(days-1) + spendingmoney) #notice hotelcost(days) instead of hotelcost(nights) and def tripcost(city, days) instead of def tripcost(city, days, nights)
print(tripcost("Los Angeles",5,1000)) #print 2218
print("\n")

#5 Lists and Dictionaries
zooanimals = ["pangolin", "cassowary", "sloth", "tiger"]
print(len(zooanimals)) #print 4
print(zooanimals[1]) #print cassowary
print("The fourth animal at the size is the " +zooanimals[3]) #print he fourth animal at the size is the tiger
numbers = [5, 6, 7, 8]
print(numbers[1] + numbers[3]) #print 14
zooanimals[3] = "shark"
print(zooanimals) #print ['pangolin', 'cassowary', 'sloth', 'shark']
zooanimals.append("lion")
print(zooanimals) #print ['pangolin', 'cassowary', 'sloth', 'shark', 'lion']
print(zooanimals[1:3]) #print ['cassowary', 'sloth'] We start counting indices from 0 and that we stopped before index 3
animals = "catdogfrog"
print(animals[0:3]) #print cat
print(animals[3:6]) #print dog
print(animals[6:]) #print frog
zooanimals = ["pangolin", "cassowary", "sloth", "tiger"]
print(zooanimals.index("cassowary")) #print 1
zooanimals.insert(1, "shark") 
#or
#zooanimals.insert(zooanimals.index("cassowary"), "shark")
print(zooanimals) #['pangolin', 'shark', 'cassowary', 'sloth', 'tiger']
print(zooanimals.index("cassowary")) #print 2
zooanimals.sort()
zooanimalssorted = []
for eachzooanimals in zooanimals:
	print(eachzooanimals, end = " ")
	zooanimalssorted.append(eachzooanimals) #it appears a for loop required to print a sorted list
print("\n")
print(zooanimalssorted) #print ['cassowary', 'pangolin', 'shark', 'sloth', 'tiger']
zooanimalssorted.remove("sloth")
print(zooanimalssorted) #print ['cassowary', 'pangolin', 'shark', 'tiger']
numbers = [5, 6, 7, 8]
for eachnumber in numbers:
	print(eachnumber * 2, end=" ")
print("\n")
residents = {"Puffin": 104, "Sloth": 105, "Burmese Python": 106}
print(residents) #print {'Sloth': 105, 'Puffin': 104, 'Burmese Python': 106}
print(residents["Puffin"]) #print 104
menu = {}
menu["Chicken Alfredo"] = 14.50
print(menu) #print {'Chicken Alfredo': 14.5}
menu['Hamburger'] = 10.00 #add key: item to menu dictionary
menu['BBQ Chicken'] = 7.50 #add key: item to menu dictionary
menu['Ham Sandwich'] = 6.25 #add key: item to menu dictionary
print(len(menu)) #print 4
print(menu) #print {'Ham Sandwich': 6.25, 'Chicken Alfredo': 14.5, 'BBQ Chicken': 7.5, 'Hamburger': 10.0}
del menu["Chicken Alfredo"]
print(menu) #print {'Ham Sandwich': 6.25, 'BBQ Chicken': 7.5, 'Hamburger': 10.0}
menu["Ham Sandwich"] = 20.00
print(menu) #print {'Ham Sandwich': 20.0, 'BBQ Chicken': 7.5, 'Hamburger': 10.0}
mydictionary = {"fish": ["c", "a", "r", "p"], "cash": -4483, "luck":"good"}
print(mydictionary["fish"]) #print ['c', 'a', 'r', 'p']
print(mydictionary["fish"][2]) #print r
mydictionary["inventory"] = ["rations","flashlight","sleeping bag"]
print(mydictionary) #print {'cash': -4483, 'fish': ['c', 'a', 'r', 'p'], 'luck': 'good', 'inventory': ['rations', 'flashlight', 'sleeping bag']}
mydictionary["fish"].sort() #sort key fish's list in dictionary mydictionary
print(mydictionary) #print {'luck': 'good', 'inventory': ['rations', 'flashlight', 'sleeping bag'], 'fish': ['a', 'c', 'p', 'r'], 'cash': -4483}
mydictionary["fish"].remove("p")
print(mydictionary) #print {'luck': 'good', 'inventory': ['rations', 'flashlight', 'sleeping bag'], 'fish': ['a', 'c', 'r'], 'cash': -4483}
mydictionary["cash"] = 1000
print(mydictionary) #print {'luck': 'good', 'inventory': ['rations', 'flashlight', 'sleeping bag'], 'fish': ['a', 'c', 'r'], 'cash': 1000}
for eachword in "abcxyz123":
	print(eachword, end="")
print("\n")
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.", "Baa" : "The sound a goat makes.", "Carpet": "Goes on the floor.", "Dab": "A small amount."}
for eachwebster in webster:
	print(eachwebster) #print webster's key
	print(webster[eachwebster]) #print webster's item
def countnumbers(numbers):
	total = 0
	for n in numbers:
		total = total + 1
	return total
listnumbers = [4, 8, 15, 16, 23, 42]
print(countnumbers(listnumbers)) #print 6
def fizzcount(x):
	count = 0
	for eachitem in x:
		if eachitem == 'fizz':
			count = count + 1
	return count
fizzlist = ['fizz', 'wizz', 'jizz', 'fizz']
print(fizzcount(fizzlist)) #print 2
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana":6, "apple": 0, "orange": 32, "pear": 15}
total = 0
for eachkey in prices:
	print(eachkey) #print prices' key
	print(eachkey+" price:", prices[eachkey]) #print prices' prices
	print(eachkey+" stock:", stock[eachkey]) #print prices' stock
	total = total + (prices[eachkey]*stock[eachkey])
	print("running total",total)
print("grand total",total)
groceries = ["banana","orange","apple"]
def computebill(food):
	total = 0
	for eachfood in food:
		if stock[eachfood] > 0:
			total = total + prices[eachfood]
			stock[eachfood] = stock[eachfood] - 1
	return total
print(computebill(groceries)) #print 7.5.  4 + 1.5 = 5.5.  Apple is excluded because its stock is 0.
print(stock) #orange minus one and banana minus one
print("\n")

#6 Student Becomes The Teacher "Challenge Course"
lloyd = {"name": "Lloyd", "homework":[0.0, 97.0, 75.0, 92.0], "quizzes":[88.0, 40.0, 94.0], "tests":[75.0, 90.0]}
alice = {"name": "Alice", "homework":[100.0, 92.0, 98.0, 100.0], "quizzes":[82.0, 83.0, 91.0], "tests":[89.0, 97.0]}
tyler = {"name": "Tyler", "homework":[0.0, 87.0, 75.0, 22.0], "quizzes":[0.0, 75.0, 78.0], "tests":[100.0, 100.0]}
print(lloyd) #print {'name': 'Lloyd', 'homework': [0.0, 97.0, 75.0, 92.0], 'quizzes': [88.0, 40.0, 94.0], 'tests': [75.0, 90.0]}
students = [lloyd, alice, tyler]
print(students) #print [{'name': 'Lloyd', 'quizzes': [88.0, 40.0, 94.0], 'tests': [75.0, 90.0], 'homework': [0.0, 97.0, 75.0, 92.0]}, {'name': 'Alice', 'quizzes': [82.0, 83.0, 91.0], 'tests': [89.0, 97.0], 'homework': [100.0, 92.0, 98.0, 100.0]}, {'name': 'Tyler', 'quizzes': [0.0, 75.0, 78.0], 'tests': [100.0, 100.0], 'homework': [0.0, 87.0, 75.0, 22.0]}]
for eachstudents in students:
	print(eachstudents["name"])
	print(eachstudents["homework"])
	print(eachstudents["quizzes"])
	print(eachstudents["tests"])
def average(numbers):
	sumnumbers = sum(numbers)
	average = sumnumbers / len(numbers)
	return average
print(average(lloyd["homework"])) #print 66.0
def getaverage(student):
	averagescore = (average(student["homework"])*.10) + (average(student["quizzes"])*.30) + (average(student["tests"])*.60)
	return averagescore
def getlettergrade(score):
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"	
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else:
		return "F"
for eachstudents in students:
	print(eachstudents["name"]+ " average score is below")
	print(getaverage(eachstudents))
	print(getlettergrade(getaverage(eachstudents)))
def getclassaverage(students):
	results = []
	for eachstudents in students:
		results.append(getaverage(eachstudents)) #called function getaverage.  A function can call another function.  Must use return statement.
	return (average(results))
print(getclassaverage(students)) #print 83.11666666...
print(getlettergrade(getclassaverage(students))) #print B
print("\n")

#7 Lists and Functions
nlist = [1, 3, 5]
nlist[1] = nlist[1] * 5
print(nlist[1]) #print 15
print(nlist) #print[1, 15, 5]
nlist = [1, 3, 5]
nlist.pop(1) #remove the item at index number 1.  Returns the item.
print(nlist) #print [1, 5]
nlist = [1, 3, 5]
nlist.remove(5) #removes the item specified in paranthesis; in this case, removes the 5
print(nlist) #print [1, 3]
nlist = [1, 3, 5]
del(nlist[1]) #remove the item at index number 1.  It doesn't return it.  Like .pop()
print(nlist)
def firstitem(items):
	print(items[0])
firstitem([2, 7, 9]) #return 2

def listfunction(x):
	x[1] = x[1] + 3
	return x
print(listfunction([3, 5, 7])) #print [3, 8, 7]

def forloopslist(x):
	for i in range(0,len(x)):
		print(x[i])
	for i2 in range(0, len(x)):
		x[i2] = x[i2] * 2
		print(x)
	print(x)
forloopslist([3,5,7]) #return 3\n 5\n 7\n [6, 5, 7]\n [6, 10, 7]\n [6, 10, 14]\n [6, 10, 14]
#range(start, stop, step) range() returns a list of numbers from start up to (but not including) stop. Each item increases by step.
print(range(0,6)) #print range(0,6)
print(list(range(0,6))) #print [0, 1, 2, 3, 4, 5]
for eachnumber in range(0,6):
	print(eachnumber,end=" ") #print 0, 1, 2, 3, 4, 5
# def rangefunction(x):
# 	for i in range(0, len(x)):
# 		x[i] = x[i] * 2
# 	return x
# print(rangefunction(range(0,3))) Error message TypeError
def sumlistnumbers(numbers):
	result = 0
	print(numbers) #print [10, 11, 12, 13, 14, 15]
	for i in range(0, len(numbers)):
		result = result + numbers[i]
	return result
print(sumlistnumbers(list(range(10,16)))) #print 75
def sumliststrings(words):
	result = ""
	for w in range(0, len(words)):
		result = result + (words[w]+" ")
	return result
namelist = ["Michael","Liberman","III"]
print(sumliststrings(namelist)) #print Michael Liberman III
def joinedlists(x, y):
	print(x+y) #print [1, 2, 3, 4, 5, 6]
	return(x+y)
print(joinedlists([1,2,3],[4,5,6])) #print [1, 2, 3, 4, 5, 6]
longnumbers = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatnumbers(lists):
	results = []
	for eachlist in lists:
		for eachnumber in eachlist:
			results.append(eachnumber)
	return results
print(flatnumbers(longnumbers)) #print [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\n")

#Battleship
#In this project you will build a simplified, one-player version of the classic board game Battleship! In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. The player will have 10 guesses to try to sink the ship.
from random import randint
board = []
for i in range(0,5):
	board.append(["O"] * 5)
print(board) #print [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
# for eachboard in board:
# 	print(eachboard)
#--for loop above works to print each board on its separate line
def printboard(board):
	for eachboard in board:
		print(" ".join(eachboard))
printboard(board)
# letters = ["a","b","c","d","e"]
# print(letters) #print ['a', 'b', 'c', 'd', 'e']
# print(" ".join(letters)) #print a b c d e #The .join() method uses the string to combine the items in the list.
# print(letters) #print ['a', 'b', 'c', 'd', 'e']
# print("---".join(letters)) #print a---b---c---d---e
def randomrow(board):
	return(randint(0,len(board)-1))
def randomcolumn(board):
	return(randint(0,len(board)-1))
shiprow = randomrow(board)
shipcolumn = randomcolumn(board)
print(shiprow+1, shipcolumn+1)
# guessrow = int(input("Guess row: "))
# guesscolumn = int(input("Guess column: "))
# for turn in range(1,5):
# 	print("Turn", turn)
# 	guessbattleship = input("Guess row column separated by a space ")
# 	guessbattleship = guessbattleship.split(" ")
# 	guessrow = int(guessbattleship[0]) - 1
# 	guesscolumn = int(guessbattleship[1]) - 1
# 	if (guessrow == shiprow) and (guesscolumn == shipcolumn):
# 		print("Congratulations! You sank my battleship")
# 		board[shiprow][shipcolumn] = "!"
# 		printboard(board)
# 		break	
# 	else:
# 		if (guessrow < 0 or guessrow > 5) or (guesscolumn < 0 or guesscolumn > 5):
# 			print("Oops, that's not even in the ocean.")
# 			continue
# 		elif (board[guessrow][guesscolumn] == "X"):
# 			print("You guessed that one already")
# 			continue
# 		else:
# 			print("You missed my battleship!")
# 			board[guessrow][guesscolumn] = "X"
# 		printboard(board)
# 	if turn == 4:
# 		print("Game Over")
# 		board[shiprow][shipcolumn] = "!"
# 		printboard(board)
# 		break
print("\n")

#8 Loops
# choice = input("Enjoying the course? (y/n) ")
# while choice != "y" and choice != "n":
# 	choice = input("Sorry, I didn't catch that.  Enter (y/n): ")
count = 0
while True:
	print(count)
	count += 1
	if count >= 10:
		print(count,"break time exit loop.")
		break
#while/else.  The else block will execute anytime the loop condition is evaluated to False.  Python 2.7 only?  Works with Python 3.5.
from random import randint
print("Lucky numbers.  Three numbers generated.  If one of the three is a 5, you lose.")
count = 0
while count < 3:
	number = randint(1,5)
	print(number)
	if number == 5:
		print(number,"you lose")
		break
	count += 1
else:
	print("You win")
# computernumber = randint(1,10)
# print("Cheat",computernumber)
# guesses = 3
# while guesses > 0:
# 	print(guesses,"remaining")
# 	usernumber = int(input("Guess the number: "))
# 	if usernumber == computernumber:
# 		print(usernumber, "is correct")
# 		break
# 	print("Incorrect")
# 	guesses -= 1
# else:
# 	print("You lose")
#Create a for loop that prompts the user for a hobby 3 times.
# hobbies = []
# for eachinput in range(0,3):
# 	hobby = input("Enter a hobby ")
# 	hobbies.append(hobby)
# print(hobbies)
word = "Marble"
for eachword in word:
	if eachword == "a":
		print("X", end="")
	else:
		print(eachword, end="")
print("\n")
#Looping over a dictionary you get the key which you can use to get the value
dictionary = {"a": "apple", "b":"berry", "c":"cherry"}
for getkey in dictionary:
	print(getkey+" is the key for the value below")
	print(dictionary[getkey])
#enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.
choices = ["pizza","pasta","salad","nachos"]
print("Your choices are: ")
for index, eachchoices in enumerate(choices):
	print(index+1,eachchoices) #eachchoices should start at index 1.
#Iterate at least two lists at once. Use the zip function  zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
lista = [3, 9, 17, 15, 19]
listb = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for eachlista, eachlistb in zip(lista, listb):
	print(eachlista)
	print(eachlistb)
	print(eachlista, eachlistb)
#for loops may have an else associated with them.  the else statement is executed after the for if the for loop ends normally--not with a break.
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
for eachfruits in fruits:
	if eachfruits == "tomato":
		print(eachfruits+" is not a fruit.  It actually is a fruit")
		break
	else:
		print(eachfruits)
else:
	print("A fine selection of fruits!")
fruits = ['banana', 'apple', 'orange', 'pear', 'grape']
for eachfruits in fruits:
	if eachfruits == "tomato":
		print(eachfruits+" is not a fruit.  It actually is a fruit")
		break
	else:
		print(eachfruits)
else:
	print("A fine selection of fruits!")
print("\n")

#Practice Makes Perfect
#is even
def iseven(number):
	if number % 2 == 0:
		return True
	else:
		return False
print(iseven(100)) #print True
print(iseven(101)) #print False
#is int
#a number with a decimal part that is all 0s is also an integer, such as 7.0.
# def isint(number):
# 	if type(number) == int:
# 		return True
# 	elif str(number) == str(number)+".0":
# 		return True
# 	else:
# 		return False
from math import floor
def isint(number):
	number += 0.0
	numbery = floor(number)
	if number == numbery:
		return True	
	else:
		return False
print(isint(-1)) #return True
print(isint(5)) #return True
print(isint(5.0)) #return True
print(isint(5.9)) #return False
#digit sum
def digitsum(number):
	digitssum = 0
	for eachnumber in str(number):		
		digitssum = int(eachnumber) + digitssum
	print(digitssum)
digitsum(1234) #return 10
#factorial
def factorial(number):
	answer = 1
	for eachnumber in range(1,number+1):
		answer = eachnumber * answer
	print(answer)
factorial(4) #return 24
factorial(1) #return 11
factorial(3) #return 6
#is prime
#python program from william fiset primenumberprogram.py
def isprime(number):
	is_prime = True
	for factor in range(2, number):
		if number % factor == 0:
			is_prime = False
	if is_prime == True:
		print(number,"is a prime number!")
	else:
		print(number,"is not a prime number!")
isprime(5) #return 5 is a prime number!
isprime(21) #return 21 is not a prime number!
#reverse
#may not use reversed or [::-1]
def reverse(text):
	initialize = len(text)
	for eachinitialize in range(initialize-1,-1,-1):
		print(text[eachinitialize],end = "")
		initialize -= 1
reverse("super! dog POO") #returned OOP god !repus
print("\n")
#antivowel
def antivowel(text):
	newword = []
	vowels = ["A","E","I","O","U","a","e","i","o","u"]
	for eachtext in text:
		if eachtext not in vowels:
			newword.append(eachtext)
	print("".join(newword))	
antivowel("Hey You!") #return Hy Y!
#scrabble score
def scrabblescore(word):
	word = word.lower()
	points = 0
	score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
	for eachword in word:
		points = points + score[eachword]
	print(points)
scrabblescore("Helix") #return 15
scrabblescore("zztop") #return 25
#censor
def censor(text, word):	
	asterik = "*"*len(word)	
	newtextsplit = text.replace(word,asterik)
	print(newtextsplit)
censor("this hack is wack hack","hack") #return this **** is wack ****
#count
def count(sequence, item):
	tally = 0
	for eachsequence in sequence:
		if eachsequence == item:
			tally += 1
	return tally
print(count([1,2,1,1],1)) #print 3
print(count(["apple",2,"bear",1,"apple"],"apple")) #print 2
#purify
def purify(filterlist):
	for eachfilterlist in filterlist:
		if eachfilterlist % 2 != 0:
			filterlist.remove(eachfilterlist)
	print(filterlist)
purify([1,2,3,4,5,6,7,8,9,10]) #return [2, 4, 6, 8, 10]
#digit sum
def product(number):
	digitsproduct = 1
	for eachnumber in str(number):
		digitsproduct = int(eachnumber) * digitsproduct
	print(digitsproduct)
product(1234) #return 24 1*2*3*4
product(455) #return 100 4*5*5
def productlist(number):
	digitsproduct = 1
	for eachnumber in number:
		digitsproduct = eachnumber * digitsproduct
	print(digitsproduct)
productlist([1,2,3,4]) #return 24 1*2*3*4
productlist([4,5,5]) #return 100 4*5*5
#remove duplicates
def removeduplicates(duplicatelist):
	return set(duplicatelist)
print(removeduplicates([1,1,2,2])) #print {1,2}
print(list(removeduplicates([1,1,2,2]))) #print [1,2]
#median
import statistics
example_list = [4,6,2,6,7,8,2,5,6,78,4,6,7,2,2,2]
def median(medianlist):
	y = statistics.median(medianlist)
	print(y)
median(example_list) #return 5.5
median([1,1,2]) #return 1
median([7, 12, 3, 1, 6]) #return 6
median([7, 3, 1, 4]) #return 3.5

#9 Exam Statistics
import statistics
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def average(grades):
	print(statistics.mean(grades))
	floater = (statistics.mean(grades))
	print("%.2f" % floater)
average(grades) #return 80.42307692307692\n 80.42
def populationvariance(grades):
	#A large variance indicates that the data is spread out; a small variance indicates it is clustered closely around the mean.
	print(statistics.pvariance(grades))
	floater = (statistics.pvariance(grades))
	print("%.2f" % floater)
populationvariance(grades) #return 334.07100591715977\n 334.07
#If you have already calculated the mean of your data, you can pass it as the optional second argument mu to avoid recalculation
grades2 = [100, 100, 90, 100, 85, 90, 90, 85]
mu = statistics.mean(grades2)
print(mu) #print 92.5
print(statistics.pvariance(grades2, mu)) #print 37.5
print(statistics.pvariance(grades2)) #print 37.5
#Use variance() function when your data is a sample from a population. To calculate the variance from the entire population, see pvariance().  A large variance indicates that the data is spread out; a small variance indicates it is clustered closely around the mean.
gradessample = [100, 100, 90, 40]
grades2sample = [100, 100, 90, 100]
print(statistics.variance(gradessample)) #print 825.0
print(statistics.variance(grades2sample)) #print 25.0
#The standard deviation is the square root of the variance. You can calculate the square root by raising the number to the one-half power.
print(statistics.stdev(grades)) #print 19.02393903507516
print(statistics.stdev(grades2)) #print 6.546536707079771
print("\n")

#10 Advanced Topics in Python
ddictionary = {"Name":"Guido", "Age": 56, "BDFL": True}
print(ddictionary) #print {'Age': 56, 'Name': 'Guido', 'BDFL': True}
print(ddictionary.items()) #print dict_items([('BDFL', True), ('Age', 56), ('Name', 'Guido')]) #.items() returns an array of tuples with each tuple consisting of a key/value pair from the dictionary
print(ddictionary.keys()) #print dict_keys(['BDFL', 'Name', 'Age'])
print(ddictionary.values()) #dict_values([True, 'Guido', 56])
for key in ddictionary:
	print(key, ddictionary[key]) #print BDFL True\n Name Guido\n Age 56
for i in range(1,12):
	if i % 2 == 0:
		i = i ** 2
		print(i, end=" ") #print 4 16 36 64 100.  Even numbers squared
print("\n")
#List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:  [start(inclusive):end(exclusive):stride]
slicelist = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(slicelist[0:4]) #print [1, 4, 9, 16]
print(slicelist[2:9:2]) #print [9, 25, 49, 81]
print(slicelist[3:]) #print [16, 25, 36, 49, 64, 81, 100]
print(slicelist[:2]) #print [1, 4]
print(slicelist[::2]) #print [1, 9, 25, 49, 81]
print(slicelist[::-1]) #print [100, 81, 64, 49, 36, 25, 16, 9, 4, 1]
toonehundred = list(range(1,101))
print(toonehundred[9::10]) #print [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(toonehundred[::-10]) #print [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
to21 = list(range(1,22))
print(to21[::2]) #print [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21].  Print odds.
print(to21[7:14]) #print [8, 9, 10, 11, 12, 13, 14] print middle thirds 8 to 14 inclusive
#the function the lambda creates is an anonymous function.  The lambda and the function bythree immediately below are the same.
#lambda x: x % 3 == 0
#def bythree(x):
#	return x % 3 == 0
mylist = range(1,16)
answer = lambda x: x % 3 == 0, mylist
print(answer) #(<function <lambda> at 0x7fbfd3b5e400>, range(1, 16))
#RM:  I still don't understand lambda
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
for key in movies:
	print(key, movies[key]) #print Monty Python and the Holy Grail Great\n Monty Python's Life of Brian Good\n Monty Python's Meaning of Life Okay
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
print(garbled[len(garbled):0:-2]) #print e secret message
print("\n")

#Skipped Introduction to Bitwise Operators

#11 Introduction To Classes
class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous
  def description(self):
    print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))
  def is_edible(self):
    if not self.poisonous:
      print("Yep! I'm edible.")
    else:
      print("Don't eat me! I am super poisonous.")
lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description() #print I'm a yellow lemon and I taste sour.
lemon.is_edible() #print Yep! I'm edible.

class Animal():
	isalive = True
	addlovescale = 5
	health = "good"
	def __init__(self, name, age, ishungry):
		self.name = name
		self.age = age
		self.ishungry = ishungry
		#self.isalive = isalive #excluded for class scope variables or member variables
		#self.addlovescale = addlovescale #excluded for class scope variables or member variables
	#When a class has its own functions, those functions are called methods.  __init__ is a method
	def description(self):
		print(self.name+" is age",self.age)
zebra = Animal("Jeffrey",2,True)
print(zebra.name) #print Jeffrey
giraffe = Animal("Bruce",1,False)
print(giraffe.age) #print 1
panda = Animal("Chad",7,True)
print(panda.ishungry) #print True
print(panda.isalive) #print True
print(zebra.addlovescale) #print 5
zebra.description() #return Jeffrey is age 2
hippo = Animal("Rebecca",3,False)
hippo.description() #return Rebecca is age 3
sloth = Animal("Sean",50,True)
ocelot = Animal("Otto",19,False)
print(sloth.health) #print good
print(ocelot.health) #print good

class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name
  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print(product + " added.")
    else:
      print(product + " is already in the cart.")
  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print(product + " removed.")
    else:
      print(product + " is not in the cart.")
mycart = ShoppingCart("Rocky")
mycart.add_item("broccoli",.50) #return broccoli added
mycart = ShoppingCart("Pop")
mycart.add_item("coffee",10.20) #return coffee added
print(ShoppingCart.items_in_cart) #print {'broccoli': 0.5, 'coffee': 10.2}

class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id
  def display_cart(self):
    print("I'm a string that stands in for the contents of your shopping cart!")
class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print("I'm a string that stands in for your order history!")
monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart() #return I'm a string that stands in for the contents of your shopping cart!
monty_python.display_order_history() #return I'm a string that stands in for your order history
#Inheritance works the following below:
#class DerivedClass(BaseClass):
#   code goes here
#DerivedClass is the new class you're making and BaseClass is the class for which DerivedClass inherits
class Shape(object):
	def __init__(self, number_of_sides):
		self.number_of_sides = number_of_sides
class Triangle(Shape):
	def __init__(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

class Employee(object):
	def __init__(self, name):
		self.name = name
	def greet(self, other):
		print("Hello, %s" % other.name)
class CEO(Employee):
	def greet(self, other):
		print("Get back to work, %s!" % other.name)
ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo) #return Hello, Emily
ceo.greet(emp) #return Get back to work, Steve!

class Employee2(object):
	def __init__(self, employee_name):
		self.employee_name = employee_name
	def calculate_wage(self, hours):
		self.hours = hours
		return hours * 20.00
class PartTimeEmployee(Employee2):
	def calculate_wage(self, hours):
		self.hours = hours
		return hours * 12.00
	def fulltimewage(self, hours):
		return super(PartTimeEmployee, self).calculate_wage(hours) #.calculated_wage is used at the Base Class Employee2 to calculate the full time wage in fulltimewage method
matt = Employee2("matt")
print(matt.calculate_wage(30)) #print 600.0 30*20.00
matt = PartTimeEmployee("matt")
print(matt.calculate_wage(30)) #print 360.00 30*12.00.  PartTimeEmployee("matt") needs BaseClass Employee2 to utilize matt
#Working with a derived class (or subclass) and realize that you've overwritten a method or attribute defined in that class' base class (also called a parent or superclass) that you actually need.  Access the attributes or methods of a superclass with Python's built-in super call.
milton = PartTimeEmployee("milton")
print(milton.fulltimewage(10)) #print 200.0 10*20.00

class Triangle():
	numberofsides = 3
	def __init__(self, angle1, angle2, angle3):
		self.angle1 = angle1
		self.angle2 = angle2
		self.angle3 = angle3
	def checkangles(self):
		if self.angle1 + self.angle2 + self.angle3 == 180:
			return True
		else:
			return False
class Equilateral(Triangle):	
	def isequilateral(self, angle1, angle2, angle3):
		self.angle1 = angle1
		self.angle2 = angle2
		self.angle3 = angle3
		if angle1 == 60 and angle2 == 60 and angle3 == 60:
			print("Equilateral Triangle")
		else:
			print("Not Equilateral Triangle")
alpha = Triangle(10,10,10)
print(alpha.numberofsides) #print 3
print(alpha.checkangles()) #print False
beta = Triangle(100,45,35)
print(beta.checkangles()) #print True
beta = Equilateral(100,45,35)
beta.isequilateral(100,45,35) #print not Equilaterial Triangle
charlie = Equilateral(45,45,90)
charlie.isequilateral(45,45,90) #print not Equilaterial Triangle
delta = Equilateral(60,60,60)
delta.isequilateral(60,60,60) #print Equilaterial Triangle
#it seems Equilateral(Triangle) the Triangle in (Triangle) no need to include __init__ in Equilateral(Triangle) because Equilateral(Triangle) is using Triangle()'s __init__

#Classes
class Car():
	initialcondition = "new" #condition is a member variable
	def __init__(self, model, color, mpg):
		self.model = model
		self.color = color
		self.mpg = mpg
	def drivecar(self):
		self.condition = "used"
		return self.condition
	def displaycar(self): #displaycar is like a function.  It's a method in a class.
		print("This is a "+self.color+" "+self.model+" with",self.mpg,"MPG.")
#We define a "child" class that inherits all of the variables and functions from its "parent".  Parent is Car().  Child is ElectricCar().
class ElectricCar(Car):
	def __init__(self, model, color, mpg, batterytype):
		self.model = model
		self.color = color
		self.mpg = mpg
		self.batterytype = batterytype
	def driveelectriccar(self):
		self.condition = "like new"
		return self.condition
mycar = Car("DeLorean","silver",88) #mycar is the new object which is an instance of Car()
print(mycar.initialcondition) #print new
mycar.displaycar() #return This is a silver DeLorean with 88 MPG.
print(mycar.drivecar()) #print used
myelectriccar = ElectricCar("Toyota","white",150,"molten salt")
myelectriccar.displaycar() #return This is a white Toyota with 150 MPG.
print(myelectriccar.driveelectriccar()) #print like new

#__repr__() short for representation.  By providing a return value in this method, we can tell Python how to represent an object of our class.
class point3d():
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def __repr__(self):
		return "(%d, %d, %d)" % (self.x, self.y, self.z)
mypoint = point3d(1,2,3)
print(mypoint) #print (1, 2, 3)

#12 File Input/Output
my_list = [i ** 2 for i in range(1, 11)] #Generates a list of squares of the numbers 1-10
f = open("output.txt", "w")
for item in my_list:
  f.write(str(item) + "\n")
f.close()

myfile = open("output.txt","r+") #opens the file in read-write-mode and prepares Python to send data into the file output.txt.
myfile.write("Data to be written") #The .write() method takes a string argument.
myfile.close() #You must close the file. You do this simply by calling my_file.close(). If you don't close your file, Python won't write to it properly.
#During the I/O process, data is buffered: this means that it is held in a temporary location before being written to the file.  Python doesn't flush the buffer—that is, write data to the file—until it's sure you're done writing. One way to do this is to close the file. If you write to a file without closing, the data won't make it to the target file.
myfile = open("output.txt","r") #reopen output.txt because I closed output.txt at myfile.close().  I need to reopen to print myfile.
print(myfile.read()) #print Data to be written64\n 81\n 100
myfile.close()
myfile = open("output.txt","r")
print(myfile.readline()) #print Data to be written64.  readline() reads from a file line by line, rather than pulling the entire file in at once.  Subsequent calls to .readline() will return successive lines.  The next .readline() prints the second line which is 81.
print(myfile.readline()) #print 81
myfile.close()

#File objects contain a special pair of built-in methods: __enter__() and __exit__(). The details aren't important, but what is important is that when a file object's __exit__() method is invoked, it automatically closes the file. How do we invoke this method? With with and as.  We don't explicitly close() our file.
with open("output.txt","r") as readoutput:
	readline = readoutput.readline()
print(readline) #print Data to be written64
with open("output.txt","r") as readoutput:
	readlines = readoutput.readlines()
print(readlines) #print ['Data to be written64\n', '81\n', '100\n']
with open("output.txt","r") as readoutput:
	read = readoutput.read()
print(read) #print Data to be written64\n 81\n 100
with open("output.txt","w") as writeoutput:
	write = writeoutput.write("Overide output.txt")
with open("output.txt","r") as readoutput:
	read = readoutput.read()
print(read) #print Overide output.txt
#Test whether a file we've opened is closed
#Python file objects have a closed attribute which is True when the file is closed and False otherwise.
print(writeoutput.closed) #print True
with open("output.txt","r") as readoutput:
	read = readoutput.read()
	print(readoutput.closed) #print False
print(read) #print Overide output.txt
print(readoutput.closed) #print True