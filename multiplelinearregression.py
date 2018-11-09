#Multiple Linear Regression uses two or more independent variables to predict the values of the dependent variable.  When we have two independent variables, we can create a linear regression plane. We can now guess what the rent is by plugging in the independent variables and finding where they lie on the plane.
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

streeteasy = pd.read_csv("queens.csv")
#print(streeteasy)
'''
We have to split our dataset into:
	Training set: the data used to fit the model
	Test set: the data partitioned away at the very start of the experiment (to provide an unbiased evaluation of the model)
In general, putting 80% of your data in the training set and 20% of your data in the test set is a good place to start.  Suppose you have some values in x and some values in y:

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

Here are the parameters:
	train_size: the proportion of the dataset to include in the train split (between 0.0 and 1.0)
	test_size: the proportion of the dataset to include in the test split (between 0.0 and 1.0)
	random_state: the seed used by the random number generator [optional]
'''

#Create a DataFrame x that selects the following columns from the main df DataFrame
x = streeteasy[["bedrooms","bathrooms",'size_sqft','min_to_subway','floor','building_age_yrs','no_fee','has_roofdeck','has_washer_dryer','has_doorman','has_elevator','has_dishwasher','has_patio','has_gym']]
#Create a DataFrame y that selects the rent column from the main df DataFrame.
y = streeteasy["rent"]
#Use scikit-learn's train_test_split() method to split x into 80% training set and 20% testing set and generate: x_train, x_test, y_train, y_test, Set the random_state to 6.
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)
#Let's take a look at the shapes of x_train, x_test, y_train, and y_test to see we got the proportion we wanted.  We have 14 features that we're looking for each apartment, and 1 label we're looking for each apartment.
# print(x_train) #print 80% of x rows
# print(x_test) #print 20% of x rows
# print(y_train) #print 80% of y rows
# print(y_test) #print 20% of y rows
#Now we have the training set and the test set, let's use scikit-learn to build the linear regression model.
#we need to import LinearRegression from the linear_model module:  from sklearn.linear_model import LinearRegression
#Then, create a LinearRegression model, and then fit it to your x_train and y_train data: mlr = LinearRegression() mlr.fit(x_train, y_train) #finds the coefficients and the intercept value
#We can also use the .predict() function to pass in x-values. It returns the y-values that this plane would predict:  y_predicted = mlr.predict(x_text) #takes values calculated by .fit() and the x values, plugs them into the multiple linear regression equation, and calculates the predicted y values.
#We will start by using two of these columns to teach you how to predict the values of the dependent variable, prices.
from sklearn.linear_model import LinearRegression
mlr = LinearRegression()
mlr.fit(x_train,y_train)  #.fit() is before .predict()
y_predict = mlr.predict(x_test)
#Checkpoint:  We have x_test, x_train, y_test, y_train, and y_predict
#Create a 2D scatterplot to see how the independent variables impact prices.  x-axis is the actual rent.  y-axis is the predicted rent.
# plt.scatter(y_test,y_predict,alpha=.4)
# plt.xlabel("Actual Prices")
# plt.ylabel("Predicted Prices")
# plt.title("Actual Rent vs. Predicted Rent")
plt.show()
#multiple linear regression can use any number of independent variables, its general equation becomes:  y=b+m1x1+m2​x2+...+mxnx.  The m are the coefficients and the b are the intercepts.
#The .fit() method gives the model two variables that are useful to us:  .coef_, which contains the coefficients; .intercept_, which contains the intercept.  You can print the coefficients using .coef_; specifically assignedLinearRegression()variable.coef_.  Coefficients are most helpful in determining which independent variable carries more weight. For example, a coefficient of -1.345 will impact the rent more than a coefficient of 0.238, with the former impacting prices negatively and latter positively.
print(mlr.coef_) #print [ 259.49483776  472.15466299    0.97777539  -10.29535775   33.05646388   -8.12803401  259.14494075   62.78960059  124.40966155   56.38161397  157.69503746 -195.65879788  237.50188285   84.89712538]  #RM:  there are 14 coefficients for the 14 independent variables
#The independent variables will either have a positive linear relationship to the dependent variable, a negative linear relationship, or no relationship. A negative linear relationship means that as X values increase, Y values will decrease. Similarly, a positive linear relationship means that as X values increase, Y values will also increase.
#Graphically, when you see a downward trend, it means a negative linear relationship exists. When you find an upward trend, it indicates a positive linear relationship.
#We graph the relationship between square feet size_sqft and rent.
# plt.scatter(streeteasy[['size_sqft']], streeteasy[['rent']], alpha=0.4)
# plt.xlabel("Square Feet")
# plt.ylabel("Rent")
# plt.title("Square Feet Relation To Rent")
plt.show()
#We can use Residual Analysis to evalulate the accuracy of our multiple linear regression model.  It's one technique.  The difference between the actual value y and the predicted value yhat is the residual e or e = y-yhat.  y is the actual rent.  yhat is the predicted rent.
#sklearn's linear_model.LinearRegression comes with a .score() method that returns the coefficient of determination R^2 of the prediction.  R^2=1-(u/v) where u is the residual sum of squares ((y - y_predict) ** 2).sum() and v is the total sum of squares ((y - y.mean()) ** 2).sum().  The total sum of squares tells you how much variation there is in the y variable.  R^2 is the percentage variation in y explained by all the x variables together.
#For example, say we are trying to predict rent based on the size_sqft and the bedrooms in the apartment and the R^2 for our model is 0.72 — that means that all the x variables (square feet and number of bedrooms) together explain 72% variation in y (rent).
#We add another x variable, building's age, to our model. By adding this third relevant x variable, the R^2 is expected to go up. Let say the new R^2 is 0.95. This means that square feet, number of bedrooms, and age of the building together explain 95% of the variation in the rent.
#The best possible R^2 is 1.00 (and it can be negative because the model can be arbitrarily worse). Usually, a R^2 of 0.70 is considered good.
print(mlr.score(x_train,y_train)) #print 0.6658360310089573 mean squared error regression loss for the training set
print(mlr.score(x_test,y_test)) #print 0.665170319780827 mean squared error regression loss for the testing set
residuals = y_predict - y_test
# plt.scatter(y_predict, residuals, alpha=0.4)
# plt.title('Residual Analysis residuals vs. predicted_y values')
plt.show()
'''
Review
Multiple Linear Regression uses two or more variables to make predictions about another variable y=b+m1x1+m2​x2+...+mxnx.
Multiple linear regression uses a set of independent variables and a dependent variable. It uses these variables to learn how to find optimal parameters. It takes a labeled dataset and learns from it. Once we confirm that it's learned correctly, we can then use it to make predictions by plugging in new x values.
We can use scikit-learn's LinearRegression() to perform multiple linear regression.
Residual Analysis is used to evaluate the regression model's accuracy. In other words, it's used to see if the model has learned the coefficients correctly.
Scikit-learn's linear_model.LinearRegression comes with a .score() method that returns the coefficient of determination R^2 of the prediction. The best score is 1.0.
'''

#Multiple Linear Regression Multiple Choice Quiz
'''
In the multiple linear regression equation, what are the m variables y=b+m1x1+m2​x2+...+mxnx?  The coefficients.  The coefficients are helpful in determining which independent variable carries more weight.
True/False: The test set is the data that you partition away at the very start of your experiment (to provide an unbiased evaluation of the model).  True.
Find the Error: Which line would break the following code?  y_predict = regr.predict(x_test).  Yes, this line would cause the error, because you haven't .fit() the model yet.
Which of the two coefficients will have a greater impact on the dependent variable — a coefficient of -1.5 or a coefficient of 1.5?  They will have the same level of impact.  One will cause y values to drop and the other will cause them to rise. However, they'll do it with the same level of impact.
Which of the following statements is true about Residual Analysis?  Residual Analysis allows you to assess the accuracy of a multiple linear regression model.  A residual is the difference between the real value and the predicted value.
Given a regression line and four data points, which point has the largest residual?  C.  It has the greatest difference between the observed value of the dependent variable (y) and the predicted value (yhat).
What does it mean for a model to have an R^2 value of 0?  A value of 0 would indicate that the model fails to accurately model the data at all.
Fill in the Blank: from _________ import LinearRegression.  What is the module we are importing from?  sklearn.linear_model
'''