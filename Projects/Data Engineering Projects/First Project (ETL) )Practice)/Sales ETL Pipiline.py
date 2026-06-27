import pandas as pd

#1. Extract the file
def extract():
    df = pd.read_csv("/workspaces/Python-Projects-/Projects/Data Engineering Projects/First Project (ETL) )Practice)/csv files/raw_sales.csv")
    return df



#2. Transform the file
def transform(df):
    df['customer_name'] = df['customer_name'].fillna("Unknown").str.title().str.strip()
    df['email']= df['email'].fillna("Unknown").str.lower().str.strip()
    df['product'] = df['product'].fillna("Unknown").str.title().str.strip()
    df['status']= df['status'].fillna("Unknown").str.title().str.strip()
    df['order_date'] = pd.to_datetime(
    df['order_date'],
    format='mixed',
    errors='coerce'  #Change the format to date type, format ='mixed' to let pandas know the date fill be mixed format
    #coerce for invalid dates
)
    df['order_date'] = df['order_date'].dt.strftime('%Y-%m-%d')

    return df
  

#3. Load the file

def load(df):
    df.to_csv("cleaned 2.csv", index=False) 


#Running
df = extract()
df = transform(df)
load(df)


