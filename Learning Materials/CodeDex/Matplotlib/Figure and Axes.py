import matplotlib.pyplot as plt
import numpy as np

#plt.figure()           # 1. Set up the canvas
#plt.plot(x, y)         # 2. Create the plot
#plt.show()             # 3. Display the plot



decade_x = np.array([1980, 1990, 2000, 2010, 2020])
median_home_price_y = np.array([646000, 122900, 169000,221800, 336900])


plt.plot(decade_x, median_home_price_y)
plt.title("Median Home Price vs Decade")
plt.xlabel("Decade")
plt.ylabel("Median Home Price ($)")
plt.show()








#x_values = np.array([0, 1, 2, 3])
#y_values = np.array([3, 1, 4, 2])

#Creates 4 points which are
#(0, 3), (1, 1), (2, 4), (3, 2)

#Plotting
#plt.figure()
#plt.plot(x_values, y_values) #plotting x and y values