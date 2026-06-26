import pandas as pd

df = pd.read_csv("/workspaces/Python-Projects-/Projects/Data Engineering Projects/First Project (ETL) )Practice)/csv files/raw_sales.csv")


#Cleaning the column_name
df['customer_name']= df['customer_name'].str.title()
df['customer_name']= df['customer_name'].fillna('Unknown')
#print(df)

#Exporting to excel
df.to_excel("Clean name.xlsx", index= False)
df.to_csv ("Clean name.csv", index= False)