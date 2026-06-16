import numpy as np

# arange() function is used to create an array with regularly spaced values between a specified start and end value.

arr = np.arange(5)
print(arr) # Output: [0 1 2 3 4]

#arange() uses start, stop, and step parameters to generate the array. 
# The start parameter is the value at which the array starts (inclusive), 
# the stop parameter is the value at which the array ends (exclusive), and the step parameter is the difference 
# between each consecutive value in the array.

#Example
arr2= np.arange(start = 1, stop= 10, step= 3)

print(arr2) # Output: [1 4 7]

#Example 2: Halley's Comet orbits the sun every 75 years. We can use arange() to create an array of the years when Halley's Comet will be visible from Earth.

arr3= np.arange(start = 1986, stop = 3000, step= 75)
print(arr3)