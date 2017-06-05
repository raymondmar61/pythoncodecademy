n = [1, 3, 5]
print(n[1])
#Overwrite the second element with result
n[1] = n[1] * 5
print(n)
n.append(4)
print(n)
#n.pop(index) will remove the item at index from the list and return it to you
n.pop(1)
print(n)
#n.remove(item) will remove the actual item if it finds it.  It doesn't remove the item at index.
n = [1, 3, 5, 4]
n.remove(5) #removes 5, not index 5
print(n)
#del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it
n = [1, 3, 5, 4]
del(n[1])
print(n)

number = 5
def my_function(x):
	return x * 3
print(my_function(number))

m = 5
n = 13
def add_function(x, y):
	return x + y
print(add_function(m, n))

h = "Hello"
def string_function(s):
	return (s + " world")
print(string_function(h))

#You pass a list to a function the same way you pass any other argument to a function
n = [3, 5, 7]
def list_function(x):
	return x
print(list_function(n))

def first_item(items):
    print(items[0])
    print(items[2])
numbers = [2, 7, 9]
first_item(numbers) #calling function first_item it printed both print statements

def list_function(x):
    #return x[1] = x[1] + 10 invalid syntax
    x[1] = x[1] + 10 #added 10 to n[1] which is x[1] in function
    return x[1] #must include variable in return statement of course
n = [3, 5, 7]
print(list_function(n))
print(n) #note n[1] is 5 + 10 = 15

#You can also append or delete items of a list inside a function just as if you were manipulating the list outside a function.
n = [3, 5, 7]
def list_extender(lst):
    lst.append(9)
    return lst
print(list_extender(n))

#Printing out a list item by item in a function; utilize every element in a list in a function.
n = [3, 5, 7]
def print_list(x):
	for i in range(0, len(x)):
		print(x[i])
print_list(n)

#Modifying each element in a list in a function.  It is useful to do so in a function as you can easily put in a list of any length and get the same functionality.
n = [3, 5, 7]
def double_list(x):
	for i in range(0, len(x)):
		#print(x[i] * 2) print statement takes each index multiple two returns index in its own line
		x[i] = x[i] * 2
	return x #return the list n as x, return x[i] returns 7 * 2 = 14, the last index
print(double_list(n))

#range() function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.   range() function returns a list of numbers from start up to (but not including) stop. Each item increases by step.  start defaults to zero and step defaults to one.
# range(6) # => [0,1,2,3,4,5] range(stop)
# range(1,6) # => [1,2,3,4,5] range(start, stop)
# range(1,6,3) # => [1,4] range(start, stop, step)
def my_function(x):
	for i in range(0, len(x)):
		x[i] = x[i] * 2
		print(x[i])
	return x #return the list x 
r = list(range(0,3)) #need list() to create a list with range() for python 3.5
print(my_function(r)) #range(0,3) generate list [0,1,2] to pass into function my_function

#Iterating over a list in a function.  Uses indexes to loop through the list, making it possible to also modify the list if needed. 
n = [3, 5, 7]
def total(numbers):
	result = 0
	for i in range(0, len(numbers)):
		result = result + numbers[i]
	return result
print(total(n))

n = ["Michael", "Lieberman"]
def join_strings(words):
    result = ""
    for w in range(0, len(words)):
        result = result + words[w]
    return result
print(join_strings(n))

#Using two lists as two arguments in a function.  Using multiple lists in a function is no different from just using multiple arguments in a function!
# a = [1, 2, 3]
# b = [4, 5, 6]
# print a + b
# prints [1, 2, 3, 4, 5, 6]
m = [1, 2, 3]
n = [4, 5, 6]
def join_lists(x, y):
    print(x + y)
    return (x + y)
print(join_lists(m, n))