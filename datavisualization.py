#https://www.codecademy.com/learn/data-visualization-python
#LINE GRAPHS IN MATPLOTLIB
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
#plt.plot(days, money_spent_2, color="orange", linestyle=":", marker="s") #orange dotted square
plt.show()