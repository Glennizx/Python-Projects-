import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('./data/gas_electricity_rent_expenses.csv') #Only works in the website

fig, ax = plt.subplots(figsize=(10,6))
category = df['Category'].unique()

for c in category: 
    month_data = df[df['Category'] == c]
    ax.plot(
      month_data["Month"],
      month_data["Amount_USD"],
      marker='o',
      label=c
    )

ax.set_title("Monthly Expenses")
ax.set_xlabel("Month")
ax.set_ylabel("Amount USD")

plt.show()