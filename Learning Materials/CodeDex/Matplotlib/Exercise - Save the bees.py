import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/workspaces/Python-Projects-/Learning Materials/CodeDex/Matplotlib/save_the_bees.csv')

#df.head()            # View the first few rows of the dataset
#df.tail()            # View the last few rows
#df.columns           # See column names
#df['state'].head()   # Look at a single column

#Total number of colonies (Bar)
pick_states = ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado']
df_filtered = df[df['state'].isin(pick_states)]
df_grouped = df_filtered.groupby('state', as_index=False)['num_colonies'].sum()

plt.bar(df_grouped['state'], df_grouped['num_colonies'], color='red')

plt.xlabel('State')
plt.ylabel("Number of colonies")
plt.show()





