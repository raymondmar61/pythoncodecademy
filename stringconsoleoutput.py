brian = "Hello life!"
print(brian)
print("Hello who? " +brian)

caesar = "Graham"
praline = "John"
viking = "Teresa"
print(caesar)
print(praline)
print(viking)

#Use backshash \ for escaping characters
print("This isn\'t flying, this is falling with style!")

#Each character in a string is assigned a number called index
#index number starts with 0
fifth_letter = "monty"
print(fifth_letter)
fifth_letter = "monty"[4]
print(fifth_letter)

#len() gets the length, the number of characters of a string
parrot = "Norwegian Blue"
print(len(parrot))

#lower() method to get rid of all the capitalization in your strings
print(parrot.lower())
#upper() method captailze strings
print(parrot.upper())

#str() method turns non-strings into strings
pi = 3.14
print(str(pi))

#dot notation
print("Methods that use dot notation only work with strings; e.g. parrot.lower() and parrot.upper()")
print("On the other hand, len() and str() can work on other data types; e.g. len(parrot) and str(pi)")

#concatenate string
print(fifth_letter+ " is also " +parrot)

string_1 = "Camelot"
string_2 = "place"
print("Let's not go to %s.  \'Tis a silly %s." %(string_1, string_2))
print("Let's not go to " +string_1+ ".  \'Tis a silly " +string_2+ ".")

name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")
print("Ah, so your name is %s, your quest is %s, and your favorte color is %s." % (name, quest, color))

my_string = "Hello"
print(len(my_string))
print(my_string.upper())