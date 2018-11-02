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



'''