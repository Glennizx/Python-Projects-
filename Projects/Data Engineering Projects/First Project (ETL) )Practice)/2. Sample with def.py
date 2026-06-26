import pandas as pd

#1. Extract the file
def extract():
    df = pd.read_csv("/workspaces/Python-Projects-/Projects/Data Engineering Projects/First Project (ETL) )Practice)/csv files/raw_sales.csv")
    return df



#2. Transform the file
def transform(df):
    df['customer_name'] = df['customer_name'].fillna("Unknown").str.title().str.strip()
    df['email']= df['email'].fillna("Unknown").str.title().str.strip()
    df['product'] = df['product'].fillna("Unknown").str.title().str.strip()
    df['status']= df['status'].fillna("Unknown").str.title().str.strip()
    return df

#3. Load the file

def load(df):
    df.to_csv("cleaned.csv", index=False) 


#Running
df = extract()
df = transform(df)
load(df)


