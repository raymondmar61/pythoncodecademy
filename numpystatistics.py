#https://www.codecademy.com/learn/intro-statistics-numpy
import numpy as np

#Introduction to Statistics with NumPy Interactive Lesson
survey_responses = [5, 10.2, 4, .3, 6.6]
survey_array = np.array(survey_responses)
print(np.mean(survey_array)) #print 5.220000000000001
store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18,  9,  2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])
print(np.mean(store_one)) #print 6.5
print(np.mean(store_two)) #print 10.428571428571429
print(np.mean(store_three)) #print 5.0
class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006, 2013, 1978, 1951, 1998, 1996, 1952, 2005, 2007, 2003, 1955, 1963, 1978, 2001, 2012, 2014, 1948, 1970, 2011, 1962, 1966, 1978, 1988, 2006, 1971, 1994, 1978, 1977, 1960, 2008, 1965, 1990, 2011, 1962, 1995, 2004, 1991, 1952, 2013, 1983, 1955, 1957, 1947, 1994, 1978, 1957, 2016, 1969, 1996, 1958, 1994, 1958, 2008, 1988, 1977, 1991, 1997, 2009, 1976, 1999, 1975, 1949, 1985, 2001, 1952, 1953, 1949, 2015, 2006, 1996, 2015, 2009, 1949, 2004, 2010, 2011, 2001, 1998, 1967, 1994, 1966, 1994, 1986, 1963, 1954, 1963, 1987, 1992, 2008, 1979, 1987])
#The logical statement np.mean(survey_array > n) evaluates which survey answers were greater than n, and assigns them a value of 1. np.mean adds all of the 1s up and divides them by the length of survey_array.
#Calculate the percent of attending alumni who graduated on and after 2005 and save your result to the variable millennials.
millennials = np.mean(class_year > 2005)
print(millennials) #print 0.2
ring_toss = np.array([[1, 0, 0], [0, 0, 1], [1, 0, 1]])
print(np.mean(ring_toss)) #print 0.4444444444444444 mean all ring_toss
print(np.mean(ring_toss, axis=1)) #print [0.33333333 0.33333333 0.66666667] mean each row; e.g. row one 1 0 0 row two 0 0 1 row three 1 0 1
print(np.mean(ring_toss, axis=0)) #print [0.66666667 0.         0.66666667] mean each column; e.g. column one 1 0 1 column two 0 0 0 colum three 0 1 1
temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91, 97, 88, 87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95, 96, 87, 99, 93, 90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86, 92, 98,94, 98, 90, 99, 96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 87, 87, 90, 90, 98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])
sorted_temps = np.sort(temps)
print(sorted_temps) #print [ 85  85  85  85  85  86  86  86  86  86  86  86  87  87  87  87  87  87  87  88  88  88  88  88  88  88  88  89  89  90  90  90  90  90  90  90  90  91  91  91  92  92  92  92  92  93  93  93  93  93  94  94  94  94  94  94  94  95  95  96  96  96  96  96  96  97  97  97  97  97  98  98  98  98  98  98  99  99  99  99  99 100 101 101 187 191 195 196 198 199]
#The median is the middle value of a dataset that’s been ordered in terms of magnitude.  If the length of our dataset was an even number, the median would be the value halfway between the two central values or the average of the two central values. 
incomes = [10100, 35500, 105000, 85000, 25500, 40500, 65000]
print(np.median(np.array(incomes))) #print 40500.0
#What if we wanted to find a point at which 40% of the samples are below, and 60% of the samples are above?  This type of point is called a percentile. The Nth percentile is defined as the point N% of samples lie below it. 40% of samples are below is called the 40th percentile. Percentiles are useful measurements because they can tell us where a particular value is situated within the greater dataset.
#There are 11 numbers in the dataset. The 40th percentile will have 40% of the 10 remaining numbers below it (40% of 10 is 4) and 60% of the numbers above it (60% of 10 is 6). So in this example, the 40th percentile is 4.  d = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8].  print(np.percentile(d, 40)) #print 4.00
patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])
thirtieth_percentile = np.percentile(patrons,30)
print(thirtieth_percentile) #print 3.0
seventieth_percentile = np.percentile(patrons,70)
print(seventieth_percentile) #print 8.0
#The difference between the first and third quartile is a value called the interquartile range.  Or the difference between the 25% and the 75% quartiles.  The interquartile range gives us an idea of how spread out our data is. The smaller the interquartile range value, the less variance in our dataset. The greater the value, the larger the variance.
movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2]) #data set number of movies watches watched in a week in hours
first_quarter = np.percentile(movies_watched, 25)
third_quarter = np.percentile(movies_watched, 75)
interquartile_range = third_quarter-first_quarter
print(first_quarter) #print 1.0
print(third_quarter) #print 3.5
print(interquartile_range) #print 2.5
#The standard deviation tells us the spread of the data. The larger the standard deviation, the more spread out our data is from the center. The smaller the standard deviation, the more the data is clustered around the mean.  We can find the standard deviation of a dataset using the Numpy function np.std.  nums = np.array([65, 36, 52, 91, 63, 79]) np.std(nums) 17.716909687891082
pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])
acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])
pumpkin_avg = np.mean(pumpkin)
acorn_squash_avg = np.mean(acorn_squash)
pumpkin_std = np.std(pumpkin)
acorn_squash_std = np.std(acorn_squash)
print(pumpkin_avg) #print 1431.8
print(acorn_squash_avg) #print  124.7
print(pumpkin_std) #print 611.3183785884406
print(acorn_squash_std) #print 87.22505374031019
rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11]) #rainfall inches each month on average
rain_mean = np.mean(rainfall)
rain_median = np.median(rainfall)
first_quarter = np.percentile(rainfall,25)
third_quarter = np.percentile(rainfall,75)
interquartile_range = third_quarter-first_quarter
rain_std = np.std(rainfall)
print(rain_mean) #print 2.895
print(rain_median) #print 2.81
print(first_quarter) #print 1.6775
print(third_quarter) #print 4.025
print(interquartile_range) #print 2.3475
print(rain_std) #print 1.5267312577311483

#Introduction to Statistics with NumPy Multiple Choice Quiz
'''
Consider the following one dimensional array. What Numpy command can we use to find the "middle value" of this set?  np.median(my_set)
What Numpy method can we use to identify outliers in our data?  np.sort()
What does the interquartile range refer to?  The difference between the first and third quartile.
What is the standard deviation?  A measure of how "spread out" your dataset it.
Which is the correct way of finding the 35th percentile for array 'd'?  np.percentile(d, 35)
What is the mean of a dataset?  The sum of all the values in the dataset divided by the number of values in the dataset.
We have a dataset named temps that contains numbers ranging from 32 to 100. Which method would you use to calculate the percentage of values that were less than 60?  np.mean(temps < 60)
The following array is two-dimensional. How do we calculate the means of each of the interior arrays?  np.mean(data, axis=1)
'''

#CrunchieMunchies Freeform Project
#Use NumPy statistical calculations to analyze this data and prove that your CrunchieMunchies cereal is the healthiest choice for consumers
calorie_stats = [70,120,70,50,110,110,110,130,90,90,120,110,120,110,110,110,100,110,110,110,100,110,100,100,110,110,100,120,120,110,100,110,100,110,120,120,110,110,110,140,110,100,110,100,150,150,160,100,120,140,90,130,120,100,50,50,100,100,120,100,90,110,110,80,90,90,110,110,90,110,140,100,110,110,100,100,110] #reported calorie amounts for different cereal brands
calorie_stats = np.array(calorie_stats) #convert list to numpy array
average_calories = np.mean(calorie_stats > 60)
print(average_calories) #print 0.961038961038961 How much higher is the average calorie count of your competition as a percentage?
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted) #print [ 50  50  50  70  70  80  90  90  90  90  90  90  90 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 120 120 120 120 120 120 120 120 120 120 130 130 140 140 140 150 150 160]
median_calories = np.median(calorie_stats)
print(median_calories) #print 110.0
nth_percentile = np.percentile(calorie_stats,60)
print(nth_percentile) #print 110.0 At 60%, 40% are over 110.0 and 60% are under 110.
#Calculate different percentiles and print them to the terminal until you find the lowest percentile that is greater than 60 calories.
for eachnumber in range(1,101):
	if np.percentile(calorie_stats,eachnumber) > 60:
		print(eachnumber) #print 4
		break
print(np.percentile(calorie_stats,4)) #print 70.0.  At 4%, 96% are calories 70 and greater
print(np.percentile(calorie_stats,3)) #print 55.599999999999994
#Let's calculate the percentage of cereals that have more than 60 calories per serving.
print(calorie_stats.size) #print 77 count items in array or length array length
greaterthan60calories = calorie_stats > 60 #Get calories array greater than 60 save to variable greaterthan60calories
print(calorie_stats[greaterthan60calories].size) #print 74 count items in array or length array length
print(calorie_stats[greaterthan60calories].size/calorie_stats.size) #print 0.961038961038961
#quicker way
print(np.mean(calorie_stats > 60)) #print 0.961038961038961
calorie_std = np.std(calorie_stats)
print(calorie_std) #print 19.35718533390827

#Statistical Distributions with NumPy Interactive Lesson
from matplotlib import pyplot as plt

historgramd = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]
historgramd = np.array(historgramd)
fiveorsiz = historgramd[(historgramd >= 4)]
print(fiveorsiz) #print [4 4 4 4 5]
print(fiveorsiz.size) #print 5
#plt.hist(historgramd,range=(1,6), bins=5, alpha=.5)
plt.show()
#plt.hist(historgramd,range=(2,4), bins=3, alpha=.5) #RM I can narrow the histogram to show 2's, 3's, and 4's only
plt.show()

#The NumPy library has several functions for generating random numbers, including one specifically built to generate a set of numbers that fit a normal distribution: np.random.normal. This function takes the following keyword arguments:  loc: the mean for the normal distribution; scale: the standard deviation of the distribution; size: the number of random numbers to generate.  a = np.random.normal(0, 1, size=100000)
#Suppose that we have a normal distribution with a mean of 50 and a standard deviation of 10. When we say "within one standard deviation of the mean", this is what we are saying mathematically:
'''
lower_bound = mean - std
            = 50 - 10
            = 40

upper_bound = mean + std
            = 50 + 10
            = 60
'''
#It turns out that we can expect about 68% of our dataset to be between 40 and 60, for this distribution.  No matter what mean and standard deviation we choose, 68% of our samples will fall between +/- 1 standard deviation of the mean!  68% of our samples will fall between +/- 1 standard deviation of the mean.  95% of our samples will fall between +/- 2 standard deviations of the mean.  99.7% of our samples will fall between +/- 3 standard deviations of the mean.
#The binomial distribution can help us. It tells us how likely it is for a certain number of “successes” to happen, given a probability of success and a number of trials.
#The probability of success was 30% (he makes 30% of free throws).  The number of trials was 10 (he took 10 shots).  The number of successes was 4 (he made 4 shots).
#Suppose we want to know the different probabilities of our basketball player making 1, 2, 3, etc. out of 10 shots.  NumPy has a function for generating binomial distributions: np.random.binomial, which we can use to determine the probability of different outcomes.  The function will return the number of successes for each "experiment".  It takes the following arguments:  N: The number of samples or trials; P: The probability of success; size: The number of experiments.
#Let's generate 10,000 "experiments"
# N = 10 shots
# P = 0.30 (30% he'll get a free throw)
# a = np.random.binomial(10, 0.30, size=10000)
a = np.random.binomial(10, 0.30, size=10000)
# plt.hist(a, range=(0, 10), bins=10)
# plt.xlabel('Number of "Free Throws"')
# plt.ylabel('Frequency')
plt.show()
#What percent chance did he have of making those 4 shots?  We can calculate a different probability by counting the percent of experiments with the same outcome, using the np.mean function.  Remember that taking the mean of a logical statement will give us the percent of values that satisfy our logical statement.
#Let's calculate the probability that he makes 4 baskets:
a = np.random.binomial(10, 0.30, size=10000)
fourbaskets = np.mean(a == 4)
print(fourbaskets) #print 0.2003 probability basketball player makes four shots.  #because we're using a random number generator, we'll get a slightly different result each time.
sunflowerheights = [13.89, 14.7, 13, 11.37, 12.1, 11.82, 13.09, 13.78, 12, 12.83, 12.1, 11.09, 13.32, 11.86, 14.35, 11.7, 12.85, 14, 13.83, 12.02, 12.05, 14.1, 12.39, 11.83, 13.18, 11.43, 14.61, 13.12, 11.5, 11.15, 12.64, 14.07, 12.44, 11.21, 14.31, 14.62, 14.67, 14.55, 12.72, 11.19, 13.27, 12.02, 13.79, 13.14, 14.51, 12.37, 14.06, 14.36, 11.24, 14.73, 13.03, 13.86, 13.33, 11.3, 12.18, 11.75, 14.69, 14.18, 14.05, 12.58, 14.53, 12.45, 14.44, 12.76, 11.65, 14.7, 14.54, 12.98, 13.08, 14.63, 13.22, 12.59, 14.62, 11.37, 14.55, 14.7, 14.89, 11.45, 14.74, 13.78, 13.62, 12.36, 11.15, 11.15, 13.1, 12.82, 12.34, 13.25, 12.1, 14.69, 14.58, 14.89, 14.03, 12.29, 12.03, 11.83, 13.57, 11.75, 13.64, 12.42, 13.07, 12.97, 14.89, 11.23, 13.45, 14.11, 12.47, 12.24, 13.9, 12.85, 14.65, 13.54, 12.76, 12.41, 11.61, 11.77, 11.44, 13.85, 13.02, 14.61, 13.68, 12.99, 11.88, 12.48, 12.78, 12.23, 13.88, 12.83, 13.41, 13.9, 12.35, 12.91, 11.32, 13.63, 11.37, 12.87, 11.27, 12.56, 11.87, 12.53, 14.5, 11.38, 11.25, 11.13, 13.7, 12.58, 11.88, 14.5, 11.91, 13.87, 14.38, 12.04, 13.61, 13.1, 12.96, 12.3, 14.54, 13.66, 14.86, 12.42, 14.34, 14.1, 12.37, 14.33, 11.64, 13.45, 13.49, 13.55, 12.65, 11.54, 12.48, 12.26, 13.93, 11.98, 12.04, 14.59, 11.51, 12.49, 13.71, 11.26, 12.15, 13.84, 14.62, 11.76, 12.59, 13.56, 12.21, 11.24, 14.47, 14.63, 12.51, 11.43, 14.84, 14.14, 14.16, 12.93, 13.19, 11.53, 12.78, 12.79]
sunflowers = np.array(sunflowerheights)
sunflowers_mean  = np.mean(sunflowers)
print(sunflowers_mean) #print 13.002150000000002
sunflowers_std = np.std(sunflowers)
print(sunflowers_std) #print 1.123322250068964
#create a normal distribution curve 5,000 samples using the sunflowers_mean and sunflowers_std
sunflowers_normal = np.random.normal(loc=sunflowers_mean, scale=sunflowers_std, size=5000)
#plt.hist(sunflowers_normal) #x-axis is height of sunflowers, y-axis is number of sunflowers at the x-axis height totaling 5,000.  RM:  it's random generating normal distribution
plt.show()
#10% of sunflowers that are planted fail to bloom. We planted 200, and want to know the probability that fewer than 20 will fail to bloom.  Generate 5,000 binomial random numbers that represent our situation.  np.random.binomial(number of trials, probability of success, size=number of experiments).
experiments = np.random.binomial(200, .10, size=5000)
prob = np.mean(experiments<20) #What percent of experiments had fewer than 20 sunflowers fail to bloom?  RM:  it's random generating percentage
print(prob) #print .4684

#Statistical Distributions with NumPy Multiple Choice Quiz
'''
What is a histogram?  A chart that creates equally spaced bins and counts how many values from our dataset fall into each bin.
In a normal distribution, how much of the data lies within one standard deviation?  68%
What type of distribution does this graph represent?  Bimodal distribution.  This graph has two peaks, so we would describe it as bimodal distribution.
Why do we use binomial distributions?  Because they are effective at helping us understand the different probabilities that an event will occur.  Binomial distributions are excellent at predicting if an event will occur given probability and sample size.
How many peaks does a unimodal dataset have?  One.
Which of the following are the correct keyword arguments for generating a random distribution using np.random.binomial?  
Which of the following are the correct keyword arguments for generating a random distribution using np.random.binomial?  N, P, size.  N is the number of trials, P is the probability of success, and size relates to the number of experiments.
Select the graph that represents a skew-left dataset.  We can tell because the left tail is longer.
The average height of a male giraffe is 16.3 feet with a standard deviation of 3.3 feet. Which of the following will generate a random distribution of 1000 male giraffe heights using np.random.normal?  np.random.normal(loc = 16.3, scale = 3.3, size = 1000)
'''

#Election Results Freeform Project
#A survey to determine how many people would vote for Cynthia Ceballos vs. Justin Kerrigan in the mayoral election.  Compare the survey responses to the actual results.
survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']
survey_responses = np.array(survey_responses)
print(survey_responses)
print(survey_responses[(survey_responses == "Ceballos")]) #print ['Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos']
total_ceballos = survey_responses[(survey_responses == "Ceballos")]
print(total_ceballos) #print ['Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos' 'Ceballos']
print(total_ceballos.size) #print 33
print(survey_responses.size) #print 70
percentage_ceballos = total_ceballos.size/survey_responses.size
print(percentage_ceballos) #print 0.4714285714285714
#In the real election, 54% of the 10,000 town population voted for Cynthia Ceballos.  Generate a binomial distribution that takes the number of total survey responses, the actual success rate, and the size of the town's population as its parameters. Then divide the distribution by the number of survey responses. Save your calculation to the variable possible_surveys.
possible_surveys = np.random.binomial(70, .54, size=10000)
print(possible_surveys) #print [43 32 40 ... 33 38 37]  #RM:  number of survey responses voted for Ceballos out of 70 total survey_responses.size
possible_surveys = possible_surveys / survey_responses.size
print(possible_surveys) #print [0.61428571 0.45714286 0.57142857 ... 0.47142857 0.54285714 0.52857143] #RM:  number of survey responses voted for Ceballos out of 70 total survey_responses.size as a percentage
#plt.hist(possible_surveys, range=(0,1), bins=20)
plt.show()
#47% of people we surveyed said they would vote for Ceballos, but 54% of people voted for Ceballos in the actual election.  Calculate the percentage of surveys that could have an outcome of Ceballos receiving less than 50% of the vote and save it to the variable ceballos_loss_surveys.
ceballos_loss_surveys = np.mean(possible_surveys < .50)
print(ceballos_loss_surveys) #print 0.2179
#With this current poll of 70 responses, about 20% of the time a survey output would predict Kerrigan winning, even if Ceballos won the actual election.  Your co-worker points out that your poll would be more accurate if it had more responders.  Generate another binomial distribution, but this time, see what would happen if you had instead surveyed 7,000 people. Divide the distribution by the size of the survey and save your findings to large_survey.
large_survey = np.random.binomial(7000, .54, size=10000)
print(large_survey) #print [3795 3798 3902 ... 3715 3863 3812]  #RM:  number of survey responses voted for Ceballos out of 7000
large_survey = large_survey / 7000
print(large_survey) #print [0.54214286 0.54257143 0.55742857 ... 0.53071429 0.55185714 0.54457143] #RM:  number of survey responses voted for Ceballos out of 7000 as a percentage
#plt.hist(large_survey, range=(0,1), bins=20)
plt.show()
#recalculate the percentage of surveys that would have an outcome of Ceballos losing and save it to the variable ceballos_loss_new
ceballos_loss_new = np.mean(large_survey < .50)
print(ceballos_loss_new) #print 0.0  RM:  Ceballos wins election.  7,000 responses instead of 70 respones.  The new probability Ceballos receives less than 50% with 7,000 responses is 0.0.