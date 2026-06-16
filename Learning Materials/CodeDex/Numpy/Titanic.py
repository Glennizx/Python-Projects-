import numpy as np

passengers = np.array([
   [1, 0, 3, 22],
   [2, 1, 1, 38],
   [3, 1, 3, 26],
   [4, 1, 1, 35],
   [5, 0, 3, 35],
   [6, 0, 3, 18],
   [7, 0, 1, 54],
   [8, 0, 3, 2],
   [9, 1, 3, 27],
  [10, 1, 2, 14],
  [11, 1, 3, 4],
  [12, 1, 1, 58],
  [13, 0, 3, 20],
  [14, 0, 3, 39],
  [15, 0, 3, 14],
  [16, 1, 2, 55],
  [17, 0, 3, 2],
  [18, 1, 2, 12],
  [19, 0, 3, 31],
  [20, 1, 3, 8],
  [21, 0, 2, 35],
  [22, 1, 2, 34],
  [23, 1, 3, 15],
  [24, 1, 1, 28],
  [25, 0, 3, 8],
  [26, 1, 3, 38],
  [27, 0, 3, 2],
  [28, 0, 1, 1],
  [29, 1, 3, 5],
  [30, 0, 3, 18],
  [31, 0, 1, 40],
  [32, 1, 1, 70],
  [33, 1, 3, 33],
  [34, 0, 2, 66],
  [35, 0, 1, 28],
  [36, 0, 1, 42],
  [37, 1, 3, 5],
  [38, 0, 3, 18],
  [39, 0, 3, 18],
  [40, 1, 3, 14],
  [41, 0, 3, 40],
  [42, 0, 2, 27],
  [43, 0, 3, 29],
  [44, 1, 2, 0],
  [45, 1, 3, 19],
  [46, 0, 3, 33],
  [47, 0, 3, 14],
  [48, 1, 3, 22],
  [49, 0, 3, 41],
  [50, 0, 3, 18]
])


print(passengers.shape) # Shape of the array is (50, 4) which means it has 50 rows and 4 columns.
average_age = np.average(passengers, axis = 0)[3]
print(average_age) # Output: 25.5
oldest_age = np.max(passengers, axis = 0)[3]
print(oldest_age) # Output: 70

count_ones = np.sum(passengers[:, 1] ==1) # Count the number of passengers in the second column (index 1) that are equal to 1 (indicating they survived).
print(count_ones) # Output: 22
number_of_survivor = (count_ones / passengers.shape[0]) * 100 # Calculate the percentage of survivors by dividing the count of survivors by the total number of passengers (the number of rows in the array) and multiplying by 100.
print(f"Percentage of survivors: {number_of_survivor:.2f}%") # Output: Percentage of survivors: 44.00%