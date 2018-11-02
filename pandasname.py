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
print(df2[df2.Location=="San Francisco"])
'''
   Store ID       Location  Number of Employees
2         3  San Francisco                   90
'''
numberofemployees = df2["Number of Employees"]
print(numberofemployees)
#print(df2["Number of Employees"]) #also works
'''
0    100
1    120
2     90
3    115
Name: Number of Employees, dtype: int64
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
print(orders.head(5)) #print first 5 rows shoefly.csv
emails = orders["email"] #select column email get all data under email column
frances_palmer = orders[(orders.first_name=="Frances") & (orders.last_name=="Palmer")] #get all rows from first name Frances and last name Palmer
comfy_shoes = orders[orders.shoe_type.isin(["clogs","boots","ballet flats"])] #get all rows shoes are clogs, boots, or ballet flats

#Creating, Loading, and Selecting Data with Pandas Multiple Choice Quiz
'''
Consider the following code that is intended to create a new DataFrame showing the grades of students in a class. Will this code create a valid DataFrame? If not, why?
grades = pd.DataFrame({'name': ['Chloe', 'Grace', 'Jeremy', 'Isla'], 'unit_1_grade': [95, 82, 83, 75], 'unit_2_grade': [91, 74, 89, 84], 'Grade for the Year': [93, 78, 86] })  The code will not run because Grade for the Year has fewer elements than the other columns.
Which of the following commands will print the first 5 rows (not including the header) of the DataFrame df?  print(df.head(5))
If we have the following initial DataFrame (shown below) and we want to reset the indices and overwrite the DataFrame to obtain the final DataFrame (shown below), what line of code would we use?
If we have the following initial DataFrame (shown below) and we want to reset the indices and overwrite the DataFrame to obtain the final DataFrame (shown below), what line of code would we use?  df.reset_index(inplace=True, drop=True)
Which of the following commands will correctly import the csv content_inventory.csv into the DataFrame content?  content = pd.read_csv('content_inventory.csv')
You're doing some analytics on the ages of the typical customer for a company. They give you the following DataFrame. If you want to ignore all of the PII (personal identifying information) and only select the ages from the DataFrame, which of the follow lines of code would you use?  customers.age.  RM:  the DataFrame is a list of lists.
If you wanted to select the row including all of the data for the month of May, which of the following lines of code would you use?  clinic_df[clinic_df.month == 'May']
'''

#Modifying DataFrames Interactive Lesson
#df = pd.read_csv('shoefly_messy_orders.csv')
#df['columnname'] = df.columnname.apply(string.lower) converts data to lowercase #RM doesn't work on my Python
#df['newcolumnname'] =  df.columnnameappliedlogic.apply(lambda x: False if x == 'fabric' else True) #add a column newcolumnname, which is True for all non-fabric shoes and False for fabric shoes in columnnameappliedlogic.
#df['newcolumnname'] = df.apply(lambda row: "{} {} bought {} {} {}".format(row.first_name, row.last_name, row.shoe_color, row.shoe_material, row.shoe_type), axis=1) #print row.first_name row.last_name bought row.shoe_color row.shoe_material row.shoe_type.
df = pd.DataFrame([[1, '3 inch screw', 0.5, 0.75], [2, '2 inch nail', 0.10, 0.25], [3, 'hammer', 3.00, 5.50], [4, 'screwdriver', 2.50, 3.00]], columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price'])
df['Sold in Bulk?'] = ["Yes","Yes","No","No"] #add column Sold in Bulk and its data
df["Is taxed?"] = "Yes" #add column Is taxed? same data Yes
df["Revenue"] = df.Price - df["Cost to Manufacture"] #add column Revenue populate Price - Cost to Manufacture.  RM:  no period when column name specified with brackets
print(df)
'''
   Product ID   Description   ...     Is taxed?  Revenue
0           1  3 inch screw   ...           Yes     0.25
1           2   2 inch nail   ...           Yes     0.15
2           3        hammer   ...           Yes     2.50
3           4   screwdriver   ...           Yes     0.50
[4 rows x 7 columns]
'''
df = pd.DataFrame([['JOHN SMITH', 'john.smith@gmail.com'], ['Jane Doe', 'jdoe@yahoo.com'], ['joe schmo', 'joeschmo@hotmail.com']],columns=['Name', 'Email'])
df["Lowercase Name"] = df["Name"].str.lower() #create column Lowercase Name convert Name all lower case
#In Pandas, we often use lambda functions to perform complex operations on columns.  RM:  I created a quick crash course and review lambdafunction.py in Outside The Book.
df["Email Provider Lambda"] = df["Email"].apply(lambda getemailprovider: getemailprovider.split("@")[-1])
df["Email Provider No Lambda"] = df["Email"].str.split("@").str[-1] #source: https://stackoverflow.com/questions/43876961/using-pandas-str-find-method-to-slice-strings-in-dataframe-column.  https://pandas.pydata.org/pandas-docs/stable/text.html
df['last_name lambda'] = df.Name.apply(lambda get_last_name: get_last_name.split(" ")[-1])
df["last name no lambda"] = df["Name"].str.split(" ").str[-1]
#df["Email Provider"] = df["Email"].str[5:] #source: https://stackoverflow.com/questions/25789445/pandas-make-new-column-from-string-slice-of-another-column
#We can also operate on multiple columns at once. If we use apply without specifying a single column and add the argument axis=1, the input to our lambda function will be an entire row, not a column. To access particular values of the row, we use the syntax row.column_name or row[‘column_name’].
print(df)
'''
         Name         ...         last name no lambda
0  JOHN SMITH         ...                       SMITH
1    Jane Doe         ...                         Doe
2   joe schmo         ...                       schmo

[3 rows x 7 columns]
'''
employeesdf = pd.read_csv("employees.csv")
employeesdf["total_earned"] = employeesdf["hourly_wage"] * employeesdf["hours_worked"]
employeesdf["total_earned lambda"] = employeesdf.apply(lambda x: (x["hourly_wage"] * x["hours_worked"] + (((x["hours_worked"])-40)*1.5*x["hourly_wage"])) if x["hours_worked"] > 40 else x["hourly_wage"] * x["hours_worked"], axis=1)
print(employeesdf["total_earned lambda"])
'''
0      902.5
1      680.0
2      480.0
3     1035.0
4      418.0
5      546.0
6      600.0
7      480.0
8      630.0
9      850.0
10     448.0
11     400.0
12     429.0
13     608.0
14     840.0
15     630.0
16     660.0
17     456.0
18     740.0
19     812.5
Name: total_earned lambda, dtype: float64
'''
#You can change all of the column names at once by setting the .columns property to a different list.  For example, we might want all of the column names to follow variable name rules, so that we can use df.column_name (which tab-completes) rather than df['column_name'] (which takes up extra space).  RM:  rename a column Complete Name to Complete_Name for df["Complete Name"] to df.Complete_Name.
imdbdf = pd.read_csv("imdb.csv")
imdbdf.columns = ["ID","Title","Category","Year Released","Rating"] #rename columns, edit column name.  Old column names: id, name, genre, year, imdb_rating
print(imdbdf.head(2))
'''   ID           Title Category  Year Released  Rating
0   1          Avatar   action           2009     7.9
1   2  Jurassic World   action           2015     7.3
'''
#You also can rename individual columns by using the .rename method. Pass a dictionary like the one below to the columns keyword argument:  df.rename(columns={'old_column_name1': 'old_column_name1', 'old_column_name2': 'new_column_name2'},inplace=True).  The code renames old_column_name1 to old_column_name1 and old_column_name2 to new_column_name2.
#Using .rename with only the columns keyword will create a new DataFrame, leaving your original DataFrame unchanged. That's why we also passed in the keyword argument inplace=True. Using inplace=True lets us edit the original DataFrame.
#.rename can rename just one column and be specific which column names are changed.
imdbdf.rename(columns={"Title":"movie_title"}, inplace=True)
print(imdbdf.head(2))
'''
   ID     movie_title Category  Year Released  Rating
0   1          Avatar   action           2009     7.9
1   2  Jurassic World   action           2015     7.3
'''
orders = pd.read_csv('shoefly.csv')
print(orders.head(5))
orders["shoe_source"] = orders.apply(lambda x: "vegan" if x["shoe_material"] != "leather" else "animal", axis=1)
orders["salutation"] = orders.apply(lambda y: ("{}{}".format("Dear Ms. ",y["last_name"])) if y["gender"] == "female" else ("{}{}".format("Dear Mr. ",y["last_name"])), axis=1)
print(orders)
'''
      id first_name        ...         shoe_source         salutation
0  54791    Rebecca        ...               vegan   Dear Ms. Lindsay
1  53450      Emily        ...               vegan     Dear Ms. Joyce
2  91987      Joyce        ...               vegan    Dear Ms. Waller
3  14437     Justin        ...               vegan  Dear Mr. Erickson
4  79357     Andrew        ...              animal     Dear Mr. Banks
[5 rows x 10 columns]
'''

#Modifying DataFrames Multiple Choice Quiz
'''
The following lambda function is intended to take the age of a visitor to a website and check if they are over 13 years old. If they are, the function should welcome them to the site, if they are not it should tell them so. Will this lambda function work? If not, why not?  age_check = lambda x: 'Welcome to the site!' if age > 13 else 'Sorry you are too young to enter this site.'  This code will not work because the lambda function takes an input of x but the if statement checks against the value of age.
Consider the following lambda function. What would be the output of mylambda(4)? (Hint: in Python ** means exponent) mylambda = lambda x: x**2 + 3*x if x > 7 else 2*x - 10. -2
The DataFrame attendance is shown below and counts the number of days a student has been absent. If a student has been absent for more than 10 days we want to call their parents. How would we add a column with 'Yes' if a student has been absent more than 10 days and 'No' if not?  attendance['call_parents'] = attendance.apply(lambda row: 'Yes' if row['days_absent'] > 10 else 'No', axis=1)
Read through the following block of code. How many columns does the resulting DataFrame customers contain (not including the index)?  customers = pd.DataFrame([['Annie Hall', 'anniehall@snailmail.com', '201-555-0213'], ['Geoffrey Adams', 'gadams@yahee.com', '622-555-0994'], ['Casey Flanders', 'flandersc@netscope.com', '413-555-9431'], ['Hiroshi Tanaka', 'hiroshit@snailmail.com', '718-555-1985'], ['Sam Waterson', 'waterboy@hitmail.com', '594-555-8321']], columns = ['name', 'email', 'phone_number']) customers['purchase_volume'] = [20, 6, 15, 9, 11] customers['area_code'] = customers.phone_number.apply(lambda x: x.split('-')[0])  5.  The initial definition of customers contains 3 columns. Then customers['purchase_volume'] and customers['area_code'] both add an additional column, bringing the total number of columns up to 5.
Consider the following DataFrame showing the daily inventory and amount of products sold of a local office supply store. You want to add a column to this DataFrame to determine how many of each item is remaining at the end of the day. Which of the following lines of code would accomplish this?  office_supply_store['remaining_inventory'] = office_supply_store.initial_inventory - office_supply_store.number_sold
The DataFrame below shows a set of student grades for 3 units in a Biology course. Unfortunately, the unit names are not descriptive and the student names are simply stored in a column called id. Which of the following commands will change the names of the columns to the following: id -> Name, unit_1 -> Ecology, unit_2 -> Cells, unit_3 -> Genetics.  grades = grades.rename(columns={'id': 'Name','unit_1': 'Ecology','unit_2': 'Cells','unit_3': 'Genetics'})
'''

#Petal Power Inventory Freeform Project
inventory = pd.read_csv("inventory.csv")
print(inventory.head(10)) #print first 10 rows
stanten_island = inventory[inventory.location=="Staten Island"] #save all Staten Island rows to variable stanten_island
product_request = stanten_island["product_type"] #save column product_type to variable product_request
seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type =="seeds")] #save rows location is Brooklyn and product_type is seeds to variable seed_request.  RM:  there are no rows.
inventory["in_stock"] = inventory.apply(lambda x: "True" if x["quantity"] > 0 else "False", axis=1) #insert column or new column in_stock populate True if quantity greater than zero otherwise False
inventory["total_value"] = inventory.price * inventory.quantity #insert column total_value multiplying current inventory value
combine_lambda = lambda row: "{} - {}".format(row.product_type,row.product_description)
inventory["full_description"] = inventory.apply(combine_lambda, axis=1) #insert column full_description combinining columns product_type and product_description from combine_lambda variable
print(inventory.head(5))
'''
        location             ...                        full_description
0  Staten Island             ...                           seeds - daisy
1  Staten Island             ...                      seeds - calla lily
2  Staten Island             ...                          seeds - tomato
3  Staten Island             ...                     garden tools - rake
4  Staten Island             ...              garden tools - wheelbarrow
[5 rows x 8 columns]
'''
