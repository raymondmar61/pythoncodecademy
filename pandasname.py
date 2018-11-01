#https://www.codecademy.com/learn/data-processing-pandas
#Pandas is a Python module for working with tabular data (i.e., data in a table with rows and columns). Tabular data has a lot of the same functionality as SQL or Excel, but Pandas adds the power of Python.  After learning Pandas, you’ll be able to ingest, clean, and aggregate large quantities of data, and then use that data with other Python modules like Scipy (for statistical analysis) or Matplotlib (for visualization).

#Creating, Loading, and Selecting Data with Pandas Interactive Lesson
import pandas as pd
#df = pd.read_csv(filename.csv) #load csv data into Pandas.  Variable df is data frame.
#df.to_csv('filename.csv') #saves csv data
#print(df.head(10)) #print first 10 rows.  df.head() default is five rows.
#print(df[(df.shoe_type == 'sandals') & (df.shoe_color == 'black')]) #prints black sandals rows
#print(df[(df.first_name == 'Susan') & (df.last_name == 'Dennis')]) #print Susan Dennis orders rows
dfgeneric = pd.DataFrame({"column1":[1, 2, 3, 4],"column2":[2, 4, 6, 8],"column3":[3, 6, 9, 12]})
print(dfgeneric)
'''
   column1  column2  column3
0        1        2        3
1        2        4        6
2        3        6        9
3        4        8       12
'''
print(dfgeneric.head(2))
'''
   column1  column2  column3
0        1        2        3
1        2        4        6
'''
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4], "Product Name": ["t-shirt","t-shirt","skirt","skirt"], "Color":["blue","green","red","black"]})
print(df1)
#You can pass in a list of lists, where each one represents a row of data. Use the keyword argument columns to pass a list of column names.
df2 = pd.DataFrame([[1, 'San Diego', 100],[2, 'Los Angeles', 120],[3, "San Francisco",90],[4,"Sacramento",115]],columns=["Store ID","Location","Number of Employees"])
print(df2)
'''
   Store ID       Location  Number of Employees
0         1      San Diego                  100
1         2    Los Angeles                  120
2         3  San Francisco                   90
3         4     Sacramento                  115
'''
df = pd.read_csv("cupcakes.csv")
print(df)
print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 4 columns):
name               3 non-null object
cake_flavor        3 non-null object
frosting_flavor    3 non-null object
topping            3 non-null object
dtypes: object(4)
memory usage: 176.0+ bytes
None
'''
print(df["cake_flavor"])
'''
0    chocolate
1      vanilla
2       carrot
Name: cake_flavor, dtype: object
'''
topping = df["topping"]
print(topping)
'''
0    chocolate shavings
1     rainbow sprinkles
2               almonds
Name: topping, dtype: object
'''
print(type(topping)) #print <class 'pandas.core.series.Series'>.  When we select a single column, the result is called a Series.
selecttwocolumns = df[["cake_flavor","frosting_flavor"]]
print(selecttwocolumns)
'''
  cake_flavor frosting_flavor
0   chocolate       chocolate
1     vanilla         vanilla
2      carrot    cream cheese
'''
print(type(selecttwocolumns)) #print <class 'pandas.core.frame.DataFrame'>
print(df.iloc[2]) #print the third row Carrot Cake.  DataFrames are zero-indexed.  Row one is index zero.
'''
name                Carrot Cake
cake_flavor              carrot
frosting_flavor    cream cheese
topping                 almonds
Name: 2, dtype: object
'''
#RM:  selecting rows using .iloc[] is like selecting items from a list.
firstrowsecondrow = df.iloc[0:2]
print(firstrowsecondrow) #print first row and second row
'''
            name         ...                     topping
0   Devil's Food         ...          chocolate shavings
1  Birthday Cake         ...           rainbow sprinkles

[2 rows x 4 columns]
'''
dfgradebook = pd.read_csv("gradebook.csv")
grade90 = dfgradebook[dfgradebook.grade >= 90] #get rows grade column data 90 and greater
print(grade90)
'''
   PRIKEY student assignment_name  grade
2       2     Bob    Assignment 1     99
3       3     Bob    Assignment 2     90
8       8   Ellie    Assignment 1     91
'''
print(dfgradebook[(dfgradebook.grade >=90) & (dfgradebook.assignment_name == "Assignment 1")]) #get rows grade column data 90 and greater and Assignment 1
'''
   PRIKEY student assignment_name  grade
2       2     Bob    Assignment 1     99
8       8   Ellie    Assignment 1     91
'''
amybobdan = dfgradebook[dfgradebook.student.isin(["Amy","Bob","Dan"])]
print(amybobdan)
'''
   PRIKEY student assignment_name  grade
0       0     Amy    Assignment 1     75
1       1     Amy    Assignment 2     82
2       2     Bob    Assignment 1     99
3       3     Bob    Assignment 2     90
6       6     Dan    Assignment 1     88
7       7     Dan    Assignment 2     82
'''
#When we select a subset of a DataFrame using logic, we end up with non-consecutive indices.  We can fix this using the method .reset_index()
print(amybobdan.reset_index())
'''
   index  PRIKEY student assignment_name  grade
0      0       0     Amy    Assignment 1     75
1      1       1     Amy    Assignment 2     82
2      2       2     Bob    Assignment 1     99
3      3       3     Bob    Assignment 2     90
4      6       6     Dan    Assignment 1     88
5      7       7     Dan    Assignment 2     82
'''
print(amybobdan.reset_index(drop=True)) #the old indices have been moved into a new column called 'index'. Unless you need those values for something special, it's probably better to use the keyword drop=True so that you don't end up with that extra column.
'''
   PRIKEY student assignment_name  grade
0       0     Amy    Assignment 1     75
1       1     Amy    Assignment 2     82
2       2     Bob    Assignment 1     99
3       3     Bob    Assignment 2     90
4       6     Dan    Assignment 1     88
5       7     Dan    Assignment 2     82
'''
#same as
amybobdanresetindex = dfgradebook[dfgradebook.student.isin(["Amy","Bob","Dan"])].reset_index(drop=True)
print(amybobdanresetindex)
'''
   PRIKEY student assignment_name  grade
0       0     Amy    Assignment 1     75
1       1     Amy    Assignment 2     82
2       2     Bob    Assignment 1     99
3       3     Bob    Assignment 2     90
4       6     Dan    Assignment 1     88
5       7     Dan    Assignment 2     82
'''

orders = pd.read_csv("shoefly.csv")
print(orders.head(5))
emails = orders["email"] #select column email get all data under email column
frances_palmer = orders[(orders.first_name=="Frances") & (orders.last_name=="Palmer")] #get all rows from first name Frances and last name Palmer
comfy_shoes = orders[orders.shoe_type.isin(["clogs","boots","ballet flats"])] #get all rows shoes are clogs, boots, or ballet flats