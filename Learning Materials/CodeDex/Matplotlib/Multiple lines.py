import numpy as np
import matplotlib.pyplot as plt



gas_bill = np.array([500, 200, 300, 500, 400, 606])
electric_bill = np.array([1000, 2000, 3000, 6000, 2000, 5000])

month = np.array(['January', 'February', 'March', 'April', 'May', 'June'])


plt.plot(month, gas_bill, label = 'Gas Bill')
plt.plot(month, electric_bill, label ='Electric Bill')

plt.title('Comparison of Gas & Electric Bill')
plt.xlabel('Month')
plt.ylabel('Bill (Pesos)')
plt.legend()
plt.show()
plt.figure()



#Example 1
#time = np.array([10, 20, 30, 40, 50, 60])

#uber = np.array([59.99, 82.43, 66.34, 62.15, 60.99, 55.21])
#lyft = np.array([65.81, 76.11, 72.45, 59.22, 55.26, 57.23])

#plt.figure()
#plt.legend()
#plt.plot(time, uber, label='Uber prices')
#plt.plot(time, lyft, label='Lyft prices')
#plt.show()