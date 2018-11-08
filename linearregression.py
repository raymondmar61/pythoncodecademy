#Linear Regression Interactive Lesson
#Given a set of data points, find a line that fits the data best! This is the simplest form of regression, and allows us to make predictions of future points.  Find a line that fits a set of data best, we are performing Linear Regression.  A line is a rough approximation, but it allows us the ability to explain and predict variables that have a linear relationship with each other.

from matplotlib import pyplot as plt
#lemonade revenue by month
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]
# plt.plot(months, revenue, "o")
# plt.title("Sandra's Lemonade Stand")
# plt.xlabel("Months")
# plt.ylabel("Revenue ($)")
plt.show()
'''
A line is determined by its slope and its intercept. In other words, for each point y on a line we can say:  y=mx+b.  m is the slope.  b is the intercept. y is a given point on the y-axis and it corresponds to a given x on the x-axis.  The slope is a measure of how steep the line is, while the intercept is a measure of where the line hits the y-axis.
'''
#slope:
m = 8
#intercept:
b = 40
y = [((m*x)+b) for x in months]
# print(y)
# plt.plot(months, y, "o")
# plt.title("Sandra's Lemonade Stand y=mx+b")
# plt.xlabel("Months")
# plt.ylabel("Revenue y ($)")
plt.show()
'''
For each data point, we calculate loss, a number that measures how bad the model's (in this case, the line's) prediction was. You may have seen this being referred to as error.
We can think about loss as the squared distance from the point to the line. We do the squared distance (instead of just the distance) so that points above and below the line both contribute to total loss in the same way.  In this example:  For point A, the squared distance is 9 (3**2)
For point B, the squared distance is 1 (1**2). RM:  Point A is three points above the line.  Point A is one point below the line.   The total loss is 10=9+1.  A line that had less loss than 10 is a better model.
'''
x = [1, 2, 3]
y = [5, 1, 3]
#y = x
m1 = 1
b1 = 0
#y = 0.5x + 1
m2 = 0.5
b2 = 1
y_predicted1 = [(m1*eachx)+b1 for eachx in x]
y_predicted2 = [(m2*eachx)+b2 for eachx in x]
total_loss1 = 0
for n in range(0,len(y)):
  difference = (y[n]-y_predicted1[n])**2
  total_loss1 = total_loss1 + difference
total_loss2 = 0
for n in range(0,len(y)):
  difference = (y[n]-y_predicted2[n])**2
  total_loss2 = total_loss2 + difference
print(total_loss1) #print 17
print(total_loss2) #print 13.5  total_loss2 is the better fit.  RM:  no numpy?
#The goal of a linear regression model is to find the slope and intercept pair that minimizes loss on average across all of the data.
#As we try to minimize loss, we take each parameter we are changing, and move it as long as we are decreasing loss. It's like we are moving down a hill, and stop once we reach the bottom.  The process by which we do this is called gradient descent. We move in the direction that decreases our loss the most. Gradient refers to the slope of the curve at any point.  We find the sum of y_value - (m*x_value + b) for all the y_values and x_values we have and then we multiply the sum by a factor of -2/N. N is the number of points we have.
def get_gradient_at_b(x, y, m, b):
	diff = 0
	for i in range(0,len(x)):
		diff = diff + ((y[i])-((m*x[i])+b))  #RM:  no numpy?
		b_gradient = diff*(-2/len(x)) #len(x) is the number of points for -2/N.
	return b_gradient
#To find the m gradient, or the way the loss changes as the slope of our line changes,  we find the sum of x_value * (y_value - (m*x_value + b)) for all the y_values and x_values we have and then we multiply the sum by a factor of -2/N. N is the number of points we have.
#Once we have a way to calculate both the m gradient and the b gradient, we'll be able to follow both of those gradients downwards to the point of lowest loss for both the m value and the b value. Then, we'll have the best m and the best b to fit our data!
def get_gradient_at_m(x, y, m, b):
	diff = 0
	N = len(x) #N is the number of points we have or len(x)
	for i in range(0,N):
		diff = diff + (x[i]*(y[i]-((m*x[i])+b)))
		m_gradient = (-2/N)*diff
	return m_gradient
#Now that we know how to calculate the gradient, we want to take a "step" in that direction. However, it's important to think about whether that step is too big or too small. We don't want to overshoot the minimum error!  We can scale the size of the step by multiplying the gradient by a learning rate.
#To find a new b value, we would say:  new_b = current_b - (learning_rate * b_gradient) where current_b is our guess for what the b value is, b_gradient is the gradient of the loss curve at our current guess, and learning_rate is proportional to the size of the step we want to take.
def step_gradient(x, y, b_current, m_current):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (0.01 * b_gradient)
    m = m_current - (0.01 * m_gradient)
    return [b, m]
# current intercept guess:
b = 0
# current slope guess:
m = 0
b, m = step_gradient(months, revenue, b, m)
print(b, m) #print 2.355 17.78333333333333
#How do we know when we should stop changing the parameters m and b?  Convergence is when the loss stops changing (or changes very slowly) when parameters are changed.  Hopefully, the algorithm will converge at the best values for the parameters m and b.  e.g. at the 600th iteration, the b value or y-intercept converged at 45.
#We want our program to be able to iteratively learn what the best m and b values are. So for each m and b pair that we guess, we want to move them in the direction of the gradients we've calculated. But how far do we move in that direction?  We have to choose a learning rate, which will determine how far down the loss curve we go.  Finding the absolute best learning rate is not necessary for training a model. You just have to find a learning rate large enough that gradient descent converges with the efficiency you need, and not so large that convergence never happens.
'''
#RM:  full Machine Larning Linear Regression
def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

#Your step_gradient function here
def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]
  
#Your gradient_descent function here:  
def gradient_descent(x, y, learning_rate, num_iterations):
  b = 0
  m = 0
  for i in range(0,num_iterations):
    b, m = step_gradient(b,m,x,y,learning_rate)    
  return [b,m]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#Uncomment the line below to run your gradient_descent function
b, m = gradient_descent(months, revenue, 0.01, 1000)

#Uncomment the lines below to see the line you've settled upon!
y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()
'''
#Congratulations! You've now built a linear regression algorithm from scratch.
#Luckily, we don't have to do this every time we want to use linear regression. We can use Python's scikit-learn library. Scikit-learn, or sklearn, is used specifically for Machine Learning. Inside the linear_model module, there is a LinearRegression() function we can use:  from sklearn.linear_model import LinearRegression
#You can first create a LinearRegression model, and then fit it to your x and y data:  line_fitter = LinearRegression();  line_fitter.fit(X, y).
#The .fit() method gives the model two variables that are useful to us:  the line_fitter.coef_, which contains the slope; the line_fitter.intercept_, which contains the intercept.
#We can also use the .predict() function to pass in x-values and receive the y-values that this line would predict:  y_predicted = line_fitter.predict(X).
#Note: the num_iterations and the learning_rate that you learned about in your own implementation have default values within scikit-learn, so you don't need to worry about setting them specifically!
from sklearn.linear_model import LinearRegression
import numpy as np
#a dataset of soup sales data vs temperature.
temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]
line_fitter = LinearRegression()
line_fitter.fit(temperature, sales)
sales_predict = line_fitter.predict(temperature)
print(sales_predict) #print [56.34285714 54.03834586 51.73383459 49.42932331 47.12481203 44.82030075 42.51578947 40.2112782  37.90676692 35.60225564 33.29774436 30.99323308 28.6887218  26.38421053 24.07969925 21.77518797 19.47067669 17.16616541 14.86165414 12.55714286]
# plt.plot(temperature, sales, 'o')
# plt.plot(temperature,sales_predict,"*")
plt.show()
'''
Review
We have seen how to implement a linear regression algorithm in Python, and how to use the linear regression model from scikit-learn. We learned:
We can measure how well a line fits by measuring loss.
The goal of linear regression is to minimize loss.
To find the line of best fit, we try to find the b value (intercept) and the m value (slope) that minimize loss.
Convergence refers to when the parameters stop changing with each iteration.
Learning rate refers to how much the parameters are changed on each iteration.
We can use Scikit-learn's LinearRegression() model to perform linear regression on a set of points.
'''

#Linear Regression Multiple Choice Quiz
'''
What is the purpose of performing gradient descent?  To move parameters in the direction that minimizes loss.  We are trying to find the minimum point of the loss curve, not change the slope.
If the algorithm is taking too long to converge, should you move the learning rate up or down?  Up.
The goal of a linear regression algorithm is to find the ___ and ___ that minimize average loss.  slope; intercept
If the model worked correctly, what should y_new represent in the code below?  regr = LinearRegression() regr.fit(X, y) y_new = regr.predict(X),  The y-values that X would produce on the line of best fit.
Let's say we have 3 lines that produce the following average loss on our dataset. Which one is the line of best fit?  Line A: 17 Line B: 11.5 Line C: 13.  B.  This is the line with the lowest average loss, which is what we want.
What is the sum of squared error between the points described by x_values and y_values and the line described by m and b?  y_values_of_points = [1, -4, -7, -6] y_values_of_line = [1, -3, -6, -8].  6.  To find the loss, square the distance from each point to the line, and add these together (0^2 + 1^2 + 1^2 + (-2)^2 = 6)
When does the linear regression algorithm stop?  When the parameters stop changing (or change very slowly).  This is how we know the algorithm has converged.
Which of these lines seems to fit the data best?
'''

#Honey Production Freeform Project
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
df = pd.read_csv("honeyproduction.csv")
#print(df)
prod_per_year  = df.groupby("year").totalprod.mean() #group average totalprod by year
#Create a variable called X that is the column of years in this prod_per_year DataFrame.  After creating X, we will need to reshape it to get it into the right format, using this command:  X = X.values.reshape(-1, 1).  RM:  create the x-values list which is year.
X = df["year"]
X = X.values.reshape(-1, 1)
y = df["totalprod"] #RM:  create the y-values list which is totalprod or total production
#plt.scatter(X,y)
#plt.show()
regr = LinearRegression() #Create a linear regression model from scikit-learn and call it regr.  Use the LinearRegression() constructor from the linear_model module to do this.
regr.fit(X,y) #Fit the model to the data by using .fit(). You can feed X into your regr model by passing it in as a parameter of .fit().
#After you have fit the model, print out the slope of the line (stored in a list called regr.coef_) and the intercept of the line (regr.intercept_).
print(regr.coef_) #print [-88582.62988818]
print(regr.coef_[0]) #print -88582.62988818
print(regr.intercept_) #print 181765231.19491225
y_predict = regr.predict(X) #Create a list called y_predict that is the predictions your regr model would make on the X data.
#print(y_predict)
#plt.plot(X,y_predict)
plt.show()

#Let's predict what the year 2050 may look like in terms of honey production.
#create a NumPy array called X_future that is the range from 2013 to 2050.  RM:  years 2013-2050. x-axis
X_future = np.array(range(2013,2051))
#print(X_future) #print [2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 2027 2028 2029 2030 2031 2032 2033 2034 2035 2036 2037 2038 2039 2040 2041 2042 2043 2044 2045 2046 2047 2048 2049 2050]
X_future = X_future.reshape(-1,1) #we need to reshape it for scikit-learn.
#print(X_future) #print [[2013] [2014] [2015] [2016] [2017] [2018] [2019] [2020] [2021] [2022] [2023] [2024] 2025] [2026] [2027] [2028] [2029] [2030] [2031] [2032] 2033] [2034] [2035] [2036] [2037] [2038] [2039] [2040] 2041] [2042] [2043] [2044] [2045] [2046] [2047] [2048] [2049] [2050]]
future_predict = regr.predict(X_future) #Create a list called future_predict that is the predictions your regr model would make on the X_future data.
print(future_predict) #print [3448397.22999918 3359814.60011098 3271231.9702228  3182649.34033462 3094066.71044645 3005484.08055824 2916901.45067006 2828318.82078189 2739736.19089371 2651153.56100553 2562570.93111733 2473988.30122915 2385405.67134097 2296823.0414528  2208240.41156462 2119657.78167641 2031075.15178823 1942492.52190006 1853909.89201188 1765327.26212367 1676744.6322355  1588162.00234732 1499579.37245914 1410996.74257097 1322414.11268276 1233831.48279458 1145248.85290641 1056666.22301823  968083.59313005  879500.96324185  790918.33335367  702335.70346549  613753.07357731  525170.44368911  436587.81380093  348005.18391275  259422.55402458  170839.9241364 ]
#plt.plot(X_future,future_predict)
plt.show()