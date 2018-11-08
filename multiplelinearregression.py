#Multiple Linear Regression uses two or more independent variables to predict the values of the dependent variable.  When we have two independent variables, we can create a linear regression plane. We can now guess what the rent is by plugging in the independent variables and finding where they lie on the plane.
import pandas as pd
from sklearn.model_selection import train_test_split

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
#Now we have the training set and the test set, let's use scikit-learn to build the linear regression model!
#we need to import LinearRegression from the linear_model module:  from sklearn.linear_model import LinearRegression
#Then, create a LinearRegression model, and then fit it to your x_train and y_train data: mlr = LinearRegression() mlr.fit(x_train, y_train) # finds the coefficients and the intercept value
#We can also use the .predict() function to pass in x-values. It returns the y-values that this plane would predict:  y_predicted = mlr.predict(x_text) # takes values calculated by `.fit()` and the `x` values, plugs them into the multiple linear regression equation, and calculates the predicted y values.
#We will start by using two of these columns to teach you how to predict the values of the dependent variable, prices.
from sklearn.linear_model import LinearRegression
mlr = LinearRegression()
mlr.fit(x_train,y_train)
y_predict = mlr.predict(x_test)
#Checkpoint:  We have x_test, x_train, y_test, y_train, and y_predict!