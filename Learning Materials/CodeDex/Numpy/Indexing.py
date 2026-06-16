import numpy as np

#Indexing
coffee = np.array([3, 2, 1, 0, 1])
print(coffee[0])   # Output: 3
print(coffee[1])   # Output: 2
print(coffee[2])   # Output: 1
print(coffee[3])   # Output: 0
print(coffee[4])   # Output: 1


#Slicing
coffee = np.array([3, 2, 1, 0, 1])

print(coffee[0:2])    # Output: [3 2]
print(coffee[2:])     # Output: [1 0 1]
print(coffee[-2:])    # Output: [0 1]


#Sample
population = np.array([19571216, 19673200, 19854526, 20104710, 19463131, 19544098, 19593849, 19636391, 19657321, 19653431, 19626488])
print(population[10])