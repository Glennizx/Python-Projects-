import numpy as np

#order = np.array([12.99, 9.99, 4.99, 12.99])
#print(order * 0.8) 
# This is way easier than if you do it with a Python list (where you have to use a for loop to update all the items in a list).

tallest_buildings = np.array([2717, 2227, 2073, 1972, 1966, 1819, 1776])

#Convert the height of building from feet to meters

converted_heights = tallest_buildings * 0.3048
print(converted_heights)
