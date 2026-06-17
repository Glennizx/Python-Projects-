import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#Exercise


adoption_data = pd.DataFrame({
  'month': ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  'adoptions': [45000, 52000, 48000, 43000, 38000, 41000]
})

plt.plot(adoption_data['month'], adoption_data['adoptions'], color='g', linestyle ='-.')
plt.title('Catp Adoption through the month')
plt.xlabel('Month')
plt.ylabel('# of Adoptions')



#Sample: Importing from pandas 
#df = pd.DataFrame({
#  'hour_of_day': ['7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'],
#  'water_consumed_liters': [0.4, 0.5, 1, 0.2, 0, 0.3, 0, 0, 0, 0.7, 0, 0]
#})

#plt.figure()
#plt.plot(df['hour_of_day'], df['water_consumed_liters'])
#plt.show()