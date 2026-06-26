import pandas as pd

df = pd.read_csv("/workspaces/Python-Projects-/Projects/Data Engineering Projects/First Project (ETL) )Practice)/csv files/raw_sales.csv")


#Cleaning the column_name
df['customer_name']= df['customer_name'].fillna('Unknown').str.title().str.strip()

#print(df)

#Exporting to excel

df.to_csv ("Clean name.csv", index= False)