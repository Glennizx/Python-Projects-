#Exercise 1:

# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")

elif not username.find(" ") == -1:
    print("Your username can't contain spaces")

elif not username.isalpha():
    print("Your username can't contain digits")

else:
    print(f"Welcome {username}!")


#Example 1
name = input("Enter your full name: ")
result =len(name)
print(result)

#Example 2
name = input("Enter your full name: ")

result = name.find("L") #finds the index of the first space in the name
                        #len reading starts at 0, so the first space is at index 5 for "Glenn Eze"
                        #if the character is not found, it returns -1           
print(result)


#Example 3
name = input("Enter your full name: ")
result = name.rfind("o")  #Find the last index of the character "o" 
                          #"Bro code" will result  in 6, because the last "o" is at index 5(starting from 0)
                          #if the character is not found, it returns -1
print(result)


#Example 4
name = input("Enter your full name: ")
name = name.capitalize() #capitalizes the first letter of the name and makes the rest lowercase
print(name)


#Example 5
name = input("Enter your full name: ")
name = name.capitalize() #capitalizes the first letter of the name and makes the rest lowercase
print(name)

#Example 6
phone_number = input("Enter your phone number: ")

result =phone_number.count("-") #counts the number of times the character "-" appears in the phone number
print(result)


#Example 7
phone_number = input("Enter your phone number: ")
phone_number = phone_number.replace("-"," ")
print(phone_number)




#NOTE: Other string methods
name = input("Enter your full name: ")
name = name.upper() #makes all letters uppercase
name = name.lower() #makes all letters lowercase
name = name.isupper() #returns True if all letters are uppercase, False otherwise
name = name.islower() #returns True if all letters are lowercase, False otherwise
name = name.isalpha() #returns True if all characters are letters or Alphabetical characters, False otherwise
name = name.isalnum() #returns True if all characters are letters or numbers, False otherwise
name = name.replace(" ", "_") #replaces all spaces with underscores
name = name.strip() #removes all leading and trailing spaces
name = name.split() #splits the name into a list of words
name = name.join("-") #joins the list of words into a string with hyphens between them
name = name.startswith("G") #returns True if the name starts with "G", False otherwise
name = name.endswith("e") #returns True if the name ends with "e", False
name = name.count("o") #returns the number of times "o" appears in the name
name = name.index("o") #returns the index of the first occurrence of "o" in the name, raises an error if "o" is not found
name = name.rindex("o") #returns the index of the last occurrence of "o" in the name, raises an error if "o" is not found
name = name.isdigit() #returns True if all characters are digits, False otherwise
name = name.isdecimal() #returns True if all characters are decimal characters, False otherwise
name = name.isnumeric() #returns True if all characters are numeric characters, False otherwise
#print(name)

#Comprehensive list of string methods: https://www.w3schools.com/python/python_ref_string.asp
#print(help(str)) #prints the documentation for the string class, including all methods and their descriptions

