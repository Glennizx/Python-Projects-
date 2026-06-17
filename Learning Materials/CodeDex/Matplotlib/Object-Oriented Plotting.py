import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5'],
    'The_Housemaid_Sales': [31.01, 29.82, 22.12, 15.67, 12.63],
    'Marty_Supreme_Sales': [11.55, 30.75, 19.05, 11.67, 8.57]
})

fig, ax =plt.subplots()
ax.plot(df['Week'], df['The_Housemaid_Sales'], label= 'Housemaid Sales')
ax.plot(df['Week'], df['Marty_Supreme_Sales'], label= 'Marty Supreme Sales')
ax.set_title('Sales Comparison')
ax.set_xlabel('Week')
ax.set_ylabel('Sales Amount')
ax.legend()
plt.show()

#Example
#fig, ax = plt.subplots()
#ax.plot(x, y)
#ax.set_title('Title')
#plt.show()


#Example 2:


#df = pd.DataFrame({
#  'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
#  'Sales': [100, 120, 90, 150, 130],
#  'Profit': [20, 25, 18, 30, 28]
#})


#Instead of using plt.plot()

# fig represents the entire figure (the canvas that holds everything)
# ax represents a single plto area where data is shown


#fig, ax = plt.subplots()

#ax.plot(df['Month'], df['Sales'], label='Sales')
#ax.plot(df['Month'], df['Profit'], label='Profit')
#ax.set_title('Monthly Sales and Profit')
#ax.set_xlabel('Month')
#ax.set_ylabel('Amount')
#ax.legend()

#plt.show()
