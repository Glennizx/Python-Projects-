import numpy as np


# 1D Arrays Sample
#arr = np.array([1, 2, 3, 4, 5, 6])

#2D arrays
#arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#2D arrays in a grid format (easier for the eyes)
#arr = np.array([
#  [1, 2, 3],  #Index 0
#  [4, 5, 6],  #Index 1
#  [7, 8, 9]   #Index 2
#])

#print(arr[0]) # Output: [1 2 3]


#Monthly Budget sampl;e

#gradebook = np.array([
 # [98, 98, 90, 84, 93, 73, 80],                # student 1
  #[93, 95, 75, 90, 89, 84, 76],                # student 2
  #[90, 89, 88, 84, 90, 67, 72],                # student 3
  #[89, 84, 69, 74, 84, 70, 72]                 # student 4
#])


egg_carton1 = np.array([
  [0.89, 0.90, 0.83, 0.89, 0.97, 0.98], 
  [0.95, 0.95, 0.89, 0.95, 0.23, 0.99]
])

egg_carton2 = np.array([
  [0.89, 0.95, 0.84, 0.92, 0.94, 0.93], 
  [0.93, 0.95, 0.02, 0.03, 0.23, 0.99]
])

egg_carton3 = np.array([
  [0.83, 0.95, 0.89, 0.54, 0.37, 0.92], 
  [0.98, 0.99, 0.19, 0.23, 0.89, 0.91]
])

average1 = np.average(egg_carton1)
average2 = np.average(egg_carton2)
average3 = np.average(egg_carton3)
print(f"Average 1: {average1:.2f}")  #
print(f"Average 2: {average2:.2f}")  
print(f"Average 3: {average3:.2f}")  

