#Bitwise operations are operations that directly manipulate bits. In all computers, numbers are represented with bits, a series of zeros and ones.  This course will introduce you to the basic bitwise operations and then show you what you can do with them.
#To be honest, you aren't really going to see bitwise operators in your everyday program. However, they do pop up from time to time, and when they do, you should have a general idea of what is going on.
print(5 >> 4)  # Right Shift.  Returns 0
print(5 << 1)  # Left Shift.  Returns 10
print(8 & 5)   # Bitwise AND.  Returns 0
print(9 | 4)   # Bitwise OR.  Returns 13
print(12 ^ 42) # Bitwise XOR.  Returns 38
print(~88)     # Bitwise NOT.  Returns -89

#In binary we count in base two, where each place can hold one of two values: 0 or 1. 
#For example, the numbers one and zero are the same in base 10 and base 2. But in base 2, once you get to the number 2 you have to carry over the one, resulting in the representation "10". Adding one again results in "11" (3) and adding one again results in "100" (4).
print(0b1)  #1
print(0b10)  #2
print(0b11)  #3
print(0b100)  #4
print(0b101)  #5
print(0b110)  #6
print(0b111)  #7
print("******")
print(0b1 + 0b11)
print(0b11 * 0b11)

# one = 0b1
# two = 0b10
# three = 0b11
# four = 0b100
# five = 0b101
# six = 0b110
# seven = 0b111
# eight = 0b1000
# nine = 0b1001
# ten = 0b1010
# eleven = 0b1011
# twelve = 0b1100

#There are Python functions that can aid you with bitwise operations. In order to print a number in its binary representation, you can use the bin() function. bin() takes an integer as input and returns the binary representation of that integer in a string. (Keep in mind that after using the bin function, you can no longer operate on the value like a number.)
#You can also represent numbers in base 8 and base 16 using the oct() and hex() functions. (We won't be dealing with those here, however.)
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))

#The int function actually has an optional second parameter.  When given a string containing a number and the base that number is in, the function will return the value of that number converted to base ten.
print(int("1",2))
print(int("10",2))
print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
print(int("11001001",2))

#Stopped lesson