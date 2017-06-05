#Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." So "Python" becomes "ythonpay."

s = "Charle"
print(s[0]) #prints "C"
print(s[1:4]) #prints "har"

print("Pyg Latin")

pyg = "ay"
original = input("Enter a word:")
if len(original) > 0 and original.isalpha() == True:
	word = original.lower()
	first = word[0]
	new_word = word[1:len(word)] + first + pyg
	print(new_word)
else:
	print("You didn't enter a word")