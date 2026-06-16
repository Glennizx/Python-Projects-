# collection = single "variable" used to store multiple values
# list [] = ordered, changeable, allows duplicate members
# tuple () = ordered, unchangeable, allows duplicate members
# set {} = unordered, unchangeable, no duplicate members


fruits = ("apple","orange", "banana", "coconut") # Tuples are ordered, so the items have a defined order, and that order will not change. Also, tuples are unchangeable, so we cannot change, add, or remove items after the tuple has been created. However, we can use the count() method to find out how many times a specified item occurs in a tuple, and the index() method to find the first occurrence of a specified item in a tuple.
print(fruits)

#fruits = {"apple","orange", "banana", "coconut"} # Sets are unordered, so the items will appear in a random order. Also, sets do not allow duplicate items, so if we try to add a duplicate item, it will not be added to the set.




#print(dir(fruits))
#print(help)
#print(len(fruits))
#print("apple" in fruits) # Will show if the item is in the list or not

#print(fruits[::-1])

#for fruit in fruits:
    #print(fruit) 



#fruits[0] = 'pineapple'  # Lists are changeable, so we can change the value of an item in a list by referring to its index number.

#for fruit in fruits:
    #print(fruit)


#fruits.append("pineapple") # Adds an element at the end of the list
#fruits.insert(1, "grape") # Adds an element at the specified position
#fruits.remove("banana") # Removes the specified item
#fruits.pop() # Removes the last item
#fruits.pop(1) # Removes the specified index
#fruits.clear() # Empties the list
#fruits.sort()]
#fruits.reverse()
#print(fruits.index("apple")) # Will show the index number of the first item with the specified value
#print(fruits.count("apple")) # Will show how many times the specified item occurs in the list

#fruits.add("pineapple")
#fruits.append("grape") # This will give an error because sets do not have the append() method. We can use the add() method to add an item to a set.


