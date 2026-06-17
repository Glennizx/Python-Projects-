import matplotlib.pyplot as plt
import numpy as np

#There are three ways to set colors:

#Color names, such as 'red', 'green', 'blue', 'yellow', 'orange, 'skyblue'.
#Hex codes, such as #FF5733.
#Letter codes: 'r' red, 'g' green, 'b' blue, 'c' cyan, 'm' magenta, 'y' yellow, 'k' black, 'w' white.


#Exercise 1 
team_secret = np.array([20, 33, 22, 15, 40])
team_tnc = np.array([10, 15, 16, 22, 30])
team_round = np.array(['rd1', 'rd2', 'rd3', 'rd4,', 'rd5'])
plt.figure()
plt.plot(team_round, team_secret,label = 'Team Secret', color = 'red', linestyle = '-')
plt.plot(team_round, team_tnc,label = 'Team TNC', color = 'green', linestyle = '--')
plt.title("Score")
plt.xlabel('Round')
plt.ylabel('Score')
plt.legend()
plt.show()




#Example
#days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
#emails = np.array([45, 38, 70, 49, 30])

#plt.figure()
#plt.plot(days, emails, color='purple', linestyle='--')

#plt.title('Emails received on the week of 12/2')
#plt.xlabel('Day of the Week')
#plt.ylabel('Number of Emails')

#plt.show()
