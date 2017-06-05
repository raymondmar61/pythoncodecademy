#In terms of lists and dictionaries, for loops allow us to iterate through all of the elements in a list from the left-most (or zeroth element) to the right-most element. 
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for x in names:
    print(x)

webster = {"Aardvark" : "A star of a popular children's cartoon show.","Baa" : "The sound a goat makes.","Carpet": "Goes on the floor.","Dab": "A small mount."}
for x in webster:
	print(webster[x]) #x is each dictionary key.  Print the key's values.

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for x in a:
	if x % 2 == 0:
		print(x)
	else:
		print(x, "is an odd number.")

#Functions can also take lists as inputs and perform various operations on those lists.
def fizz_count(word):
	count = 0
	for x in word:
		if x == 'fizz':
			count += 1
	return count	
lists = ['fizz', 'wizz', 'jizz', "fizz"]
print(fizz_count(lists))
print("\n")

for letter in "Codecademy":
    print(letter)

word = "Programming is fun!"
for letter in word:
	if letter == "i":
		print(letter)

prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
inventory = {"banana":6, "apple": 0, "orange": 32, "pear": 15}
totalvalue = 0 #initialize total for for loop
for x in prices:
	print(x) #prints the keys banana, apple, orange, pear
	print(prices) #prints the entire list
	print(prices[x]) #prints the price for each key in prices
	print(inventory[x]) #prints the inventory for each key in inventory since the keys are the same
	totalvalue = totalvalue + (prices[x]) + (inventory[x])

print(totalvalue)
print("")

#using prices and inventory dictionaries for a different scenario
groceries = ['banana', 'orange', 'apple']
def compute_bill(food):
	total = 0
	for x in food:
		if inventory[x] > 0: #is inventory in stock
			total = total + prices[x] #add the price spent for groceries
			inventory[x] = inventory[x] - 1 #subtract the inventory by one
	print(total)

compute_bill(groceries)

