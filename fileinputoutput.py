#what if you want to read information from a file on your computer and/or write that information to another file?
#This process is called file I/O (the "I/O" stands for "input/output"), and Python has a number of built-in functions that handle this for you.
#the sample file below created a file output.txt in present folder which is codecademy
#my_list generates a list of squares of the numbers 1 - 10 above
my_list = [i**2 for i in range(1,11)]
#open output.txt in "w" mode ("w" stands for "write"). We stored the result of this operation in a file object, f.  Prepares Python to send data into the file.
f = open("output.txt", "w")
for item in my_list:
	#write each element of that list to output.txt
    f.write(str(item) + "\n")
f.close()

my_list = [i**2 for i in range(1,11)]
print(my_list)
my_file = open("output.txt", "r+") #can't create a new file in r+, must be in w
for eachnumber in my_list:
	print(eachnumber)
	my_file.write(str(eachnumber) + "\n")
my_file.close()

#to read from our output.txt file, we do this with the read() function, like so: print my_file.read()
my_file = open("output.txt","r")
print(my_file.read())
my_file.close()

#write-only mode ("w"), read-only mode ("r"), read and write mode ("r+"), and append mode ("a", which adds any new data you write to the file to the end of the file)
#it appears to create a new file, open() must be in "w" mode.
#files must be closed after writing.  Call function my_file.close().  If you don't close your file, Python won't write to it properly.
#Reason:  During the I/O process, data is buffered: this means that it is held in a temporary location before being written to the file.  Python doesn't flush the buffer—that is, write data to the file—until it's sure you're done writing. One way to do this is to close the file. If you write to a file without closing, the data won't make it to the target file.

#What if we want to read from a file line by line, rather than pulling the entire file in at once. Python includes a readline() function that does exactly that.
my_file = open("textdontdelete.txt","r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()

#Check out our extremely bad code below. Part 1.
# # Open the file for reading
# read_file = open("text.txt", "r")
# # Use a second file handler to open the file for writing
# write_file = open("text.txt", "w")
# # Write to the file
# write_file.write("Not closing files is VERY BAD.")
# # Try to read from the file
# print(read_file.read()) #it didn't read any data back.
#Check out our extremely bad code below.  Part 2.
# Open the file for reading
read_file = open("text.txt", "r")
# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")
#Add a write_file.close()
write_file.close()
# Try to read from the file
print(read_file.read())
#Add a read file.close()
read_file.close()

#Is there a way to get Python to automatically close our files for us?  Yes.
#file objects contain a special pair of built-in methods: __enter__() and __exit__().
#when a file object's __exit__() method is invoked, it automatically closes the file. How do we invoke this method? With with and as:  with open("file", "mode") as variable: # Read or write to the file
with open("textsuccess.txt", "w") as textfile:
	textfile.write("Success!")
	textfile.close()
#Now you try: write any data you like to the text.txt file using with...as.
with open("trytext.txt","w") as jojo:
	jojo.write("I did it myself")
	jojo.close()
#Python file objects have a closed attribute which is True when the file is closed and False otherwise.
#By checking file_object.closed, we'll know whether our file is closed and can call close() on it if it's still open.
#f = open("bg.txt")
# f.closed
# # False
# f.close()
# f.closed
# # True
with open("textshorty.txt","w") as my_file:
	my_file.write("ok shorty")
print(open("textshorty.txt","r").readline()) #view textshorty.txt print statement
my_file = open("textshorty.txt","r")	
print(my_file.readline()) #view textshorty.txt print statement and variable
if my_file.closed == False: #note close and closED
	my_file.close() #note close and closED
print(my_file.closed) #note close and closED