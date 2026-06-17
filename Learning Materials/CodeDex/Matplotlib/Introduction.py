#%%

import matplotlib.pyplot as plt
import numpy as np


year = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])
revenue = np.array([4.8, 5.3, 2.1, 3.4, 5.9, 6.5, 7.2, 8.1])

plt.figure()
plt.plot(year, revenue)

plt.title('Action Genre Box Office Revenue (2018-2025)')
plt.xlabel('Year')
plt.ylabel('Revenue (billions USD)')

plt.show()