# 2D Collections

#Example 2
num_pad = ( (1, 2 , 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")

)

for row in num_pad: #Iterate through each row in the num_pad
    for num in row: #Iterage through each number in the row
        print(num, end= " ")
    
    print() #Print a new line after each row is printed




# Example 1: A list of lists
#groceries = [{"apple", "orange", "banana", "coconut"},
 #            {"celery", "carrots", "potatoes"},
 #            {"chicken", "beef", "pork"}
#]

#for collection in groceries:
#    for food in collection:
#        print(food, end=" ")
    
#    print()