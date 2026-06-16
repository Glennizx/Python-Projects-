#if = Do some only IF some condition is True
#    Else do something else






#Example 1
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
     print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up")


#Example 2
response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")

else:
    print("No food for you!")



#Exercise 3
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")

else:
    print(f"Hello {name}")


#Exercise 4
for_sale = False

if for_sale:
    print("This item is for sale")

else:
    print("This items is NOT for sale")


#Exercise 5
online = True
if online:
    print("The user is online")

else:
    print("The user is offline")