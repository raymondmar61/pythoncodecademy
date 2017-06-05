#Lists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.
#A list can also be empty: empty_list = []

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]

if len(zoo_animals) > 3:
	print("The first animal at the zoo is the " +zoo_animals[0])
	print("The second animal at the zoo is the " +zoo_animals[1])
	print("The third animal at the zoo is the " +zoo_animals[2])
	print("The fourth animal at the zoo is the " +zoo_animals[3])
else:
	print("One animal is missing!")

numbers = [5, 6, 7, 8]

print("Adding the numbers at indices 0 and 2...", numbers[0] + numbers[2])
print("Adding the numbers at indices 1 and 3...", numbers[1] + numbers[3])
print("")

#A list index behaves like any other variable name! It can be used to access as well as assign values.
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
zoo_animals[2] = "hyena" #replace second index sloth with hyena
zoo_animals[3] = "shark" #replace third index tiger with shark
print(zoo_animals)

#A list doesn't have to have a fixed length. You can add items to the end of a list any time you like!
suitcase = []
suitcase.append("sunglasses")
print(suitcase)
suitcase.append("underwear")
suitcase.append("deodorant")
suitcase.append("soap")
print(suitcase)
list_length = len(suitcase)
print("There are %i items in the suitcase." %list_length)
#Sometimes we want part of the list.  We start at the index the left of the colon and continue up to the index the right of the colon minus one.
#suitcase.append("hat","passport","laptop","suit","shoes") append takes one value only
suitcase.append("hat")
suitcase.append("passport")
suitcase.append("laptop")
suitcase.append("suit")
suitcase.append("shoes")
print(suitcase)
selectitems = suitcase[2:5]
print("I want items two to four" ,selectitems)
print("\n")

#You can slice a string exactly like a list! In fact, you can think of strings as lists of characters: each character is a sequential item in the list, starting from index 0 or start at the index the left of the colon and continue up to the index the right of the colon minus one.
animals = "catdogfrog"
print("cat" ,animals[:3])
print("cat" ,animals[0:3])
print("dog" ,animals[3:6])
print("frog" ,animals[6:])
print("")

#Search for an item in a list.
moreanimals = ["aardvark", "badger","duck","emu","fennec fox"]
duck_index = moreanimals.index("duck")
print("Duck is located at index:" ,duck_index)
moreanimals.insert(1,"cobra") #insert cobra at index one or before badger
print(moreanimals)
print("\n")

#If you want to do something with every item in the list, you can use a for loop. 
#for variable in list_name:
#A variable name follows the for keyword; it will be assigned the value of each list item in turn.
#Then in list_name designates list_name as the list the loop will work on. The line ends with a colon (:) and the indented code that follows it will be executed once per item in the list.
my_list = [1,9,3,8,5,7]
for number in my_list:
	print(number * 2)

animals2 = ["cat","ant","bat"]
animals2.sort()
for animals in animals2:
	print(animals)

start_list = [5, 3, 1, 2, 4]
square_list = []
for x in start_list:
	x = x ** 2
	square_list.append(x)
	square_list.sort() #it appears .sort works even though they're numbers
print(square_list)
print("\n")

#A dictionary is similar to a list, but you access values by looking up a key instead of an index. A key can be any string or number. Dictionaries are enclosed in curly braces {}
dictionary = {"key1": "value1","key2": "value2","key3": "value3"}
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print(residents["Puffin"])

#Like Lists, Dictionaries are "mutable". This means they can be changed after they are created. One advantage of this is that we can add new key/value pairs to the dictionary.
menu = {}
menu["Chicken Alfredo"] = 14.50
menu["Hamburger"] = 10.00
menu["BBQ Chicken"] = 7.50
menu["Ham Sandwich"] = 6.25
print(menu)
print("There are " +str(len(menu))+ " items in the menu")

zoo_animals = { 'Unicorn' : 'Cotton Candy House', 'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House', 'Atlantic Puffin' : 'Arctic Exhibit', 'Rockhopper Penguin' : 'Arctic Exhibit'}
del zoo_animals['Unicorn']
del zoo_animals['Sloth']
zoo_animals["Rockhopper Penguin"] = "Dancin Floor"
print(zoo_animals)

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
print(backpack)

#a key has a value in the form of a list
my_dict = {"fish": ["c", "a", "r", "p"],"cash": -4483,"luck": "good"}
print(my_dict["fish"][0])

inventory = {'gold' : 500,'pouch' : ['flint', 'twine', 'gemstone'],'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}
#Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
#Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

print(inventory)
inventory["pocket"] = ["seashell","strange berry","lint"]
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] = 550
print(inventory)
