import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr.shape) # Output: (2, 4)
# The shape of the array is (2, 4) which means it has 2 rows and 4 columns.



arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) 

print(arr.shape)     # Output: (4, 3)  (r x c) or (row x column)
 # It means that the array has 4 rows and 3 columns.

#Use .reshape() to change the shape of the array

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8]) 
new_arr = arr.reshape(2, 4)

print(new_arr)
# Output:
# [[1 2 3 4]
#  [5 6 7 8]]


#Exercise 1:
month_results = np.array([56, 100, 33, 0, 45, 45, 46, 34, 89, 180, 60, 45, 45, 44, 46, 45, 0, 0, 15, 90, 301, 197, 20, 60, 45, 45, 42, 45])