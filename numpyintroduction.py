#https://www.codecademy.com/learn/intro-statistics-numpy

#Introduciton to Numpy Interactive Lesson
#We'll be constructing and manipulating single-variable datasets. One way to think of a single-variable dataset is that it contains answers to a question. For instance, we might ask 100 people, “How tall are you?” Their heights in inches would form our dataset.
#NumPy stands for Numerical Python.  NumPy works with many numbers at once, generates random numbers, and performs many different numerical functions (i.e., calculating sin, cos, tan, mean, median, etc.).
import numpy as np
#movie ratings.  Lorie, Marty, Tori, and Kurtz watch movies and give them ratings on a scale of 0 to 100
movie_ratings = np.array([63.0, 54.0, 70.0, 50.0])
#two dimension array.  Each row is a movie.  Three movies watched.
movie_ratings2dimension = np.array([[63.0, 54.0, 70.0, 50.0], [94.0, 85.0, 89.0, 95.0], [64.0, 90.0, 73.0, 85.0]])
#Some fans prefer to have the movies rated on a five star scale, so we can use NumPy to easily divide each element by 20.
movie_ratings_5stars = movie_ratings / 20
print(movie_ratings_5stars) #print [3.15 2.7  3.5  2.5 ]
#The ratings are always in the order (Lorie, Marty, Tori, Kurtz).  Create an array that only had Tori's ratings
#toriratings = movie_ratings[:, 2] #index starts at zero.
#print(toriratings) #IndexError: too many indices for array
#The ratings are always in the order (Lorie, Marty, Tori, Kurtz).  Create an array that only had Tori's ratings
toriratings = movie_ratings[2] #index starts at zero.
print(toriratings) #print 70.0
#The ratings are always in the order (Lorie, Marty, Tori, Kurtz).  Create an array that only had Tori's ratings
toriratings = movie_ratings2dimension[:, 2] #index starts at zero.
print(toriratings) #print [70. 89. 73.]
#select all of Marty's ratings that are over 80
martyratings = movie_ratings2dimension[:, 1]
print(martyratings) #print [54. 85. 90.]
martyratings80 = martyratings[martyratings>80]
print(martyratings80) #print [85. 90.]

#A NumPy array is a special type of list. It’s a data structure that organizes multiple items such as strings, numbers, or arrays.  Arrays give us special ways of performing mathematical operations that are both simpler to write and more efficient computationally.
#A NumPy array looks a lot like a Python list.
myarray = np.array([1, 2, 3, 4, 5, 6])
#We can transform a regular list into a NumPy array by using np.array() and saving the value to a new variable
mylist = [1, 2, 3, 4, 5, 6]
myarray = np.array(mylist)
print(type(myarray)) #print <class 'numpy.ndarray'>
test_1 = np.array([92, 94, 88, 91, 87])
#Transform CSV (comma-separated values) files into arrays using the np.genfromtxt() function
test_2 = np.genfromtxt('test_2.csv', delimiter=',')
print(test_2) #print [ 79. 100.  86.  93.  91.]
addlist = [1, 2, 3, 4, 5]
addlistplus3 = []
for eachaddlist in addlist:
	addlistplus3.append(eachaddlist+3)
print(addlistplus3) #print [4, 5, 6, 7, 8]
addlistnumpy = np.array(addlist) #convert list to an array
addlistnumpyplus3 = addlistnumpy+3 #add three for each item in array
print(addlistnumpyplus3) #print [4 5 6 7 8]
squarerootnumpy = np.array(addlist) #convert list to an array
squarerootnumpy = np.sqrt(squarerootnumpy) #calculate the square root for each item in array
print(squarerootnumpy) #[1.         1.41421356 1.73205081 2.         2.23606798]
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = (test_3)+2
print(test_3_fixed) #print [89 87 74 92 94]
test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
total_grade = (test_1+test_2+test_3)
print(total_grade) #print [258 279 246 274 270]
final_grade = total_grade/3
print(final_grade) #print [86.         93.         82.         91.33333333 90.        ]

#We could have also stored all of this data in a single, two-dimensional array.
test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
alltests = np.array([[92, 94, 88, 91, 87], [79, 100, 86, 93, 91], [87, 85, 72, 90, 92]]) #Each list represents a test.  Each item in list represents a student's score.
#Here are some examples that are not two-dimensional arrays.  This code will run but it will not create a two-dimensional array because the lists have different numbers of elements:  np.array([[29, 49,  6], [77,  1]]).
coin_toss = np.array([1,0,0,1,0])
coin_toss_again = np.array([[1,0,0,1,0], [0,0,1,1,1]])
a = np.array([5, 2, 7, 0, 11])
print(a[0]) #print 5
print(a[1]) #print 2
print(a[-1]) #print 11
print(a[-2]) #print 0
print(a[1:3]) #print [2 7]
print(a[:3]) #print [5 2 7]
print(a[-3:]) #print [ 7  0 11]
print(a[-1::-1]) #print [11  0  7  2  5]
print(a[-1:-3]) #print []
print(a[-1:-3:-1]) #print [11  0]
print(a[-1:-4:-1]) #print [11  0  7]
test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
jeremy_test_2 = test_2[3]
print(jeremy_test_2) #print 93
manual_adwoa_test_1 = test_1[1:3]
print(manual_adwoa_test_1) #print [94 88]
#Selecting elements from a 2-d array is very similar to selecting them from a 1-d array, we just have two indices to select from. The syntax for selecting from a 2-d array is a[row,column] where a is the array.
a = np.array([[32, 15, 6, 9, 14], [12, 10, 5, 23, 1], [2, 16, 13, 40, 37]])
print(a[2,1]) #print 16
print(a[:,0]) #print [32 12  2] #select a column
print(a[1,:]) #print [12 10  5 23  1] #select a row
print(a[0,0:3]) #print [32 15  6] #select first row, index 0, 1, and 2
student_scores = np.array([[92, 94, 88, 91, 87], [79, 100, 86, 93, 91], [87, 85, 72, 90, 92]]) #Each list represents a test.  Each item in list represents a student's score.
tanya_test_3 = student_scores[2,0:1]
print(tanya_test_3) #print [87]
cody_test_scores = student_scores[:,4]
print(cody_test_scores) #print [87 91 92]
#Perform element-wise logical operations. For instance, suppose we want to know how many elements in an array are greater than 5.  We can write code checks whether this statement evaluates to True without having to use a for loop.
a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
print(a>5) #print [ True False False False False False  True  True  True  True]
print(type(a>5)) #print <class 'numpy.ndarray'>
#We can then use logical operators to evaluate and select items based on certain criteria.
print(a[a>5]) #print [10  9  8  9  7]
print(type(a[a>5])) #print <class 'numpy.ndarray'>
#We can also combine logical statements.  We place each statement in parentheses and use boolean operators like & (and) and | (or).
print([(a> 5) | (a < 3)]) #[array([ True,  True,  True, False, False, False,  True,  True,  True, True])]
print(a[[(a> 5) | (a < 3)]]) #print [10  2  2  9  8  9  7]
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])
cold = porridge[porridge<60]
print(cold) #print [50 56 51]
hot = porridge[porridge>80]
print(hot) #print [90 85 98]
just_right = porridge[(porridge >=60) & (porridge <=80)]
print(just_right) #print [79 65 63 79]
'''
Arrays are a special type of list that allows us to store values in an organized manner.
An array can be created by either defining it directly using np.array() or by importing a CSV using np.genfromtxt('file.csv', delimiter=',').
An operation (such as addition) can be performed on every element in an array by simply performing it on the array itself.
Elements can be selected from arrays using their index and array locations, both of which start at 0.
Logical operations can be used to create new, more focused arrays out of larger arrays.
'''
temperatures = [[43.6,  45.1,  58.8,  53], [47, 44.5, 58.3, 52.6], [46.7, 44.2, 57.9, 52.2], [46.5, 44.1, 57.6, 51.9],[46.2, 43.9, 57.2, 51.5]]
temperatures = np.array(temperatures)
temperatures_fixed = temperatures + 3
print(temperatures_fixed)
'''
[[46.6 48.1 61.8 56. ]
 [50.  47.5 61.3 55.6]
 [49.7 47.2 60.9 55.2]
 [49.5 47.1 60.6 54.9]
 [49.2 46.9 60.2 54.5]]
'''
monday_temperatures = temperatures_fixed[0,:]
print(monday_temperatures) #print [46.6 48.1 61.8 56. ]
thursday_friday_morning = temperatures_fixed[3:5,1] #want fourth row and fifth row for Thursday and Friday column 2 for 6:00am 
print(thursday_friday_morning) #print [47.1 46.9]
thursday_friday_afternoon = temperatures_fixed[3:5,2:4] #want fourth row and fifth row for Thursday and Friday columns 3 and 4 for 12:00pm and 6:00pm
print(thursday_friday_afternoon) #print [[60.6 54.9] [60.2 54.5]]
temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]
print(temperature_extremes) #print [46.6 48.1 61.8 47.5 61.3 49.7 47.2 60.9 49.5 47.1 60.6 49.2 46.9 60.2]

#Introduciton to Numpy Multiple Choice Quiz
'''
Consider the array a = np.array([10, 4, 6, 9, 18, 22, 11, 13, 3, 2, 15]). Which logical operation could be performed on the array to return array([ 4, 18, 22, 3, 2])?  a[(a > 15) | (a < 5)]
In a two-dimensional array, how do the axes correspond to the interior arrays?  axis=0 are the values that share an index, axis=1 are the values that share an array.  axis=0 are the values that share an index (in the same column) and axis=1 are the values that share an array (in the same row).
How do you import Numpy?  import numpy as np
What's is the value of c in the following array operation?  a = np.array([1, 2, 3]) b = np.array([4, 5, 6]) c = a+b.  array([5, 7, 9])
What is the proper syntax for creating a 2-dimensional Numpy array with A and B in the first row and C and D in the second row?  np.array([['A', 'B'],['C','D']]).  This is a list of lists and would create a valid array.
'''

#Betty's Bakery Freeform Project
'''
All of Betty's recipes call for milk, eggs, sugar, flour, and butter. For example, her cupcake recipe calls for:
Flour	Sugar	Eggs	Milk	Butter
2 cups	0.75 cups	2 eggs	1 cups	0.5 cups
'''
cupcakes = ([2, .75, 2, 1, .5])
pancake = ([1, .125, 1, 1, .125])
cookie = ([2.75, 1.5, 1, 0, 1])
bread = ([4, .5, 2, 2, .5])
recipes = list([cupcakes]+[pancake]+[cookie]+[bread])
print(recipes) #print [[2, 0.75, 2, 1, 0.5], [1, 0.125, 1, 1, 0.125], [2.75, 1.5, 1, 0, 1], [4, 0.5, 2, 2, 0.5]]
recipes = np.array(recipes)
print(recipes) #print [[2.    0.75  2.    1.    0.5  ] [1.    0.125 1.    1.    0.125] [2.75  1.5   1.    0.    1.   ] [4.    0.5   2.    2.    0.5  ]]
print(recipes[:,2]) #print [2. 1. 1. 2.] print third column Eggs
print(recipes[:,2] == 1) #print [False  True  True False]
cupcakes = recipes[0,:]
print(cupcakes) #print [2.   0.75 2.   1.   0.5 ]
cookies = recipes[2,:]
print(cookies) #print [2.75 1.5  1.   0.   1.  ]
double_batch = cupcakes * 2
print(double_batch) #print [4.  1.5 4.  2.  1. ]
grocery_list = cookies + double_batch
print(grocery_list) #print [6.75 3.   5.   2.   2.  ]
