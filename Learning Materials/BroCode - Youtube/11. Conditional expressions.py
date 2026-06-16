# Conditional expressions = A one line for the if-else statement (ternary operator)
#                           Print or assign of of the two values on a condition
#                           X if condition else


#Example 1
num = -5
print("Positive" if num > 0 else "Negative")

#Example 2
num = 11
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

#Example 3
temperature = 20
weather = "HOT" if temperature > 20 else "COLD"
print(weather)

#Example 4
user_role = "guest"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)