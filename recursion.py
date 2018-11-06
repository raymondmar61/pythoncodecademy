#https://www.codecademy.com/learn/learn-recursion-python

#Recursion: Conceptual Interactive Lesson
#Codecademy story.  Wait in line.  Don't know how many people in front.  Ask person in front how many are ahead.  Person in front asks person in front how many are ahead.  The second to the last person ask how many in front.  Person said nobody in front.  It's me.  One person.  The message is repeated down the line.
#Each person waiting for a reply:  receives the message, adds themselves to the count, responds to the person tapping them.  This chain eventually reaches you with the final number. Your plan was a success!
#You executed a recursive strategy. The "function" of asking a person involved asking a person. The self-referential logic can seem like it goes on forever, but each question brings you closer to the front of the line where no more people are asked about the line.  Break the problem into two possibilities:  (1) There's nobody left in line, don't ask or (2) there's someone in line, ask them.  We repeat Step 2 with a different input which brings us closer to Step 1.
#In programming, recursion means a function definition will include an invocation of the function within its own body. Here's a pseudo-code example:
'''
define function, speller
  if there are no more letters
    print "all done"
  print the first letter
  invoke speller with the given name minus the first letter
'''
def speller(name):
	#base case
	if not name:
		print(name+" is empty.  All done.")
	#recursive
	else:
		print(name)
		speller(name[1:])
speller("Zoe")
'''
Zoe
oe
e
 is empty
'''
#The recursive calls the function with arguments which bring us closer to the base case. In this example, we're reducing the length of the name by a single letter. Eventually, there will be a function call with no letters given as the argument.
def sumlist(numbers):
	#base case
	if not numbers:
		return 0
	#recursive
	else:
		print(numbers)
		print(sum(numbers))
		return sumlist(numbers[1:])
print(sumlist([5,6,7]))
'''
[5, 6, 7]
18
[6, 7]
13
[7]
7
0
'''
#When using iteration, we rely on a counting variable and a boolean condition. For example, when iterating through the values in a list, we would increment the counting variable until it exceeded the length of the dataset.
#Recursive functions have a similar concept, which we call the base case. The base case dictates whether the function will recurse, or call itself. Without a base case, it's the iterative equivalent to writing an infinite loop.
#Because we're using a call stack to track the function calls, your computer will throw an error due to a stack overflow if the base case is not sufficient.
#The recursive step moves us closer to the base case.  In comparsion, in an iterative function, this is handled by a loop construct that decrements or increments the counting variable which moves the counter closer to a boolean condition, terminating the loop.
#In a recursive function, the "counting variable" equivalent is the argument to the recursive call. If we're counting down to 0, for example, our base case would be the function call that receives 0 as an argument. We might design a recursive step that takes the argument passed in, decrements it by one, and calls the function again with the decremented argument. In this way, we would be moving towards 0 as our base case.

#Recursion: Conceptual Multiple Choice Quiz
'''
A function will not recurse if the __ is reached.  Base case.  The recursive step will bring us closer to the base case, where no recursion takes place.
What are the two main sections of a recursive function.  The base case and the recursive step.  The base case has no recursive call and the recursive step has a recursive call that moves closer to the base case.
Which of the following describes a recursive approach?  To compute a factorial number, multiply the number by the factorial number minus one.  This is recursive because we're describing the problem in terms of itself.
Recursion is typically more efficient than iteration.  False.  Recursion has additional overhead of function frames on the call stack.
What is the purpose of the base case in a recursive function?  In the base case, there is no recursive function call.  We can think of the base case like the terminating condition of an iterative loop.
What is the importance of the recursive step?  It recursively calls the function with an argument which will reach the base case.  The recursive step will be the equivalent of an infinite loop and cause a stack overflow if it doesn't move closer to a base case.
When analyzing the Big O runtime of recursive functions, we count the __.  Relation of input to function calls.
A recursive function which has no base case, or a recursive step that does not lead to the base case, will cause what?  A stack overflow.  Recursive calls will fill the call stack until there is no room left.
What is the call stack?  A data structure typically abstracted away from us which stores function calls in programs.  The call stack contains each recursive call with the function's execution context.
What is an execution context and how does it relate to recursion?  An execution context contains the variables within each recursive function call.
'''

#Recursion:  Python Interactive Lesson
#Let's replicate what's happening in the call stack with an iterative function. The call stack is abstracted away from us in Python, but we can recreate it to gain a better understanding of how recursive calls build up and resolve.
def sum_to_one(n):
  result = 1
  call_stack = []  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  return result, call_stack
sum_to_one(4)
'''
[{'n_value': 4}]
[{'n_value': 4}, {'n_value': 3}]
[{'n_value': 4}, {'n_value': 3}, {'n_value': 2}]
BASE CASE REACHED
'''
print("\n")
def sum_to_one(n):
  result = 1
  call_stack = []  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")  
  while len(call_stack) != 0:
    return_value = call_stack.pop()
    print("Return value of {0} adding to result {1}".format(return_value['n_value'], result))
    result += return_value['n_value']
  return result, call_stack
sum_to_one(4)
'''
[{'n_value': 4}]
[{'n_value': 4}, {'n_value': 3}]
[{'n_value': 4}, {'n_value': 3}, {'n_value': 2}]
BASE CASE REACHED
Return value of 2 adding to result 1
Return value of 3 adding to result 3
Return value of 4 adding to result 6
'''
#We want a function that takes an integer as an input and returns the sum of all numbers from the input down to 1.
def sum_to_one(n):
	result = 0
	for number in range(n, 0, -1):
		result = result + number
		print("Number",number,"Result",result)
	return(result)
sum_to_one(4)
'''
Number 4 Result 4
Number 3 Result 7
Number 2 Result 9
Number 1 Result 10
'''
def recursive_sum_to_one(n):	
	#base case
	if n == 1:
		return n
	else:
		print("Number",n)
		return n + recursive_sum_to_one(n-1)
print(recursive_sum_to_one(4))
'''
Number 4
Number 3
Number 2
10
'''
def factorial(n):
  if n<=1:
    return 1
  print("Number",n)
  return n * factorial(n-1)
print(factorial(4))
'''
Number 4
Number 3
Number 2
24
'''
def flatten(my_list):
  result = []
  for el in my_list:
    if isinstance(el, list):
      print("list found!")
      flat_list = flatten(el)
      result += flat_list
    else:
      result.append(el)
  return result
### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets)) #print ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
def fibonacci(n):
  # base cases
  if n == 1:
    return n
  if n == 0:
    return n  
  # recursive step
  print("Recursive call with {0} as input".format(n))
  return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(5)
'''
Recursive call with 5 as input
Recursive call with 4 as input
Recursive call with 3 as input
Recursive call with 2 as input
Recursive call with 2 as input
Recursive call with 3 as input
Recursive call with 2 as input
'''
def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"
  middle_index = len(my_list) // 2
  middle_value = my_list[middle_index]  
  print("Middle index: {0}".format(middle_index))
  print("Middle value: {0}".format(middle_value))  
  tree_node = {"data": middle_value}
  tree_node["left_child"] = build_bst(my_list[ : middle_index])
  tree_node["right_child"] = build_bst(my_list[middle_index + 1 : ])
  return tree_node  
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)
# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
#runtime = "???"
'''
Middle index: 2
Middle value: 14
Middle index: 1
Middle value: 13
Middle index: 0
Middle value: 12
Middle index: 1
Middle value: 16
Middle index: 0
Middle value: 15
{'data': 14, 'left_child': {'data': 13, 'left_child': {'data': 12, 'left_child': 'No Child', 'right_child': 'No Child'}, 'right_child': 'No Child'}, 'right_child': {'data': 16, 'left_child': {'data': 15, 'left_child': 'No Child', 'right_child': 'No Child'}, 'right_child': 'No Child'}}
'''