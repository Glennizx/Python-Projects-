import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


toppings = np.array(['Pepperoni', 'Cheese', 'Mushroom', 'Pineapple', 'Prosciutto', 'Artichoke'])
orders = np.array([40, 25, 20, 15, 4, 5])

plt.pie(orders, labels= toppings, autopct ='%1.1f%%', explode=explode)
plt.title("Pizza Toppings")









#Example:
#flavors = np.array(['pumpkin', 'apple', 'blueberry', 'pecan', 'key lime', 'chocolate cream'])
#votes = np.array([24, 23, 11, 12, 10, 14])
#explode = [0.1, 0, 0, 0, 0, 0]

#plt.pie(votes, labels=flavors, autopct='%1.1f%%', explode=explode)
#plt.title("Favorite Pie Flavors 😋 ")
#plt.show()

#autopct means automatic percentages with:

# %d%%: no decimals
# %.1f%%: 1 decimal
# %.2f%%: 2 decimals