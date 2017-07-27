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
#start 7 Lists and Functions