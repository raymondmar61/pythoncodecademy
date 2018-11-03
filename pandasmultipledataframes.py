import pandas as pd
import numpy as np

#Working with Multiple DataFrames Interactive Lesson
#Pandas can efficiently merge tables use the .merge method.  The .merge method looks for columns that are common between two DataFrames and then looks for rows where those column's values are the same. It then combines the matching rows into a single row in a new table.  e.g. new_df = pd.merge(orders, customers)

dfsales = pd.DataFrame([["January",300],["February",290],["March",310],["April",325],["May",475],["June",495]],columns=["Month","Revenue"])
dftargets = pd.DataFrame([["January",310],["February",270],["March",300],["April",350],["May",475],["June",500]],columns=["Month","Target"])
sales_vs_target = pd.merge(dfsales, dftargets) #RM:  if the column names are the same for dfsales and dftargets Month and Revenue, then pd.merge(dfsales, dftargets) returns May 475
print(sales_vs_target)
'''      
      Month  Revenue  Target
0   January      300      310
1  February      290      270
2     March      310      300
3     April      325      350
4       May      475      475
5      June      495      500
'''
crushing_it = sales_vs_target[sales_vs_target.Revenue > sales_vs_target.Target] #find rows revenue greater than target save to variable crushing_it
print(crushing_it)
'''
      Month  Revenue  Target
1  February      290     270
2     March      310     300
'''
#Each DataFrame has its own merge method. For instance, if you wanted to merge orders with customers, you could use:  new_df = orders.merge(customers).  This produces the same DataFrame as if we had called pd.merge(orders, customers).
#We generally use this when we are joining more than two DataFrames together because we can "chain" the commands. The following command would merge orders to customers, and then the resulting DataFrame to products: big_df = orders.merge(customers).merge(products)
#.merge function "knew" how to combine tables based on the columns that were the same between two tables. For instance, products and orders both had a column called product_id.
newsalesvstarget = dfsales.merge(dftargets)
print(newsalesvstarget)
'''
      Month  Revenue  Target
0   January      300     310
1  February      290     270
2     March      310     300
3     April      325     350
4       May      475     475
5      June      495     500
'''
dfmenwomensales = pd.DataFrame([["January",30,35],["February",29,35],["March",31,29],["April",32,28],["May",47,50],["June",49,45]],columns=["Month","Men","Women"])
print(dfmenwomensales)
'''
      Month  Men  Women
0   January   30     35
1  February   29     35
2     March   31     29
3     April   32     28
4       May   47     50
5      June   49     45
'''
all_data = dfsales.merge(dftargets).merge(dfmenwomensales)
print(all_data)
'''      Month  Revenue  Target  Men  Women
0   January      300     310   30     35
1  February      290     270   29     35
2     March      310     300   31     29
3     April      325     350   32     28
4       May      475     475   47     50
5      June      495     500   49     45
'''
results = all_data[(all_data.Revenue > all_data.Target) & (all_data.Women > all_data.Men)] #get rows Revenue greater than Target and Woem greater than Men
print(results)
'''      Month  Revenue  Target  Men  Women
1  February      290     270   29     35
'''
#The column "id" in orders table or ordersdf.csv and in customers table or customersdf.csv are different.  The default merges are wrong.  RM:  id column in orders is order_id.  id column in customers is customero_id.  Different id column name.
#We solve the problem  use .rename to rename the columns for our merges. We rename the column id to customer_id, so that orders and customers have a common column for the merge.  pd.merge(orders, customers.rename(columns={'id': 'customer_id'}))
#Use .rename to merge two DataFrames whose columns don't match.
orders = pd.read_csv('ordersdf.csv')
products = pd.read_csv('productsdf.csv')
orders_products = pd.merge(products.rename(columns={"id55":"product_id"}), orders.rename(columns={"id55":"product_id"}))  #RM:  link products table product_id and orders table product_id as id55?
#official solution: orders_products = pd.merge(orders, products.rename(columns={'id':'product_id'}))
#orders_products = pd.merge(orders, products) #RM:  it appears .rename was unnecessary for my tables.  Codecademy must have changed the column names for the specific exercise.
print(orders_products)
'''
   product_id         description     ...      quantity   timestamp
0           1      thing-a-ma-jig     ...             1  2017-01-01
1           1      thing-a-ma-jig     ...             1  2017-02-02
2           2  whatcha-ma-call-it     ...             3  2017-01-01
3           2  whatcha-ma-call-it     ...             2  2017-02-01
4           3          doo-hickey     ...             1  2017-01-01
5           3          doo-hickey     ...             3  2017-02-01
6           4               gizmo     ...             2  2017-03-01
7           4               gizmo     ...             1  2017-02-02

[8 rows x 7 columns]
'''
#We could use the keywords left_on and right_on to specify which columns we want to perform the merge on.  RM:  another way to merge two dataframes or two tables.
#In the example below, the "left" table is the one that comes first (orders), and the "right" table is the one that comes second (customers). This syntax says that we should match the customer_id from orders to the id in customers.  pd.merge(orders, customers, left_on='customer_id', right_on='id').  RM:  better than .rename.
#If we use this syntax, we'll end up with two columns called id, one from the first table and one from the second. Pandas won't let you have two columns with the same name, so it will change them to id_x and id_y.
#Use the keyword suffixes. We can provide a list of suffixes to use instead of "_x" and "_y".  pd.merge(orders, customers, left_on='customer_id', right_on='id', suffixes=['_order', customer'])
orders_productsleftright = pd.merge(orders, products, left_on="product_id", right_on="product_id", suffixes=["_orders","_products"])
#solution orders_products = pd.merge(orders, products, left_on="product_id", right_on="id", suffixes=["_orders","_products"]) #RM:  Codecademy changed the column name on products table from product_id to id.
print(orders_productsleftright)
'''
   order_id  customer_id  ...           description  price
0         1            2  ...            doo-hickey      7
1         5            3  ...            doo-hickey      7
2         2            2  ...    whatcha-ma-call-it     10
3         4            3  ...    whatcha-ma-call-it     10
4         3            3  ...        thing-a-ma-jig      5
5         7            1  ...        thing-a-ma-jig      5
6         6            1  ...                 gizmo      3
7         8            1  ...                 gizmo      3

[8 rows x 7 columns]
'''
orders_productsleftright.to_csv('tempdelete.csv') #save orders_products to tempdelete.csv
#If we wanted to combine the data from [tables where data is] missing from one of the tables, we could use an Outer Join. An Outer Join would include all rows from both tables, even if they don't match. Any missing values are filled in with None or nan (which stands for "Not a Number").  pd.merge(company_a, company_b, how='outer') #RM:  not left outer join or right outer join, yet
store_a = pd.DataFrame([["hammer",12],["screwdriver",15],["nails",200],["screws",350],["saw",6],["duct tape",150],["wrench",12],["pvc pipe",54]], columns=["item","store_a_inventory"])
store_b = pd.DataFrame([["hammer",6],["nails",250],["saw",6],["duct tape",150],["pvc pipe",54],["rake",10],["shovel",15],["wooden dowels",192]], columns=["item","store_b_inventory"])
store_a_b_outer = pd.merge(store_a, store_b, how="outer")
print(store_a_b_outer)
'''
             item  store_a_inventory  store_b_inventory
0          hammer               12.0                6.0
1     screwdriver               15.0                NaN
2           nails              200.0              250.0
3          screws              350.0                NaN
4             saw                6.0                6.0
5       duct tape              150.0              150.0
6          wrench               12.0                NaN
7        pvc pipe               54.0               54.0
8            rake                NaN               10.0
9          shovel                NaN               15.0
10  wooden dowels                NaN              192.0
'''
#left merge we get all customers from Company A, and only customers from Company B who are also customers of Company A. pd.merge(company_a, company_b, how='left')
#right merge we get all customers from Company B, and only customers from Company A who are also customers of Company B. pd.merge(company_a, company_b, how="right")
store_a_b_left = pd.merge(store_a, store_b, how="left")
print(store_a_b_left)
'''
          item  store_a_inventory  store_b_inventory
0       hammer                 12                6.0
1  screwdriver                 15                NaN
2        nails                200              250.0
3       screws                350                NaN
4          saw                  6                6.0
5    duct tape                150              150.0
6       wrench                 12                NaN
7     pvc pipe                 54               54.0
'''
store_b_a_left = pd.merge(store_b, store_a, how="left")
print(store_b_a_left)
'''
            item  store_b_inventory  store_a_inventory
0         hammer                  6               12.0
1          nails                250              200.0
2            saw                  6                6.0
3      duct tape                150              150.0
4       pvc pipe                 54               54.0
5           rake                 10                NaN
6         shovel                 15                NaN
7  wooden dowels                192                NaN
'''
#When we need to reconstruct a single DataFrame from multiple smaller DataFrames, we can use the method pd.concat([df1, df2, df2, ...]). This method only works if all of the columns are the same in all of the DataFrames.  pd.concat([df1, df2]).  df1 and df2 have two columns name and email.
bakery = pd.DataFrame([["cookie",2.5], ["brownie",3.5], ["slice of cake",4.75], ["slice of cheesecake",4.75], ["slice of pie",5]], columns=["item","price"])
ice_cream = pd.DataFrame([["scoop of chocolate ice cream",3], ["scoop of vanilla ice cream",2.95], ["scoop of strawberry ice cream",3.05], ["scoop of cookie dough ice cream",3.25]], columns=["item","price"])
menu = pd.concat([bakery, ice_cream])
print(menu)
'''
                              item  price
0                           cookie   2.50
1                          brownie   3.50
2                    slice of cake   4.75
3              slice of cheesecake   4.75
4                     slice of pie   5.00
0     scoop of chocolate ice cream   3.00
1       scoop of vanilla ice cream   2.95
2    scoop of strawberry ice cream   3.05
3  scoop of cookie dough ice cream   3.25
'''

#Working with Multiple DataFrames Quiz
'''
Which of the following best describes an inner merge?  A merge where only matching rows are included.  A merge where all rows are included, whether they match or not is an outer merge.
What is the correct syntax for performing an outer merge on two Dataframes: df_one and df_two?  merged_df = pd.merge(df_one, df_two, how = 'outer'
A veterinarians office is run by two vets, Greg and Susan, and stores each of their appointment data in separate DataFrames, called greg_appointments and susan_appointments respectively. These DataFrames have the same columns. If the vet office wanted to combine the two DataFrames into a single DataFrame called appointments_all which of the following commands would they use?  appointments_all = pd.concat([greg_appointments, susan_appointments])
A veterinarian's office stores all of their data on pets and their owners in two dataframes: pets and owners. The owners dataframe has the columns 'id', 'first_name', 'last_name' and 'address'. The 'pets' dataframe has the columns id, name, owner_id, and type. If the office wanted to combine the two dataframes into one dataframe called pets_owers, what following code could work?  pets_owners = pd.merge(pets,owners.rename(columns = {'id':'owner_id'}))
Which of the following best describes an outer merge?  A merge where all rows are included, whether they match or not.
Which of the following best describes a left merge?  A merge where all rows from the first Dataframe are included, but only matching rows from the second Dataframe.
Consider the following two Dataframes vets and appointments that store the appointment and vet data for a veterinarians office. Notice that some vets do not have any appointments scheduled, and some appointments do not yet have a vet assigned. If we wanted to combine the DataFrames into completed_appointments and only show the appointments that have had vets assigned to them, what code could we use?  completed_appointments = pd.merge(vets.rename(columns = {'id':'doctor_id'}), appointments, how = 'inner')
'''

#Page Visits Funnel Freeform Project
#A funnel is a description of how many people continue to the next step of a multi-step process.  In this case, buying online.
#RM:  data is crap.  Brain is fried 11/03/18 1430hrs.
#How long is your merged DataFrame?  Use len.
#print(len(visitscart))
#How many of the timestamps are null for the column cart_time?
#cart_time_null_count = cart[cart.cart_time.isnull()].count().reset_index()
#print(cart_time_null_count)