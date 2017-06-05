#2. is_even
#Remember how an even number is a number that is divisible by 2?
def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False

#3. is_int
#Define a function is_int that takes a number x as an input.
#Have it return True if the number is an integer (as defined above) and False otherwise.
def is_int(x):
    if x == int(x):
        return True
    else:
        return False

#4. digit_sum
#Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.  For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.
def digital_sum(n):
	sum = 0
	n = str(n) #convert numbers to a string
	nlist = []
	for eachchar in n:
		nlist.append(eachchar) #add string to a list each individual number
	print(nlist)
	for x in range(0,len(nlist)):
		sum = sum + (int(nlist[x]))
	return sum
print(digital_sum(1234))

#5. factorial
#To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example: 4 is 4 * 3 * 2 * 1 = 24; 3 is 3 * 2 * 1 = 6; rather 1 * 2 * 3 * 4 = 24; 1 * 2 * 3 = 6
def factorial(x):
	i = 1
	fact = x
	if x > 0:
		while i < x:
			fact = i * fact
			print(i, fact, x)
			i = i + 1
	return(fact)
print(factorial(4))

#6. is_prime
#A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
def is_prime(x):
    if x < 2:
        return (False)
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True    
print(is_prime(4))

#7. Reverse
#Define a function called reverse that takes a string textand returns that string in reverse.
#For example: reverse("abcd") should return "dcba".

#my solution
# def reverse(text):
# 	x = len(text) - 1
# 	while x >= 0:
# 		print(text[x], end = "")
# 		x = x - 1
# #inputtext = input("Enter text:")
# reverse("hello")

#best solution from codecademy forum
#The "i" adds the letter to the front of the new string, then moves to the next letter and puts it in front.
def reverse(text):
    rev=""
    for eachletter_ in text:
        rev = eachletter_ + rev
        print(rev)
    return rev
print(reverse("Python!"))

#8. anti_vowel
#Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

#my solution
# def anti_vowel(text):
# 	box = []
# 	for eachtext in text:
# 		box.append(eachtext)
# 		for eachletter in box:
# 			if eachletter == "a":
# 				box.remove("a")
# 			elif eachletter	== "e":
# 				box.remove("e")
# 			elif eachletter	== "i":
# 				box.remove("i")
# 			elif eachletter	== "o":
# 				box.remove("o")
# 			elif eachletter	== "u":
# 				box.remove("u")
# 			elif eachletter	== "A":
# 				box.remove("A")
# 			elif eachletter	== "E":
# 				box.remove("E")
# 			elif eachletter	== "I":
# 				box.remove("I")
# 			elif eachletter	== "O":
# 				box.remove("O")
# 			elif eachletter	== "U":
# 				box.remove("U")
# 	result = ""
# 	for w in range(0, len(box)):
# 		result = result + box[w]
# 	print(result)	
# anti_vowel("HEYYOU!")

#better solution
vowels="aeiou"
def anti_vowel(x):
    for eachstring in x:         
        for thevowel in vowels:
           if eachstring.lower() == thevowel:
               x = x.replace(eachstring,"")
    return x
print(anti_vowel("Hey look Words!"))

#9 scrabble_score
#Scrabble is a game where players get points by spelling words. Words are scored by adding together the point values of each individual letter (we'll leave out the double and triple letter and word scores for now).
#dictionary and its point values:  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,     "x": 8, "z": 10}
def scrabble_score(word):
	score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
	word = word.lower()
	myscore = 0
	for eachletter in word:
		myscore = myscore + int(score[eachletter])
	print(myscore)	
scrabble_score("Pie")

#10 censor
#Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.
def censor(text, word):
    length_of_word = len(word)
    word_now_censored = '*' * length_of_word
    wordlist = text.split()
    new_words_list = []
    print(new_words_list)
    for eachcompleteword in wordlist:
        if eachcompleteword == word:
            new_words_list.append(word_now_censored)
        else:
            new_words_list.append(eachcompleteword)
    print(new_words_list)
    return " ".join(new_words_list)

print(censor("this hack is wack hack","hack"))

#11 count
#practice with a few functions that take lists as arguments
def count(sequence, item):
    found = 0
    for i in sequnce:
        if i == item:
            found+=1
    return found

#12 purify
#Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.
#For example, purify([1,2,3]) should return [2].
def purify(numberslist):
	for eachnumber in numberslist:
		if eachnumber % 2 != 0:
			numberslist.remove(eachnumber)
	print(numberslist)
purify([1,2,3,4,5,6,7,8,9,10])

#another solution
#When you use remove() method, relevant index will shift and the script will skip it. Try using append() instead:
def purify(l):
    n = []
    for i in l:
        if i % 2 == 0:
        	n.append(i)
    return n
print(purify([1,2,3,4,5,6,7,8,9,10]))

#13 product
#Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list.
#For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100)
def product(integerslist):
	multiply = 1
	for eachinteger in integerslist:
		multiply = multiply * int(eachinteger)
		print(multiply)
	print(multiply)
product([4,5,5])

#another solution
def product(lst):
    total = 1
    for i in lst:
        total *= i
    return total
print(product([4,5,5]))

#14 remove_duplicates
#Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.
#For example: remove_duplicates([1,1,2,2]) should return [1,2].
def remove_duplicates(numbers):
    newlist = []
    for eachnumber in numbers:
       if eachnumber not in newlist: #can use if statement check individual element in list
           newlist.append(eachnumber)
    return newlist
print(remove_duplicates([1,1,2,2]))
#destructively modifying a list while you are looping through it is bad practice and will likely lead to bugs somewhere down the line! That's why we always make a fresh copy to work on.

#15 median
#The median is the middle number in a sorted sequence of numbers.
#Finding the median of [7,12,3,1,6] would first consist of sorting the sequence into [1,3,6,7,12] and then locating the middle value, which would be 6.
#If you are given a sequence with an even number of elements, you must average the two elements surrounding the middle; e.g., the median of the sequence [7,3,1,4] is 3.5, since the middle elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.

#I was way off during the start
# def median(listnumbers):
# 	if len(listnumbers) % 2 == 0:

# 	print(listnumbers)
# median([1,1,2])

def median(sequence):
	sequence = sorted(sequence)
	lengthsequence = len(sequence)
	if lengthsequence % 2 == 1: #odd
		position = lengthsequence // 2
		return sequence[position]
	else: #even
		position = lengthsequence / 2.0
		return (sequence[position] + sequence[position - 1.0]) / 2.0
print(median([7,3,1,4]))