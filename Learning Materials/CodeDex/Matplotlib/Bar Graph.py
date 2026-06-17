import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.DataFrame({
  'aquarium': ['Monterrey Bay', 'Georgia Aquarium', 'Shedd Aquarium', 'National Aquarium'],
  'shark': [5, 4, 4, 2],
  'dolphin': [8, 12, 10, 5],
  'octopus': [7, 20, 8, 4],
  'sea turtle': [12, 5, 6, 3],
  'jellyfish': [30, 25, 20, 15]
})


plt.bar(df['aquarium'], df['shark'])

plt.xlabel('Aquarium')
plt.ylabel('Amount of sharks')
plt.show()



#Example
#data = {
#  'major': ['Math', 'Physics', 'CS', 'Chemistry', 'Biology'],
#  'num_students': [25, 30, 20, 15, 10]
#}

#df = pd.DataFrame(data)
#print(df)

#plt.bar(df['major'], df['num_students'])

#plt.title('Number of Students in Each Major')
#plt.xlabel('Major')
#plt.ylabel('Number of Students')

#plt.show()