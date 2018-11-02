#A lambda function is a way of defining a function in a single line of code. Usually, we would assign them to a variable.
#Lambda functions only work if we're just doing a one line command. If we wanted to something longer, we'd need a more complex function.
mylambda = lambda x: (x*2)+3
print(mylambda(5)) #print 13
stringlambda = lambda x: x.lower()
print(stringlambda("Oh Hi Mark!")) #print oh hi mark!
add_two = lambda my_input: my_input + 2
print(add_two(3)) #print 5
'''
The function is stored in a variable called add_two
lambda declares that this is a lambda function (if you are familiar with normal Python functions, this is similar to how we use def to declare a function)
my_input is what we call the input we are passing into add_two
We are returning my_input plus 2 (with normal Python functions, we use the keyword return)
'''
print(add_two(100)) #print 102 
print(add_two(-2)) #print 0
is_substring = lambda my_string: my_string in "This is the master string"
print(is_substring('I')) #print False
print(is_substring('am')) #print False
print(is_substring('the')) #print True
print(is_substring('master')) #print True
check_if_A_grade = lambda grade: "Got an A!" if grade >= 90 else "Did not get an A"
print(check_if_A_grade(91)) #print Got an A!
print(check_if_A_grade(70)) #print Did not get an A
print(check_if_A_grade(20)) #print Did not get an A
checkifABgrade = lambda grade: "Got an A!" if grade >=90 else "Got a B" if grade >=80 else "Did not get an A or B"
print(checkifABgrade(91)) #print Got an A!
print(checkifABgrade(84)) #print Got a B
print(checkifABgrade(20)) #print Did not get an A or B