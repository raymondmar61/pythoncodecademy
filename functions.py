#Reuse a piece of code, just with a few different values. Instead of rewriting the whole code, it's much cleaner to define a function, which can then be used repeatedly.

def spam(): #<-- header "def" keyword, name of the function, and parameters
	print("Eggs!") #<-- body describes the procedures the function carries out
	pass

#call a function to implement
spam() #<-- look for a function called spam() and execute the code inside the function

def square(n, p): #n and p are parameters of square.  A parameter acts as a variable name for a passed in argument.
	squared = n ** p
	return squared

base = 20
power = 3
print(base, "raised to the power of" ,power, "is", square(base,power))

def cube(number):
	number = number ** 3
	return number

def by_three(number):
	if number % 3 == 0:
		return cube(number)
	else:
		return False

number3 = 9
cubethree = cube(number3)
print(cubethree)
check = by_three(number3)
print(check)

#A module is a file that contains definitions—including variables and functions—that you can use once it is imported.
import math
print(math.sqrt(25))
#However, we only really needed the sqrt function, and it can be frustrating to have to keep typing math.sqrt()
#It's possible to import only certain variables or functions from a given module. Pulling in just a single function from a module is called a function import, and it's done with the from keyword:  from *module name* import *function name*
from math import sqrt
print(sqrt(36))
#What if we still want all of the variables and functions in a module but don't want to have to constantly type math.
#Universal import can handle this for you. The syntax for this is: from *module name* import * <--one asterik.  e.g. from math import *
#Universal imports fill your program with a ton of variable and function names without the safety of those names still being associated with the module(s) they came from.
#if you import * from several modules at once, you won't be able to figure out which variable or function came from where.
#For these reasons, it's best to stick with either import module and type module.name or just import specific variables and functions from various modules as needed.

def biggest_number(*args):
    print(max(args))
    return max(args)
    
def smallest_number(*args):
    print(min(args))
    return min(args)

def distance_from_zero(arg):
    print(abs(arg)) #absolute value
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

#type() function returns the type of the data it receives as an argument
print(type(42.4))
print(type('string'))
print(type(50))

def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

print(shut_down("yes"))

def distance_from_zero(variable):
    if type(variable) == int or type(variable) == float:
        print(type(variable))
        return abs(variable)
    else:
        return "Nope"

print(distance_from_zero(-56))
print(distance_from_zero("string"))