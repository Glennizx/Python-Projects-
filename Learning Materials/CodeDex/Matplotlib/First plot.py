import matplotlib.pyplot as plt
import numpy as np


#plt.plot(x,y) #plotting x and y values


#Sample Exercise

coffee_amt = np.array([2, 3, 5, 6 , 7])
caffeine_amt = np.array([0.5, 0.75, 1.25, 1.5, 1.75])

plt.plot(coffee_amt, caffeine_amt) #plotting x and y values
plt.title("Caffeine vs Coffee") #title of the graph
plt.xlabel("Cups of Coffee") #label for x-axis
plt.ylabel("Caffeine Amount (mg)") #label for y-axis




#Sample data (Energy vs Coffee)

coffee = np.array([0, 1, 2, 3, 4, 5])
energy = np.array([3, 6, 8, 9, 8.5, 7])



plt.plot(coffee, energy) #plotting x and y values
plt.title("Energy vs Coffee") #title of the graph
plt.xlabel("Cups of Coffee") #label for x-axis
plt.ylabel("Energy Level") #label for y-axis