import pandas as pd

df = pd.read_csv("/workspaces/Python-Projects-/Projects/Data Engineering Projects/First Project (ETL) )Practice)/csv files/raw_sales.csv")
df.info()

# Problems found
#1. 1 and 2 index has 1 missing value(null)
#2. Status column doesn't have a proper format same with customer_name
#3 order_date have 1 format not standardized


#