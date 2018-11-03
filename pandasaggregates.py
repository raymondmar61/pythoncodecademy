import pandas as pd
import numpy as np

#Aggregates in Pandas Interactive Lesson
#dataframe.columnname.aggregate() or df.column_name.command().  dataframe.columnname.median(), dataframe.columnname.nunique(), dataframe.columnname.unique().
'''
mean	Average of all values in column
std	Standard deviation
median	Median
max	Maximum value in column
min	Minimum value in column
count	Number of values in column
nunique	Number of unique values in column
unique	List of unique values in column
'''
orders = pd.read_csv('orders.csv')
print(orders.head(10))
most_expensive = orders.price.max() #highest price in price column
num_colors = orders.shoe_color.nunique() #count unique colors in shoe_color column
#Pandas give an easier option to loop using .groupby.  General template is df.groupby('column1').column2.measurement().  e.g. grades = df.groupby('student').grade.mean().  groupby function creates a new Series, not a DataFrame.
pricey_shoes = orders.groupby("shoe_type").price.max() #most expensive shoes grouped by shoe_type
print(pricey_shoes)
'''
shoe_type
ballet flats    481.0
boots           478.0
clogs           493.0
sandles         456.0
stilettos       487.0
wedges          461.0
Name: price, dtype: float64
'''
print(type(pricey_shoes)) #print <class 'pandas.core.series.Series'>
#groupby function creates a new Series, not a DataFrame; e.g. print(type(pricey_shoes)) is a Series.
#We'd prefer that those indices were actually a column. In order to get that, we can use reset_index(). This will transform our Series into a DataFrame and move the indices into their own column.  General template df.groupby('column1').column2.measurement().reset_index().
pricey_shoesresetindex = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoesresetindex)  #RM notice the difference between a Series and DataFrame.  We have column names in DataFrame
'''
      shoe_type  price
0  ballet flats  481.0
1         boots  478.0
2         clogs  493.0
3       sandles  456.0
4     stilettos  487.0
5        wedges  461.0
'''
print(type(pricey_shoesresetindex)) #print <class 'pandas.core.frame.DataFrame'>
#Sometimes, the operation is more complicated than mean or count.  Use the apply method and lambda functions, just like we did for individual column operations. Note that the input to our lambda function will always be a list of values.
# np.percentile can calculate any percentile over an array of values high_earners = df.groupby('category').wage.apply(lambda x: np.percentile(x, 75)).reset_index()
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()
print(cheap_shoes) #RM:  inconsistent prices in orders.csv at codecademy website
'''
  shoe_color   price
0      black  222.25
1      brown  193.50
2       navy  205.50
3        red  250.00
4      white  196.00
'''
#Sometimes, we want to group by more than one column. We can easily do this by passing a list of column names into the groupby method.  e.g. df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index().  Group average Total Sales by Location and Day Of Week.
shoe_counts = orders.groupby(["shoe_type","shoe_color"])["id"].count().reset_index()
print(shoe_counts)
'''
     shoe_type shoe_color  id
0   ballet flats      black   2
1   ballet flats      brown   5
2   ballet flats        red   3
3   ballet flats      white   5
4          boots      black   3
5          boots      brown   5
6          boots       navy   6
*partial*
'''
#Reorganizing a table to an Excel-like table  is called a pivot table.  df.pivot(columns='ColumnToPivot', index='ColumnToBeRows', values='ColumnToBeValues')
# First use the groupby statement: unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
# Now pivot the table pivoted = unpivoted.pivot(columns='Day of Week', index='Location', values='Total Sales')
pivoted = shoe_counts.pivot(columns="shoe_color", index="shoe_type", values = "id")
print(pivoted)
'''
shoe_color    black  brown  navy  red  white
shoe_type                                   
ballet flats    2.0    5.0   NaN  3.0    5.0
boots           3.0    5.0   6.0  2.0    3.0
clogs           4.0    6.0   1.0  4.0    1.0
sandles         1.0    4.0   5.0  3.0    4.0
stilettos       5.0    3.0   2.0  2.0    2.0
wedges          3.0    4.0   4.0  5.0    2.0
'''
pivotedresetindex = shoe_counts.pivot(columns="shoe_color", index="shoe_type", values = "id").reset_index()
print(pivotedresetindex)
'''
shoe_color     shoe_type  black  brown  navy  red  white
0           ballet flats    2.0    5.0   NaN  3.0    5.0
1                  boots    3.0    5.0   6.0  2.0    3.0
2                  clogs    4.0    6.0   1.0  4.0    1.0
3                sandles    1.0    4.0   5.0  3.0    4.0
4              stilettos    5.0    3.0   2.0  2.0    2.0
5                 wedges    3.0    4.0   4.0  5.0    2.0
'''
user_visits = pd.read_csv("page_visits.csv")
print(user_visits.head(10))
click_source = user_visits.groupby("utm_source").id.count().reset_index()
print(click_source)
'''
  utm_source   id
0      email  462
1   facebook  823
2     google  543
3    twitter  415
4      yahoo  757
'''
click_source_by_month = user_visits.groupby(["utm_source","month"])["id"].count().reset_index()
print(click_source_by_month)
'''   utm_source         month   id
0       email   1 - January   43
1       email  2 - February  147
2       email     3 - March  272
3    facebook   1 - January  404
4    facebook  2 - February  263
5    facebook     3 - March  156
6      google   1 - January  127
*partial*
'''
click_source_by_month_pivot = click_source_by_month.pivot(columns="month",index="utm_source", values="id").reset_index()
print(click_source_by_month_pivot)
'''
month utm_source  1 - January  2 - February  3 - March
0          email           43           147        272
1       facebook          404           263        156
2         google          127           196        220
3        twitter          164           154         97
4          yahoo          262           240        255
'''

#Aggregates in Pandas Multiple Choice Quiz
'''
Consider the DataFrame, sports_store, shown below, that gives the prices of various sports equipment sold at a local retail store. What command would you run if you wanted to find the average price of the items sold by this store?  sports_store.price.mean()
You are working for an online retailer of mechanical keyboards and have access to the customer_purchases DataFrame. In this DataFrame there is a row for each purchase a customer has made on the site. If the customers' names are stored in a column called name, what command would you use to determine how many unique customers purchase something from the site?  customer_purchases.name.nunique()
A movie review website employs several different critics. They store these critics' movie ratings in a DataFrame called movie_ratings, which has three columns: critic, movie, and rating. What command would give the average rating for each movie?  movie_ratings.groupby('movie').rating.mean()
A movie review website employs several different critics. They store these critics' movie ratings in a DataFrame called movie_ratings, which has three columns: critic, movie, and rating. The following code gives the max rating of each critic. What type of object is the output of this code?  movie_ratings.groupby('critic').rating.max().reset_index()  DataFrame.  Because reset_index() is added onto this line of code, the resulting object is a DataFrame with two columns: critic and rating, where rating is their max rating.
The City Library has several branches throughout the area. They collect all of their book checkout data in a DataFrame called checkouts. The DataFrame contains the columns 'location', 'date', and 'book_title'. If we want to compare the total number of books checked out at each branch, what code could we use?  checkouts.groupby(['location']).book_title.count().reset_index()
Consider the following two tables below. The first shows the ratings each critic gave to three different movies, and the second shows a pivoted version of the table that makes it easier to compare each critic's ratings for a single movie. Which of the following commands was used to achieve this pivot?  movie_review_pivot = movie_ratings.pivot(columns = 'movie', index = 'critic', values ='rating')
'''

#A/B Testing for ShoeFly.com Freeform Project
#ShoeFly.com is performing an A/B Test. They have two different versions of an ad, which they have placed in emails, as well as in banner ads on Facebook, Twitter, and Google. They want to know how the two ads are performing on each of the different platforms on each day of the week. Help them analyze the data using aggregate measures.
ad_clicks = pd.read_csv("ad_clicks.csv")
viewcount = ad_clicks.groupby("utm_source").user_id.count() #count view by utm_source
print(viewcount)
'''
utm_source
email       255
facebook    504
google      680
twitter     215
Name: user_id, dtype: int64
'''
ad_clicks["is_click"] = ad_clicks.apply(lambda x: "False" if x["ad_click_timestamp"] == "noclick" else "True", axis=1) #insert column or new column is_click False if ad_click_timestamp is noclick
clicks_by_source = ad_clicks.groupby(["utm_source","is_click"]).user_id.count().reset_index() # gruop by utm_source and is_click to count  the number of user_id's
print(clicks_by_source)
'''
  utm_source is_click  user_id
0      email    False      175
1      email     True       80
2   facebook    False      324
3   facebook     True      180
4     google    False      441
5     google     True      239
6    twitter    False      149
7    twitter     True       66
'''
clicks_pivot = clicks_by_source.pivot(columns="is_click", index="utm_source", values="user_id").reset_index() #pivot table clicks_by_source
print(clicks_pivot)
'''
is_click utm_source  False  True
0             email    175    80
1          facebook    324   180
2            google    441   239
3           twitter    149    66
'''
#insert new column in pivot table or pivot table new column
#clicks_pivot["percent_clicked"] = clicks_pivot.apply(lambda x: "True", axis=1)
#print(clicks_pivot)
'''
is_click utm_source  False  True percent_clicked
0             email    175    80            True
1          facebook    324   180            True
2            google    441   239            True
3           twitter    149    66            True
'''
clicks_pivot["percent_clicked"] = clicks_pivot["True"]/(clicks_pivot["True"]+clicks_pivot["False"]) #insert column to calculate percentage of utm_source clicks are True; e.g. email 80/(175+80)
print(clicks_pivot)
'''
is_click utm_source  False  True  percent_clicked
0             email    175    80         0.313725
1          facebook    324   180         0.357143
2            google    441   239         0.351471
3           twitter    149    66         0.306977
'''
adsshown = ad_clicks.groupby(["experimental_group","is_click"]).user_id.count().reset_index() #count number of ads clicked grouped by ad A or ad B and is_click True or False
print(adsshown)
'''
  experimental_group is_click  user_id
0                  A    False      517
1                  A     True      310
2                  B    False      572
3                  B     True      255
'''
adsshownpivot = adsshown.pivot(columns="is_click", index="experimental_group", values="user_id").reset_index() #create pivot table
print(adsshownpivot)
'''
is_click experimental_group  False  True
0                         A    517   310
1                         B    572   255
'''
adsshownpivot["percentagetrue"] = adsshownpivot["True"]/(adsshownpivot["True"]+adsshownpivot["False"]) #add column pivot table column calculate actual clicks ad A and ad B; e.g. ad A 310/(310+510)
print(adsshownpivot)
'''
is_click experimental_group  False  True  percentagetrue
0                         A    517   310        0.374849
1                         B    572   255        0.308343
'''
a_clicks = ad_clicks[ad_clicks.experimental_group=="A"] #get all rows experiment_group is A save to variable a_clicks
a_clicksgroup = a_clicks.groupby(["experimental_group","day"]).user_id.count().reset_index() #group a_clicks by experiment and by day.  RM:  group by experiment needed for pivot table.
print(a_clicksgroup)
'''
  experimental_group            day  user_id
0                  A     1 - Monday      113
1                  A    2 - Tuesday      119
2                  A  3 - Wednesday      124
3                  A   4 - Thursday      116
4                  A     5 - Friday      128
5                  A   6 - Saturday      118
6                  A     7 - Sunday      109

'''
a_clicksgroupsum = a_clicksgroup.user_id.sum() #calculate the sum of user_ids from a_clicksgroup
print(a_clicksgroupsum) #print 827
a_clicksgrouppivot = a_clicksgroup.pivot(columns="experimental_group", index="day",values="user_id").reset_index()
print(a_clicksgrouppivot)
'''
experimental_group            day    A
0                      1 - Monday  113
1                     2 - Tuesday  119
2                   3 - Wednesday  124
3                    4 - Thursday  116
4                      5 - Friday  128
5                    6 - Saturday  118
6                      7 - Sunday  109
'''
a_clicksgrouppivot["percentage"] = a_clicksgrouppivot["A"]/a_clicksgroupsum #add column percentage to calculate percentage each day over total clicks ad A
print(a_clicksgrouppivot)
'''
experimental_group            day    A  percentage
0                      1 - Monday  113    0.136638
1                     2 - Tuesday  119    0.143894
2                   3 - Wednesday  124    0.149940
3                    4 - Thursday  116    0.140266
4                      5 - Friday  128    0.154776
5                    6 - Saturday  118    0.142684
6                      7 - Sunday  109    0.131802
'''
ab_clicksgroup = ad_clicks.groupby(["experimental_group","day"]).user_id.count().reset_index()
print(ab_clicksgroup)
ab_clicksgroupsum = ab_clicksgroup.user_id.sum() #calculate the sum of user_ids from ab_clicksgroup
print(ab_clicksgroupsum) #print 1654
ab_clicksgrouppivot = ab_clicksgroup.pivot(columns="experimental_group", index="day",values="user_id").reset_index()
ab_clicksgrouppivot["percentage"] = (ab_clicksgrouppivot["A"]+ab_clicksgrouppivot["B"])/ab_clicksgroupsum #add column percentage to calculate percentage each day over total clicks ad A
print(ab_clicksgrouppivot)
'''
experimental_group            day    A    B  percentage
0                      1 - Monday  113  113    0.136638
1                     2 - Tuesday  119  119    0.143894
2                   3 - Wednesday  124  124    0.149940
3                    4 - Thursday  116  116    0.140266
4                      5 - Friday  128  128    0.154776
5                    6 - Saturday  118  118    0.142684
6                      7 - Sunday  109  109    0.131802
'''