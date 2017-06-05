#In this lesson, wel'll cover some of the more complex aspects of Python, including iterating over data structures, list comprehensions, list slicing, and lambda expressions.

#a dictionary is just a collection of keys and values.
d = {"Name": "Guido","Age": 56,"BDFL": True}
print(d)
print(d.items()) #items() function returns an array of tuples with each tuple consisting of a key/value pair from the dictionary
print(d["Name"])

my_dict = {"Name": "Raymond Mar","Hobby": "board games", "Favorite Number": 40}
print(my_dict)
print(my_dict.items()) #items() function returns an array of tuples with each tuple consisting of a key/value pair from the dictionary
print(my_dict["Name"])

#The keys() function returns an array of the dictionary's keys
#The values() function returns an array of the dictionary's values
#these functions will not return the keys or values from the dictionary in any specific order.
#You can think of a tuple as an immutable (that is, unchangeable) list (though this is an oversimplification); tuples are surrounded by ()s and can contain any data type.
my_dict = {"Name": "Raymond Mar","Hobby": "board games", "Favorite Number": 40}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())

#For iterating over lists, tuples, dictionaries, and strings, Python also includes a special keyword: in
for number in range(5):
    print(number) #prints 0 1 2 3 4 in their own line
e = { "name": "Eric", "age": 26 }
for key in e:
    print(key, e[key]) #prints name Eric, another line, age 26
for letter in "Eric":
    print(letter) #prints E r i c in their own line
my_dict = {"Name": "Raymond Mar","Hobby": "board games", "Favorite Number": 40}
for eachkey in my_dict:
	print(eachkey, my_dict[eachkey])

#List comprehensions are a powerful way to generate lists using the for/in and if keywords we've learned.
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50) #prints list 0 to 50 even numbers

#new_list = [x for x in range(1,6)] # => [1, 2, 3, 4, 5]
#doubles = [x*2 for x in range(1,6)] # => [2, 4, 6, 8, 10]
#doubles_by_3 = [x*2 for x in range(1,6) if (x*2)%3 == 0] # => [6]
even_squares = [x**2 for x in range(1,12) if x % 2 == 0]
print(even_squares)

c = ['C' for x in range(5) if x < 3]
print(c) #prints three C in a list ['C', 'C','C']
#The comprehension should consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0]
print(cubes_by_four)

#List slicing allows us to access elements of a list in a concise manner. The syntax looks like this: [start:end:stride], where start describes where the slice starts (inclusive), end is where it ends (exclusive), and stride describes the space between items in the sliced list.
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(l[2:9:2]) #prints [9, 25, 49, 81]

#If you don't pass a particular index to the list slice, Python will pick a default.
to_five = ['A', 'B', 'C', 'D', 'E']
print(to_five[3:]) # prints ['D', 'E'] 
print(to_five[:2]) # prints ['A', 'B']
print(to_five[::2]) # print ['A', 'C', 'E']
#Use list slicing to print out every odd element of my_list from start to finish.
my_list = []
for eachnumber in range(1,11):
	my_list.append(eachnumber)
print(my_list)
print(my_list[::2])

#A positive stride progresses through the list from left to right.
#A negative stride progresses through the list from right to left.
letters = ['A', 'B', 'C', 'D', 'E']
print(letters[::-1])
#Create a variable called backwards and set it equal to the reversed version of my_list.
my_list = []
for eachnumber in range(1,11):
	my_list.append(eachnumber)
backwards = (my_list[::-1])
print(backwards)

#A stride length of 1 traverses the list "by ones," a stride length of 2 traverses the list "by twos," and so on.
#Create a variable, backwards_by_tens, and set it equal to the result of going backwards through to_one_hundred by tens. Go ahead and print backwards_by_tens to the console.
to_one_hundred = []
for eachnumber in range(1,101):
	to_one_hundred.append(eachnumber)
backwards_by_tens = (to_one_hundred[::-10])
print(backwards_by_tens)

#incorrect, appending a list to a list
# to_21 = []
# for eachnumber in range(1,22):
# 	to_21.append(eachnumber)
# print(to_21)
# to_21_odd = []
# to_21_odd.append(to_21[0:22:2])
# print(to_21_odd)
# to_21_odd_middle_third = []
# to_21_odd_middle_third.append(to_21[7:14])
# print(to_21_odd_middle_third)

#correct, no appending a list to a list. Use list slicing for this one instead of a list comprehension.
to_21 = []
for eachnumber in range(1,22):
	to_21.append(eachnumber)
print(to_21)
odds = to_21[::2]
middle_third = to_21[7:14]
print(odds)
print(middle_third)
#I was thinking too hard.  Read line 57 above to_five = ['A', 'B', 'C', 'D', 'E']

#functional programming allows to pass functions around just as if they were variables or values.
#see lambda
#lambda x: x % 3 == 0 is the same as: def by_three(x): return x % 3 == 0
#we don't need to actually give the function a name; it does its work and returns a value without one. That's why the function the lambda creates is an anonymous function
#When we pass the lambda to filter, filter uses the lambda to determine what to filter, and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.
my_list = []
for eachnumber in range(1,16):
	my_list.append(eachnumber)
print(my_list)
print(filter(lambda x: x % 3 == 0, my_list)) #supposed to print [0, 3, 6, 9, 12, 15]

#Lambdas are useful when you need a quick function to do some work for you.
#If you plan on creating a function you'll use over and over, you're better off using def and giving that function a name.
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(filter(lambda x: x == "Python", languages)) #supposed to print ["Python"]

# cubes = [x**3 for x in range(1, 11)]
# filter(lambda x: x % 3 == 0, cubes)
squares = []
for eachnumber in range(1,11):
	squares.append(eachnumber**2)
print(squares)
print(filter(lambda x: x > 30 and x < 70, squares)) #supposed to print [36, 49, 64]
#python2.7 solution below
# squares = [x**2 for x in range (1,11)]
# print filter(lambda x: x>30 and x< 70, squares)

movies = {"Monty Python and the Holy Grail": "Great","Monty Python's Life of Brian": "Good","Monty Python's Meaning of Life": "Okay"}
for eachmovie in movies:
	print(eachmovie,movies[eachmovie])
print(movies.items())

#squares = [x**2 for x in range(5)]
#Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.
threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
#message is backwards
print(garbled[::-1])
#message is backwards the letter we want is every other letter.
print(garbled[::-2])

# my_list = range(16)
# filter(lambda x: x % 3 == 0, my_list)
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
#Create a new variable called message.  Set it to the result of calling filter() with the appropriate lambda that will filter out the "X"s. The second argument will be garbled.
message = filter(lambda x: x != "X", garbled)
print(message) #supposed to print I am another secret message!