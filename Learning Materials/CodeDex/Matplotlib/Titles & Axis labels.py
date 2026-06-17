import matplotlib.pyplot as plt
import numpy as np



days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
steps = np.array([100, 200, 220, 5, 20])

plt.plot(days, steps)
plt.title('Steps taken of the week')
plt.xlabel('Day')
plt.ylabel('Steps taken')





#Sample
#days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
#emails = np.array([45, 38, 70, 49, 30])

#plt.figure()
#plt.plot(days, emails)
#plt.title('Emails received on the week of 12/2')
#plt.xlabel ('Day of the Week')
#plt.ylabel('Number of Emails')
#plt.show()