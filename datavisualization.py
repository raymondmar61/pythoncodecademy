#https://www.codecademy.com/learn/data-visualization-python

#Line Graphs In Matplotlib Interactive Lesson
#Matplotlib is a Python library used to create charts and graphs.
from matplotlib import pyplot as plt
x_values = [0 ,1, 2, 3, 4] #a list of x-values for each point on our line graph
y_values = [0, 1, 4, 9, 16] #a list of y-values for each point on our line graph
#plt.plot(x_values, y_values) #create the line graph 
plt.show() #display the graph  
#RM:  don't show the chart comment out .plot() instead of .show()
days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12, 10, 14, 22, 24]
money_spent_2 = [11, 14, 15, 15, 22, 21, 12]
# plt.plot(days, money_spent)
# plt.plot(days, money_spent_2)
plt.show()
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
# plt.plot(time, revenue)
plt.show()
# plt.plot(time, revenue)
# plt.plot(time, costs)
plt.show()
days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12, 10, 14, 22, 24]
money_spent_2 = [11, 14, 15, 15, 22, 21, 12]
# plt.plot(days, money_spent, color='green') #specific different line color
# plt.plot(days, money_spent_2, color='#AAAAAA') #specific different line color
plt.show()
x_values = [0 ,1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]
# plt.plot(x_values, y_values, linestyle='--') #dash line
# plt.plot(x_values, y_values, linestyle=':') #dotted line
# plt.plot(x_values, y_values, linestyle='') #no line
plt.show()
x_values = [0 ,1, 2, 3, 4]
# y_values = [0, 1, 4, 9, 16]
# plt.plot(x_values, y_values, marker='o') #circle marker
# plt.plot(x_values, y_values, marker='s') #square marker
# plt.plot(x_values, y_values, marker='*') #star marker
plt.show()
days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12, 10, 14, 22, 24]
money_spent_2 = [11, 14, 15, 15, 22, 21, 12]
#plt.plot(days, money_spent, color="green", linestyle="--") #dashed green
#plt.plot(days, money_spent_2, color="#ffa500", linestyle=":", marker="s") #orange dotted square
plt.show()
#To zoom, we can use plt.axis(). We use plt.axis() by feeding it a list as input. This list should contain: The minimum x-value displayed, The maximum x-value displayed, The minimum y-value displayed, The maximum y-value displayed
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
#plt.plot(x, y)
#plt.axis([0, 3, 2, 5]) #min x 0, max x 3, min y 2, max y 5
plt.show()
xyears = range(12) #yes start at zero
ycoffeespentperyear = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
# plt.plot(xyears, ycoffeespentperyear)
# plt.xlabel("Years")
# plt.ylabel("$")
# plt.title("Coffee Spent Per Year")
# plt.axis([0, 12, 2900, 3100]) #Include the 12th year which was excluded in xyears = range(12)
plt.show()
'''
#https://stackoverflow.com/questions/3777861/setting-y-axis-limit-in-matplotlib
axes = plt.gca() #Get Current Axes
axes.set_xlim([x1,x2])
axes.set_ylim([y1,y2])
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,70,95)) #set y-axis only leave x1 as x1 and x2 as x2
axes = plt.gca() #Get Current Axes
axes.set_xlim([0,len(unit_topics)*2])  #there are ten bars or five unit_topics with two numbers per topic
axes.set_ylim([70,90])
'''

#Subplots.  Display two lines side-by-side instead of the same set of x- and y-axes. Multiple axes or multiple charts in the same picture,  The picture or object that contains all of the subplots is called a figure.  We can have many different subplots in the same figure.  We can lay them out in many different ways. We can think of our layouts as having rows and columns of subplots.
#.subplot().  .subplot(number of rows, number of columns, index number)  .subplot() goes first, .plot() goes second, .show() goes last.
# Data sets
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
# #First Subplot
# plt.subplot(1, 2, 1)
# plt.plot(x, y, color='green')
# plt.title('First Subplot')
# #Second Subplot
# plt.subplot(1, 2, 2)
# plt.plot(x, y, color='steelblue')
# plt.title('Second Subplot')
# Display both subplots
plt.show()
x1 = [1, 2, 3, 4]
y1 = [10, 15, 20, 25]
x2 = [10, 20, 30, 40]
y2 = [200, 250, 400, 1500]
# First Subplot
# plt.subplot(1, 2, 1)
# plt.plot(x1, y1, color='green')
# plt.title('First Subplot')
# # Second Subplot
# plt.subplot(1, 2, 2)
# plt.plot(x2, y2, color='steelblue')
# plt.title('Second Subplot')
# Display both subplots
plt.show()
months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]
# plt.subplot(1,2,1)
# plt.plot(months, temperature)
# plt.subplot(1,2,2)
# plt.scatter(months, flights_to_hawaii) #scatterplot
plt.show()

#Spacing.
'''
We can customize the spacing the figure is visible and easy to understand. Use the plt.subplots_adjust() command. .subplots_adjust() has some keyword arguments that can move your plots within the figure:
left — the left-side margin, with a default of 0.125. You can increase this number to make room for a y-axis label.
right — the right-side margin, with a default of 0.9. You can increase this to make more room for the figure, or decrease it to make room for a legend.
bottom — the bottom margin, with a default of 0.1. You can increase this to make room for tick mark labels or an x-axis label.
top — the top margin, with a default of 0.9.
wspace — the horizontal space between adjacent subplots, with a default of 0.2.
hspace — the vertical space between adjacent subplots, with a default of 0.2.
e.g., adjust bottom margin add space.  plt.subplots_adjust(bottom=0.2)
e.g., plt.subplots_adjust(top=0.95, hspace=0.25)
'''
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
# #First Subplot
# plt.subplot(1, 2, 1)
# plt.plot(x, y, color='green')
# plt.title('First Subplot')
# #Second Subplot
# plt.subplot(1, 2, 2)
# plt.plot(x, y, color='steelblue')
# plt.title('Second Subplot')
# #Display both subplots
# plt.subplots_adjust(left=.2, right=1, wspace=1)
plt.show()
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]
# plt.subplot(2,2,1)
# plt.plot(x, straight_line)
# plt.subplot(2,2,3)
# plt.plot(x,parabola)
# plt.subplot(2,2,4)
# plt.plot(x,cubic)
# plt.subplots_adjust(wspace=.35, hspace=.35, bottom=.2)
plt.show()
#multiple lines on a single graph we can label them by using the command plt.legend().  The legend method takes a list with the labels to display.  List in order of .plot sequence.
'''
A keyword argument loc positions the legend.  These are the position values loc accepts:
0 best, 1 upper right, 2 upper left, 3 lower left, 4 lower right, 5 right, 6 center left, 7 center right, 8 lower center, 9 upper center, 10 center.  Default is 0 best.
'''
x = [1, 2, 3, 4, 5]
square = [1, 4, 9, 16, 25]
cube = [1, 8, 27, 64, 125]
# plt.plot(x, square)
# plt.plot(x, cube)
# plt.legend(["Squared Numbers","Cubed Numbers"], loc=10)
plt.show()
#or we can label the lines at the .plot() which creates a legend.  Still need .legend().
x = [1, 2, 3, 4, 5]
square = [1, 4, 9, 16, 25]
cube = [1, 8, 27, 64, 125]
# plt.plot(x, square, label="Squared Numbers")
# plt.plot(x, cube, label="Cubed Numbers")
# plt.legend(loc=9)
plt.show()

#Modify ticks or modify x labels modify y labels.  Modify x axis labels and y axis labels assign a variable to a subplot; e.g. ax = plt.subplot(1, 1, 1) or ax = plt.subplot() to modify the labels for one chart.  Or assign a variable to an object which is a chart.  Assign variable to a chart.  Assign variable to chart.
# ax = plt.subplot()
# plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], label="Squared Numbers")
# plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], label="Cubed Numbers")
# ax.set_xticks([1, 2, 4]) #x-axis show labels 1, 2, and 4 only
# ax.set_yticks(range(1,76)) #x-axis show labels each from 1 to 75
plt.show()
# x axis labels string and y axis labels string
# axstringlabels = plt.subplot()
# plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o') #another way for scatterplots include 'o'
# axstringlabels.set_xticks(range(0,6,2)) #set x-axis string
# axstringlabels.set_xticklabels(["0%","20%","40%"]) #label y-axis as string
# axstringlabels.set_yticks([0.1, 0.6, 0.8]) #set y-axis string
# axstringlabels.set_yticklabels(['10%', '60%', '80%']) #label y-axis as string
plt.show()
# RM:  Assign lists to variables to modify ticks or modify axis labels
# month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]
# months = range(12)
# conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]
# plt.xlabel("Months")
# plt.ylabel("Conversion")
# plt.plot(months, conversion)
# ax = plt.subplot()
# ax.set_xticks(months)
# ax.set_xticklabels(month_names)
# ax.set_yticks([0.10, 0.25, 0.5, 0.75])
# ax.set_yticklabels(["10%","25%","50%","75%"])
plt.show()

#In order to be sure that you don't have any stray lines, you can use the command plt.close('all') to clear all existing plots before you plot a new one.
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
# plt.plot(time, revenue)
plt.show()
plt.close("all")

#We can use the command plt.figure() to create new figures and size them how we want. We can add the keyword figsize=(width, height) to set the size of the figure, in inches. We use parentheses (( and )) to pass in the width and height, which are separated by a comma (,).  RM:  .figure() is before .plot()
#We can use the command plt.savefig() to save out to many different file formats, such as png, svg, or pdf. After plotting, we can call plt.savefig('name_of_graph.png').  RM:  file saved in folder where python file is run.
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
# plt.figure(figsize=(2,5))
# plt.plot(time, revenue)
# plt.savefig("tempchartdelete.jpg")
plt.show()
plt.close("all")

#Review.  Creating a line graph from data, Changing the appearance of the line, Zooming in on different parts of the axis, Putting labels on titles and axes, Creating a more complex figure layout, Adding legends to graphs, Changing tick labels and positions, Saving what you've made
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 8, 27, 64, 125]
# plt.plot(x,y1, color="pink", marker="o")
# plt.plot(x,y2, color="gray", marker="o")
# plt.xlabel("Amazing X-axis")
# plt.ylabel("Incredible Y-axis")
# plt.title("Two Lines on One Graph")
# plt.legend(["Squared","Cube"],loc=4)
plt.show()

#Line Graphs Concepts Multiple Choice Quiz
'''
What is the command to set the horizontal spacing of subplots within a figure to 0.35?  plt.subplots_adjust(wspace=0.35)
What is the command to add a legend to a plot with the labels ['Cats', 'Dogs']?  plt.legend(['Cats', 'Dogs'])
What is the command to set the color of a line to be 'green'?  plt.plot(x, y, color='green')
What are the inputs to the plt.plot function, in order?  x values (list of numbers), y values (list of numbers)
What is the command to plot a line graph in Matplotlib?  plt.plot
What is the command to label the x-axis with the label 'Time'?  plt.xlabel('Time')
What is the command to set the linestyle of a line to be dashed?  plt.plot(x, y, linestyle='--')
What is the command to save a figure to a file called 'it_figures.png'?  plt.savefig('it_figures.png')
What is the command to set a plot to display from x=-5 to x=5 and from y=0 to y=10?  plt.axis([-5, 5, 0, 10])
Which line of code will get the axes object of a plot and store it in a variable ax?  ax = plt.subplot()
What is the command to create a figure with 3 rows and 2 columns, and a subplot in the second row and the first column?  plt.subplot(3, 2, 3)
Which line of code will set the x-axis labels to be ["Monday", "Tuesday", "Wednesday"]?  ax.set_xticklabels(["Monday", "Tuesday", "Wednesday"])
What is the command to clear all existing plots?  plt.close('all')
Which line of code will create a figure with a height of 7 inches and a width of 6 inches?  plt.figure(figsize=(6, 7))
Which line of code will set the y-axis ticks to be at 0, 1, 2, 4, and 9?  ax.set_yticks([0, 1, 2, 4, 9])
'''

#Sublime Limes' Line Graphs Freeform Project
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthnumbers = range(1,13)
visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]
# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]
# plt.figure(figsize=(12, 8))
# ax1 = plt.subplot(1,2,1)
# plt.plot(monthnumbers, visits_per_month)
# plt.title("Monthly Website Visitors")
# plt.xlabel("Months")
# plt.ylabel("Number Of Visits")
# ax1.set_xticks(monthnumbers)
# ax1.set_xticklabels(months)
# ax1.set_yticks(range(7000,20000,1000))
# ax1.set_yticklabels(range(7000,20000,1000))
# ax2 = plt.subplot(1,2,2)
# plt.plot(monthnumbers, key_limes_per_month, color="green")
# plt.plot(monthnumbers, persian_limes_per_month, color="brown")
# plt.plot(monthnumbers, blood_limes_per_month, color="red")
# plt.title("Monthly Lime Sold")
# plt.xlabel("Months")
# plt.ylabel("Limes Sold")
# plt.legend(["Key","Persian","Blood"])
# ax2.set_xticks(monthnumbers)
# ax2.set_xticklabels(months)
# # ax2.set_yticks(range(10,200,20))
# # ax2.set_yticklabels(range(10,200,20))
# #RM:  No need to set yticks and yticklabels.  matplotlib automatically sets best y labels and y axis scale.
# plt.savefig("limeanalysis.jpg")
plt.show()
plt.close("all")

#Different Plot Types Interactive Lesson
from matplotlib import pyplot as plt
#RM:  bar plt.bar compare multiple categories of data such as building heights or distance of plants from earth, pie plt.pie display elements of a data set as proportions of a whole, histogram plt.hist  how many values in a dataset fall between different sets of numbers charts

#bar chart
heights = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
x_values = range(1,len(heights)+1)
# samplebar = plt.subplot()
# plt.bar(x_values, heights)
# samplebar.set_xticks(range(1,len(heights)+1))
# samplebar.set_xticklabels(x_values)
plt.show()
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
drinknumbers = range(0,len(drinks))
sales =  [91, 76, 56, 66, 52, 27]
# #plt.bar(drinks, sales) #RM  bar chart plotted drinks list alphabetically without drinkssubplot = plt.subplot()
# drinkssubplot = plt.subplot()
# plt.bar(drinknumbers, sales)
# drinkssubplot.set_xticks(drinknumbers)
# drinkssubplot.set_xticklabels(drinks)
plt.show()

#side by side bars or double bars or two bars
import numpy as np
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
drinknumbers = range(0,len(drinks)*2,2)
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
ind = np.arange(len(drinks))
width = 0.8
#sales1
n = 1 # This is our first dataset (out of 2)
t = 2 # Number of datasets 
d = 6 # Number of sets of bars 
w = 0.8 # Width of each bar 
store1_x = [t*element + w*n for element in range(d)]
#sales2
n = 2 # This is our first dataset (out of 2)
t = 2 # Number of datasets 
d = 6 # Number of sets of bars 
w = 0.8 # Width of each bar 
store2_x = [t*element + w*n for element in range(d)]
# drinkssubplot = plt.subplot()
# plt.bar(store1_x,sales1)
# plt.bar(store2_x,sales2)
# #drinkssubplot.set_xticks(drinknumbers)
# drinkssubplot.set_xticks(((ind+width)*2)-.42)
# #Source https://stackoverflow.com/questions/10369681/how-to-plot-bar-graphs-with-same-x-coordinates-side-by-side-dodged.  RM:  shift the x values by width.  I did some trial and error.
# drinkssubplot.set_xticklabels(drinks)
plt.show()

#Stacked Bars
days = ["Mon","Tue","Wed","Thr","Fri"]
daysnumbers = range(0,len(days))
video_game_hours = [1, 2, 2, 1, 2]
book_hours = [20, 30, 40, 20, 10]
# plt.bar(range(len(video_game_hours)), video_game_hours)
# plt.bar(range(len(book_hours)), book_hours, bottom=video_game_hours)
# plt.legend(["Video Games","Books"])
# ax = plt.subplot()
# ax.set_xticks(daysnumbers)
# ax.set_xticklabels(days)
plt.show()
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
# plt.bar(range(len(sales1)), sales1)
# plt.bar(range(len(sales2)), sales2, bottom=sales1)
plt.show()

#Error Bars and error shading
#Matplotlib reads this in the same order as the list of y-values. So, the first index of your error list should correspond to the first index of your y-values list, the second index of your error list should correspond to the second index of your y-values list, and so on.
values = [10, 13, 11, 15, 20]
yerr = 2 #consistent error bar for each bar
# plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()
values = [10, 13, 11, 15, 20]
yerr = [1, 3, 0.5, 2, 4] #each value has its own error bar
# plt.bar(range(len(values)), values, yerr=yerr, capsize=100) #capsize is the horizontal line length at the top and bottom or how wide
plt.show()
plt.close("all")
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
drinknumbers = range(0,len(drinks))
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]
# ax = plt.subplot()
# plt.bar(drinknumbers, ounces_of_milk, yerr=error, capsize = 10)
# ax.set_xticks(drinknumbers)
# ax.set_xticklabels(drinks)
plt.show()
x_values = range(10)
y_values = [10, 12, 13, 13, 15, 19, 20, 22, 23, 29]
y_lower = [8, 10, 11, 11, 13, 17, 18, 20, 21, 27]
y_upper = [12, 14, 15, 15, 17, 21, 22, 24, 25, 31]
# plt.fill_between(x_values, y_lower, y_upper, alpha=0.2) #this is the shaded error
# plt.plot(x_values, y_values) #this is the line itself
plt.show()
#better
x_values = range(0,10)
y_values = [10, 12, 13, 13, 15, 19, 20, 22, 23, 29]
y_lower = [eachyvalue - 2 for eachyvalue in y_values]
y_upper = [eachyvalue + 2 for eachyvalue in y_values]
# plt.fill_between(x_values, y_lower, y_upper, alpha=0.2) #this is the shaded error
# plt.plot(x_values, y_values) #this is the line itself
plt.show()
months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]
revenueupper = [eachrevenue * 1.1 for eachrevenue in revenue]
revenuelower = [eachrevenue * .90 for eachrevenue in revenue]
# revenuebar = plt.subplot()
# plt.fill_between(months, revenuelower, revenueupper, alpha=.20)
# plt.plot(months,revenue)
# revenuebar.set_xticks(months)
# revenuebar.set_xticklabels(month_names)
plt.show()

#pie chart
budget_data = [500, 1000, 750, 300, 100]
# plt.pie(budget_data)
# plt.axis("equal") #set the axes to be equal
plt.show()
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]
# plt.pie(payment_method_freqs, labels=payment_method_names, autopct="%1.1f%%")
# plt.legend(payment_method_names, loc=1)
# plt.axis("equal")
plt.show()

#histogram
dataset = [1, 3, 5, 7, 8, 6, 2, 1, 5, 8, 9, 5, 1, 5, 6, 4, 9, 6, 3, 2 ,6 ,8, 7]
# plt.hist(dataset, range=(1,10), bins=10)
plt.show()
dataset1 = [6,8,6,4,2,3,9,8,4,2,3,6,8,4,2,3,9,2,4,5]
dataset2 = [4,5,9,8,4,5,3,2,1,8,7,9,6,3,5,3,6,9,8,7]
# plt.hist(dataset1,range=(1,10), bins=10, alpha=.5) #display transparency transparent
# plt.hist(dataset2,range=(1,10), bins=10, alpha=.5) #display transparency transparent
plt.show()
# plt.hist(dataset1,range=(1,10), bins=10, histtype="step") #display histogram outline
# plt.hist(dataset2,range=(1,10), bins=10, histtype="step") #display histogram outline
plt.show()
#histograms might have different numbers of samples, making one much bigger than the other.  To solve this, we can normalize our histograms using normed=True. This command divides the height of each column by a constant such that the total shaded area of the histogram sums to 1.
bigdataset1 = [46622,92874,60191,12212,81275,44794,25632,56034,13040,62917]
bigdataset2 = [904572,207366,873910,182220,416248,214926,751013,464412,441280,531012]
# plt.hist(bigdataset1, range=(10000,100001), bins=5)
# plt.hist(bigdataset2, range=(100000,1000001), bins=5)
# plt.show()
# plt.hist(bigdataset1, range=(10000,100001), bins=5, alpha=.5, normed=True)
# plt.hist(bigdataset2, range=(100000,1000001), bins=5, alpha=.5, normed=True)
plt.show()

#Plot Types Multiple Choice Quiz
'''
Which line of code will create a bar graph with error bars displaying +/- 4 error, with caps of size 10?  plt.bar(x, y, yerr=4, capsize=10)
What is the command to plot a bar graph in Matplotlib?  plt.bar
What does it mean to normalize a histogram?  Normalizing is dividing the height of each column by a constant such that the area under the curve sums to 1.
What is the result of adding autopct='%d%%' to a plt.pie function call?  The pie chart will now display percentages, rounded to the nearest int, on each slice of the pie.
What type of graph would work best to display the proportion of team members who own a cat, dog, bird, or no pet? (Assume each team member can only own one pet.)  Pie
What is the command to divide the data in a histogram into 10 equally-sized bins?  plt.hist(data, bins=10)
In the following function call, what does the list [0, 2, 4, 6, 8] represent?  plt.fill_between(range(5), [0, 2, 4, 6, 8], [4, 6, 8, 10, 12], alpha=0.2)  The lower-bound y-values to plot
What are the inputs to the plt.bar function, in order?  x values (list of numbers), y values (list of numbers)
What type of graph would work best to display the change in temperature in a city over time?  Line
What is the command to stack a set of bars representing y2 on top of the set of bars representing y1?  plt.bar(range(len(y2)), y2, bottom=y1)
What is the command to set x-axis ticks to be "Carbohydrates", "Lipids", "Protein"?  ax.set_xticklabels(["Carbohydrates", "Lipids", "Protein"])
'''

#Recreate graphs using Matplotlib! Interactive Lesson
past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]
# plt.figure(figsize=(10,8))
# plt.bar(years,past_years_averages, yerr=error, capsize=5)
# plt.title("Final Exam Averages")
# plt.xlabel("Year")
# plt.ylabel("Test average")
# x1,x2,y1,y2 = plt.axis()
# plt.axis((x1,x2,70,95)) #https://stackoverflow.com/questions/3777861/setting-y-axis-limit-in-matplotlib
plt.show()
#plt.savefig("my_bar_chart.png")

import numpy as np
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]
ind = np.arange(len(unit_topics))
width = 0.8
#middle_school_a
n = 1 # This is our first dataset (out of 2)
t = 2 # Number of datasets 
d = len(middle_school_a) # Number of sets of bars 
w = 0.8 # Width of each bar 
middle_school_a_x = [t*element + w*n for element in range(d)]
#middle_school_b
n = 2 # This is our first dataset (out of 2)
t = 2 # Number of datasets 
d = len(middle_school_b) # Number of sets of bars 
w = 0.8 # Width of each bar 
middle_school_b_x = [t*element + w*n for element in range(d)]
# plt.figure(figsize=(10,8))
# plt.title("Test Averages on Different Units")
# plt.xlabel("Unit")
# plt.ylabel("Test Average")
# ax=plt.subplot()
# axes = plt.gca() #Get Current Axes
# axes.set_xlim([0,len(unit_topics)*2])  #there are ten bars
# axes.set_ylim([70,90])
# # or
# # x1,x2,y1,y2 = plt.axis()
# # plt.axis((0,len(unit_topics)*2,70,90))
# plt.bar(middle_school_a_x,middle_school_a, label="Middle School A")
# plt.bar(middle_school_b_x,middle_school_b, label="Middle School B")
# plt.legend(loc=1)
# ax.set_xticks(((ind+width)*2)-.415)
# ax.set_xticklabels(unit_topics)
plt.show()

import numpy as np
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]
x = range(0,len(unit_topics))
c_bottom = np.add(As, Bs)
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)
# plt.figure(figsize=(10,8))
# plt.title('Grade distribution')
# plt.xlabel('Unit')
# plt.ylabel('Number of Students')
# plt.bar(x,As)
# plt.bar(x,Bs, bottom=As)
# plt.bar(x,Cs, bottom=c_bottom)
# plt.bar(x,Ds, bottom=d_bottom)
# plt.bar(x,Fs, bottom=f_bottom)
# ax = plt.subplot()
# ax.set_xticks(x)
# ax.set_xticklabels(unit_topics)
plt.show()

exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48,78.81,79.23,74.38,79.27,81.07,75.42,90.35,82.93,86.74,81.33,95.1,86.57,83.66,85.58,81.87,92.14,72.15,91.64,74.21,89.04,76.54,81.9,96.5,80.05,74.77,72.26,73.23,92.6,66.22,70.09,77.2]
# plt.figure(figsize=(10,8))
# plt.title("Final Exam Score Distribution")
# plt.xlabel("Percentage")
# plt.ylabel("Frequency")
# plt.hist(exam_scores1, bins=12, normed=True, histtype="step", linewidth=2, label="1st Yr Teaching")
# plt.hist(exam_scores2, bins=12, normed=True, histtype="step", linewidth=2, label="2nd Yr Teaching")
# plt.legend()
plt.show()

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]
# plt.figure(figsize=(10,8))
# plt.pie(num_hardest_reported, labels=unit_topics, autopct="%1d%%")
# plt.title("Hardest Topics")
# plt.axis("equal")
plt.show()

hours_reported =[3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25,  3.5, 3.5, 3.75, 3.75,4, 4.0, 3.75,  4.0, 4.25, 4.25, 4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85, 74.44, 75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]
plt.figure(figsize=(10,8))
hours_lower_bound = [eachyvalue*.80 for eachyvalue in hours_reported]
hours_upper_bound = [eachyvalue*1.2 for eachyvalue in hours_reported]
plt.title("Time spent studying vs final exam scores")
plt.xlabel("Score")
plt.ylabel("Hours studying (self-reported)")
plt.fill_between(exam_scores, hours_lower_bound, hours_upper_bound, alpha=0.2)
plt.plot(exam_scores, hours_reported, linewidth=2)
plt.show()
plt.savefig("my_line_graph.png")