#Python Syntax
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

#Strings & Console Output
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

#Conditionals and Control Flow
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
#start Taking a Vacation