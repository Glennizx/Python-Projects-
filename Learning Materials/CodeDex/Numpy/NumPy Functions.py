import numpy as np

temperatures = np.array([[50, 51, 54, 59, 59, 53, 54, 51],
                         [45, 50, 38, 44, 40, 46, 43, 39]])

print(np.min(temperatures))       # Output: 38
print(np.max(temperatures))       # Output: 59
print(np.sum(temperatures))       # Output: 776
print(np.average(temperatures))   # Output: 48.5

print(np.sum(temperatures, axis =0)) #Sum of each column 50 and 45 #Output [95 101 92 103 99 99 97 90]
print(np.sum(temperatures, axis =1)) #Sum of each row 50+51+54+59+59+53+54+51 and 45+50+38+44+40+46+43+39