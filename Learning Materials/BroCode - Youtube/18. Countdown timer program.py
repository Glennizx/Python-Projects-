#Countdown timer program

import time

my_time = int(input("Enter the time in seconds:"))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) #pause the program for 1 second

print("Time's up!")







#Example 1 -> Countdown timer that counts down from a specified number of seconds
my_time = int(input("Enter the time in seconds:"))

for x in range(my_time, 0, -1):
    seconds = x % 60
    print(f"00:00:{seconds}")
    time.sleep(1) #pause the program for 1 second

print("Time's up!")