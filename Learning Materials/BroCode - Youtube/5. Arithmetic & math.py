import math
#Hypotenuse Calculator
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {round(c, 2)}cm²")


# Exercise 1
#friends = 10

#friends = friends + 1
#friends += 1  --> Augmented assignment operator
#friends -= 2
#friends *=  3
#friends /= 2
#friends = friends ** 2  --> friends to the power of 2 
#friends **= 2
#remainder = friends % 3  --> will give a result of a remainder. e.g. 10/3 = 3, Output will be 1


#Exercise 2
#x = 3.14
#y = 4
#z = 5

#result = round(x)
#result = abs(y)
#result = pow(4, 3)  -- > 4 raised to 3 = 4 * 4 * 4 = 64
#result = max(x, y, z)
#result = min(x, y, z)

#Exercise 3
#import math
#x = 9.1

#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x) --> if x is 9.1 it will become 10
#result = math.floor(x) --> if x is 9.1 it will become 9
#print(result)


#Exercise 4
#import math

#radius = float(input('Enter the radius of a circle: '))

#circumference = 2 * math.pi * radius

#print(f"The circumference is: {round(circumference, 2)}")

#Exercise 5
#import math

#radius = float(input("Enter the radius of a circle: "))
#area = math.pi * pow(radius, 2)

#print(f"The area of the circle is: {round(area, 2)}cm²")


