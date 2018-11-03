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
#The column "id" in orders table or ordersdf.csv and in customers table or customersdf.csv are different.  The default merges are wrong.
#We solve the problem  use .rename to rename the columns for our merges. We rename the column id to customer_id, so that orders and customers have a common column for the merge.  pd.merge(orders, customers.rename(columns={'id': 'customer_id'}))
orders = pd.read_csv('ordersdf.csv')
print(orders)
products = pd.read_csv('productsdf.csv')
print(products)
orders_products = pd.merge(products, orders.rename(columns={"id":"customer_id"}))
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
orders_products.to_csv('tempdelete.csv') 