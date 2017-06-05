#If statement: it executes the code inside of it if some condition is true. #While loop will continue to execute as long as the condition is true. In other words, instead of executing if something is true, it executes while that thing is true.

count = 0
if count < 5:
	print("Hello I am an if statement and the count is" ,count)

while count < 10:
	print("Hello I am a while loop and the count is" ,count)
	count += 1

#The condition is the expression that decides whether the loop is going to be executed or not. There are 5 steps to this program:
#1. The loop_condition variable is set to True
#2. The while loop checks to see if loop_condition is True. It is, so the loop is entered.
#3. The print statement is executed.
#4. The variable loop_condition is set to False.
#5. The while loop again checks to see if loop_condition is True. It is not, so the loop is not executed a second time.

loop_condition = True
while loop_condition is True:
    print("I am a loop")
    loop_condition = False

#Create a while loop that prints out all the numbers from 1 to 10 squared (1, 4, 9, 16, ... , 100), each on their own line.
num = 1
while num <= 10: #better <= 10 instead of < 11
	print(num ** 2)
	num += 1

#A common application of a while loop is to check user input to see if it is valid. For example, if you ask the user to enter y or n and they instead enter 7, then you should re-prompt them for input.
choice = input("Enjoying the course? (y/n)")
while ((choice != "y") and (choice != "n")): #must be "and" not "or"
	choice = input("Sorry, I dind't catch that.  Enter again (y/n):")

#The break is a one-line statement that means "exit the current loop." An alternate way to make our counting loop exit and stop executing is with the break statement.
#The example below this loop is guaranteed to run at least once using an if statement with break statement.
count = 0
while True:
    print(count)
    count += 1
    if count >= 10:
        break

#while/else is similar to if/else, but there is a difference: the else block will execute anytime the loop condition is evaluated to False. This means that it will execute if the loop is never entered or if the loop exits normally. If the loop exits as the result of a break, the else will not be executed.
from random import randint
print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")
count = 0
while count < 3: #count is 0, 1, 2.  while loop maximum three times.
    num = randint(1, 5) #random number 1-5; didn't need random.randint(1,5) because of from random import randint
    print(num)
    if num == 5: #if num is 5, player loses and while loop ends
        print("Sorry, you lose!")
        break
    count += 1
else:
    print("You win!") #three numbers generated, none are a five, else block executed

#allow the user to guess what the number is three times.
random_number = randint(1,10) #generates number 1-10 inclusive
guesses_left = 3
while guesses_left > 0:
	guess = input("Your guess: ")
	if (int(guess)) == random_number:
		print("You win.  The number is",random_number)
		break
	guesses_left -= 1
else:
	print("You lose.  Number is", random_number)

#This kind of loop is useful when you want to do something a certain number of times, such as append something to the end of a list.
hobbies = []
for x in range(0,3):
	print(x+1)
	hobby = input("Enter a hobby: ")
	hobbies.append(hobby)
print(hobbies)

#Using a for loop, you can print out each individual character in a string.
thing = "spam!"
for c in thing:
	print(c, end = " ")
print("\n")
	#Similarily another print option
	# a = "one"
	# b = "two"
	# print(a, b, sep=",", end ="\n")

#String manipulation is useful in for loops if you want to modify some content in a string.
phrase = "A bird in the hand..."
for char in phrase:
    if (char == "A") or (char == "a"):
        print("X", end = "")
    else:
        print(char, end = "")
print("\n")        

#Perhaps the most useful (and most common) use of for loops is to go through a list.
#On each iteration, the variable num will be the next value in the list. So, the first time through, it will be 7, the second time it will be 9, then 12, 54, 99, and then the loop will exit when there are no more values in the list.
numbers  = [7, 9, 12, 54, 99]
for x in numbers:
	print(x, end = " ")
for x in numbers:
	print(x ** 2, end = " ")
print("\n")

#You may be wondering how looping over a dictionary would work. Would you get the key or the value?
#The short answer is: you get the key which you can use to get the value.
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
	print(key, "is the key for" ,d[key]) #e.g. b(key) is the key for berry(d[key])

#enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.
#We don't want the user to see things listed from index 0, since this looks unnatural. Instead, the items should appear to start at index 1. Modify the print statement to reflect this behavior by adding "+ 1.
choices = ['pizza', 'pasta', 'salad', 'nachos']
print('Your choices are:')
for index, item in enumerate(choices):
    print(index + 1, item)

#It's also common to need to iterate over two lists at once. This is where the built-in zip function comes in handy.
#zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
#zip can handle three or more lists as well!
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
    if a > b:
        print(a)
    else:
        print(b)
#list_b 40, 50, 60, 70, 80, 90 are excluded in for loop above     

#for loops may have an else associated with them.
#the else statement is executed after the for, but only if the for ends normally—that is, not with a break.
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
    if f == 'tomato':
        print ('A tomato is not a fruit!') #(It actually is.)
        break
    print ('A ' +f)
else:
    print('A fine selection of fruits!')

fruits = ['banana', 'apple', 'orange', 'pear', 'grape']
print('Correction without tomato.  You have...')
for f in fruits:
    if f == 'tomato':
        print ('A tomato is not a fruit!') #(It actually is.)
        break
    print ('A ' +f)
else:
    print('A fine selection of fruits!')    

#for statement executes else because for ends normally or no break
states = ["CA", "NV", "OR", "UT","WA"]    
for state in states:
	print("I visited " +state)
else:
	print("I didn't visit the states listed.")
